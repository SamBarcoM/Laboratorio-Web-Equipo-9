# API
import os
import json
import logging
import requests

import flask
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from dotenv import load_dotenv
from flask_api import status

from jsonschema import validate, ValidationError
from ibm_watson import AssistantV2, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from flask import jsonify

#MongoDB
import sys
import pymongo

#Twilio
from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 

uri = ""
db = None
email = "a01196844@itesm.mx"

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

assistant_api_key = os.getenv("assistant_api_key")

carousel_count = 0


def watson_create_session():

    iam_apikey = os.getenv("assistant_api_key")
    assistant_url = os.getenv("assistant_url")
    assistant_version = os.getenv("assistant_version")

    assistant = watson_instance(iam_apikey, assistant_url, assistant_version)

    try:
        watson_session = assistant.create_session(
            assistant_id=os.getenv("assistant_id")
        ).get_result()
        watson_session_id = watson_session["session_id"]
    except KeyError:
        _logger.error("The session wasn't created")
        return jsonify({"error": "Error creating the session"}), status.HTTP_503_SERVICE_UNAVAILABLE

    return watson_session_id

def watson_response(session_id1, message, channel):
    
    iam_apikey = os.getenv("assistant_api_key")
    assistant_url = os.getenv("assistant_url")
    assistant_version = os.getenv("assistant_version")

    assistant = watson_instance(iam_apikey, assistant_url, assistant_version)
    context = {}
    watson_session_id = session_id1

    try:
        watson_response = assistant.message(
            assistant_id=os.getenv("assistant_id"),
            session_id=watson_session_id,
            input={
                'message_type': 'text',
                'text': message,
                'options': {
                    'return_context': True
                }
            },
            context=context
        ).get_result()
    except ValueError as ex:
        _logger.error("Value error: %s", ex)
        return jsonify({'error': "Value error"}), status.HTTP_500_INTERNAL_SERVER_ERROR
    except ApiException:
        try:
            watson_session = assistant.create_session(
                assistant_id=os.getenv("assistant_id")
            ).get_result()
            watson_session_id = watson_session["session_id"]

            watson_response = assistant.message(
                assistant_id=os.getenv("assistant_id"),
                session_id=watson_session_id,
                input={
                    'message_type': 'text',
                    'text': message,
                    'options': {
                        'return_context': True
                    }
                },
                context=context
            ).get_result()
        except KeyError:
            _logger.error("The session wasn't created")
            return jsonify({"error": "Error creating the session"}), status.HTTP_503_SERVICE_UNAVAILABLE

    try:
        del watson_response["context"]["global"]["session_id"]
    except:
        pass

    response = {
        "response": watson_response,
        "session_id": watson_session_id
    }

    ## Crear un documetno para diferentes tipos de mensajes
    # Mensaje tiene intent y entity
    try:
        request_data = {
            "intent": response.get("response").get("output").get("intents")[0].get("intent"),
            "entity-value": response.get("response").get("output").get("entities")[0].get("value"),
            "message": message,
        }
    except:
        # Mensaje tiene intent pero no entity
        try:
            request_data = {
                "intent": response.get("response").get("output").get("intents")[0].get("intent"),
                "entity-value": None,
                "message": message,
            }
        # Mensaje desconocido por AI agent
        except:
            request_data = {
                "intent": None,
                "entity-value": None,
                "message": message,
            }
    
    # Almacena el request en la colección requests de MongoDB
    #print(request_data)
    create("requests", request_data)

    if channel == "web":
        # Si el intent identificado con Watson tiene una respuesta en MongoDB envía la respuesta indicada
        try:
            print(request_data.get("intent"), request_data.get("entity-value"))
            # Depende de cada intent el cómo se va a armar el html que verá el usuario, hay cuatro opciones: sin intent, "meet requirements", "meet activity" y "contact"
            # Debe regresar los pasos para completar la actividad especifica
            if request_data.get("intent")=="questionMeetActivityRequirements":
                # First, retrieve user status on asked activities
                user_data = retrieveCompletedActivities(email,request_data.get("entity-value"))
                requirement = retrieveRequirement(request_data.get("entity-value"))
                # If activity returns one, it has been completed
                if user_data[request_data.get("entity-value")] == 1:
                    print("user has completed the ", request_data.get("entity-value"))
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "positive", channel)
                # If activity returns zero, it hasn't been completed
                elif user_data[request_data.get("entity-value")] == 0:
                    print("user hasn't completed the ", request_data.get("entity-value"))
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "negative", channel)
                response = replaceVariables(response, requirement, channel )
                print("activity requirements")
            elif request_data.get("intent")=="questionMeetActivity":
                print("activity completeness")
                # First, retrieve user status on asked activities
                user_data = retrieveCompletedActivities(email,request_data.get("entity-value"))
                requirement = retrieveRequirement(request_data.get("entity-value"))
                # If activity returns one, it has been completed
                if user_data[request_data.get("entity-value")] == 1:
                    print("user has completed the ", request_data.get("entity-value"))
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "positive", channel)
                # If activity returns zero, it hasn't been completed
                elif user_data[request_data.get("entity-value")] == 0:
                    print("user hasn't completed the ", request_data.get("entity-value"))
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "negative", channel)
                response = replaceVariables(response, requirement, channel )
            elif request_data.get("intent")=="questionContact":
                # First retrieve requirement
                requirement = retrieveRequirement(request_data.get("entity-value"))
                # Then retrieve the answer
                response = retrieveAnswer("responses", request_data.get("intent"), None, None, channel)
                # Substitute data in contact card with specific requirement values
                response = replaceVariables(response, requirement, channel )
                print("contact")    
            elif request_data.get("intent")=="questionIncompleteActivities":
                user_data = retrieveCompletedActivities(email,None)
                user_activities = retrieveActivitiesData(user_data,0)
                # No activities are left to complete
                if len(user_activities) == 0:
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "empty", channel)
                # User has some activities to complete
                else:
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "list", channel)
                response = add_carousel(response, create_carousel(user_activities))
                print("incomplete")
            elif request_data.get("intent")=="questionCompletedActivities":
                user_data = retrieveCompletedActivities(email,None)
                user_activities = retrieveActivitiesData(user_data,1)
                # No activities have been completed
                if len(user_activities) == 0:
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "empty", channel)
                # User has some activities completed
                else:
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "list", channel)
                response = add_carousel(response, create_carousel(user_activities))
                print("completed")

            else:
                print("other")
                user_data = retrieveStudentInfo(email)
                response = retrieveAnswer("responses", request_data.get("intent"), request_data.get("entity-value"), None, channel)
                response = replaceVariables(response, user_data, channel )
        # De lo contrario, indica al usuario que no entendió a lo que se refería para que vuelva a ingresar la pregunta
        except:
            response = "<p>Sorry, I didn't understand</p>"
    
    elif channel == "telephone":
        if request_data.get("intent")=="questionMeetActivityRequirements":
            # First, retrieve user status on asked activities
            user_data = retrieveCompletedActivities(email,request_data.get("entity-value"))
            requirement = retrieveRequirement(request_data.get("entity-value"))
            # If activity returns one, it has been completed
            if user_data[request_data.get("entity-value")] == 1:
                print("user has completed the ", request_data.get("entity-value"))
                response = retrieveAnswer("responses", request_data.get("intent"), None, "positive", channel)
            # If activity returns zero, it hasn't been completed
            elif user_data[request_data.get("entity-value")] == 0:
                print("user hasn't completed the ", request_data.get("entity-value"))
                response = retrieveAnswer("responses", request_data.get("intent"), None, "negative", channel)
            response = replaceVariables(response, requirement, channel)
            print("activity requirements")
        elif request_data.get("intent")=="questionMeetActivity":
            print("activity completeness")
            # First, retrieve user status on asked activities
            user_data = retrieveCompletedActivities(email,request_data.get("entity-value"))
            requirement = retrieveRequirement(request_data.get("entity-value"))
            # If activity returns one, it has been completed
            if user_data[request_data.get("entity-value")] == 1:
                print("user has completed the ", request_data.get("entity-value"))
                response = retrieveAnswer("responses", request_data.get("intent"), None, "positive", channel)
            # If activity returns zero, it hasn't been completed
            elif user_data[request_data.get("entity-value")] == 0:
                print("user hasn't completed the ", request_data.get("entity-value"))
                response = retrieveAnswer("responses", request_data.get("intent"), None, "negative", channel)
            response = replaceVariables(response, requirement, channel )
        elif request_data.get("intent")=="questionContact":
            # First retrieve requirement
            print(request_data)
            requirement = retrieveRequirement(request_data.get("entity-value"))
            # Then retrieve the answer
            response = retrieveAnswer("responses", request_data.get("intent"), None, None, channel)
            # Substitute data in contact card with specific requirement values
            print(requirement)
            response = replaceVariables(response, requirement, channel )
            print("contact")    
        elif request_data.get("intent")=="questionIncompleteActivities":
                user_data = retrieveCompletedActivities(email,None)
                user_activities = retrieveActivitiesData(user_data,0)
                print(user_activities)
                # No activities are left to complete
                if len(user_activities) == 0:
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "empty", channel)
                # User has some activities to complete
                else:
                    response = retrieveAnswer("responses", request_data.get("intent"), None, "list", channel)
                print(response)
                response = add_carousel(response, create_whatsapp_details_list(user_activities))
                print("incomplete")
        elif request_data.get("intent")=="questionCompletedActivities":
            user_data = retrieveCompletedActivities(email,None)
            user_activities = retrieveActivitiesData(user_data,1)
            # No activities have been completed
            if len(user_activities) == 0:
                response = retrieveAnswer("responses", request_data.get("intent"), None, "empty", channel)
            # User has some activities completed
            else:
                response = retrieveAnswer("responses", request_data.get("intent"), None, "list", channel)
            response = add_carousel(response, create_whatsapp_details_list(user_activities))
            print("completed")
        else:
                print("other")
                user_data = retrieveStudentInfo(email)
                response = retrieveAnswer("responses", request_data.get("intent"), request_data.get("entity-value"), None, channel)
                response = replaceVariables(response, user_data, channel )
    return response

def watson_instance(iam_apikey: str, url: str, version: str = "2019-02-28") -> AssistantV2:
    try:
        authenticator = IAMAuthenticator(iam_apikey)
        assistant = AssistantV2(
            authenticator=authenticator,
            version=version
        )
        assistant.set_service_url(url)
    except ApiException as error:
        _logger.error("%s - %s", error.code, error.message)
        return jsonify({'error': str(error.message)}), error.code

    return assistant

# Helper functions
# Create an html list with an array
def create_list( array, channel ):
    if channel == "web":
        result = "<ul>"
        for line in array:
            result = result + "<li>" + line + "</li>"
        result = result + "</ul>"
    if channel == "telephone":
        result = ""
        for line in array:
            result = result + "\n - " + line
        result = result + "\n"
    return result

def create_carousel( itemsArray ):
    # Creates needed tags at the beginning of the carousel
    global carousel_count
    result = "<div id=\"carousel" + str(carousel_count) + "\" class=\"carousel slide\" data-ride=\"carousel\">"
    indicators = "<ol class=\"carousel-indicators\">"
    items = "<div class=\"carousel-inner\"> "
    count = 0
    
    for item in itemsArray:
        if count == 0:
            indicators = indicators + '<li data-target="#carousel' + str(carousel_count) + '" data-slide-to="0" class="active"></li>'
            items = items + """
                <div class="carousel-item active">       
                <img class="d-block w-100" src="https://source.unsplash.com/random/400x400" alt="
            """ + str(count) + """
                slide"/>     
                <div class="carousel-caption d-none d-md-block">
                    <h5>
            """ + item['name'] + """
                </h5>
                <p>
            """ + item['description'] + """
                </div>
                </div>
            """
        else:
            indicators = indicators + '<li data-target="#carousel' + str(carousel_count) + '" data-slide-to="' + str(count) + '" class="active"></li>'
            items = items + """
                <div class="carousel-item">       
                <img class="d-block w-100" src="https://source.unsplash.com/random/400x400" alt="
            """ + str(count) + """
                slide"/>     
                <div class="carousel-caption d-none d-md-block">
                    <h5>
            """ + item['name'] + """
                </h5>
                <p>
            """ + item['description'] + """
                </div>
                </div>
            """
        count = count + 1
    
    # Closes the tags added
    indicators = indicators + "</ol> " 
    items = items + "</div>"
    controls = """
        <a class="carousel-control-prev" href="#carousel""" + str(carousel_count) + """" role="button" data-slide="prev">     
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>     <span class="sr-only">Previous</span>  
        </a>   
        <a class="carousel-control-next" href="#carousel""" + str(carousel_count) + """" role="button" data-slide="next">     
            <span class="carousel-control-next-icon" aria-hidden="true"></span>     <span class="sr-only">Next</span>   
        </a>
    """
    result = result + indicators + items + controls + "</div>"
    carousel_count = carousel_count + 1
    return result

# As we can't use carousel with whatsapp, we will implement a new list more detailed
def create_whatsapp_details_list( itemsArray ):
    items = "\n"
    for item in itemsArray:
        items = items + "*_" + item['name'] + ":_* " + item['description'] + "\n"
    return items

def add_carousel( html, carousel):
    html = html.replace("$$$carousel$$$", carousel)
    return html

# Adapt html generic response to asked requirement
def replaceVariables( html, requirementJSON, channel ):
    out = "$$$*$$$"
    result = html
    for key,value in requirementJSON.items():
        out = out.replace("*",key)
        if isinstance(value,list):
            value = create_list(value, channel)
        try:
            result = result.replace(out,value)
        except:
            print("Cant replace ",out)
        out = "$$$*$$$"
    print(result)
    return result


# Mongo functions
# Connect to mongoDB
def connect_mongo():
    global db
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

# CRUD
# Inserta un documento (document) en la base de datos collection_name
def create( collection_name, document ):
    global db
    collection = db[collection_name]
    collection.insert_one(document)

# Recupera un documento de MongoDB en la colección collection_name que coincide con intent y entity
def retrieveAnswer( collection_name, intent, entity, status, channel ):
    global db
    collection = db[collection_name]
    if entity == None:
        if status == None:
            result = collection.find_one({"intent":intent, "response":{ '$exists': False }, "entity": { '$exists': False }})
        else:
            result = collection.find_one({"intent":intent, "response": status, "entity": { '$exists': False }})
    else:
        if status == None:
            result = collection.find_one({"intent":intent, "response":{ '$exists': False }, "entity":entity})
        else:
            result = collection.find_one({"intent":intent, "response": status, "entity":entity})

    if channel == "web":
        returnResult = result.get("html")
    elif channel == "telephone":
        returnResult = result.get("telephone")
    
    return returnResult

# Recupera un documento de MongoDB en la colección requirements (entities de Watson), documento con los datos de una entidad
def retrieveRequirement( entity ):
    global db
    collection = db["requirements"]
    if entity == None:
        return "error on retrieveRequirement"
    else:
        result = collection.find_one({"id":entity})
    return result

def retrieveCompletedActivities( student_mail, entity):
    global db
    collection = db["students"]
    if entity == None:
        result = collection.find_one({"mail":student_mail}, {"_id":0,"name":0,"mail":0,"campus":0,"student_number":0})
    else:
        result = collection.find_one({"mail":student_mail}, {entity:1})
    return result

def retrieveStudentInfo( student_mail ):
    global db
    collection = db["students"]
    result = collection.find_one({"mail":student_mail}, {"_id":0,"name":1,"mail":1,"campus":1,"student_number":1})
    print(result)
    return result

def retrieveActivitiesData( user_data, completeness ):
    global db
    collection = db["requirements"]
    activities = []
    for key, value in user_data.items():
        if value == completeness:
            activities.append(collection.find_one({"id":key}))
    return activities

# WHATSAPP Functions
def send_message( phone, message ):
    message = message.replace("\\n","""
    """)
    print(message)
    client.messages.create( 
                              from_= 'whatsapp:+14155238886',  
                              body = message,      
                              to = phone 
                          ) 


class GET_MESSAGE(Resource):
    def post(self):
        message = request.json["message"]
        print ("message: "+ message )
        resp = watson_response(watson_create_session(), request.json["message"], "web" )
        # return jsonify( este_es_el_mensaje = request.json["message"])
        return jsonify(
            text=resp,
        )

class GET_MESSAGE_WHATSAPP(Resource):
    def post(self):
        number = request.form['From']
        message_body = request.form['Body']
        print ("message: "+ message_body + " phone " + number)
        resp = watson_response(watson_create_session(), message_body, "telephone" )
        send_message(number, resp)
        return


api.add_resource(GET_MESSAGE, '/getMessage')  # Route_1
api.add_resource(GET_MESSAGE_WHATSAPP, '/getMessageWhatsapp')  # Route_2

#connect to mongo
try:
    connect_mongo()
except:
    print("Couldn't connect to MongoDB")

if __name__ == '__main__':
    app.run(port='5002')
