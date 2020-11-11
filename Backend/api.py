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

#Twilio
from twilio.rest import Client 

# Classes
from text_functions import textBuilder
from mongo_functions import mongoController
from twilio_functions import whatsappController
 
account_sid = 'ACcd05049a2f41238d3c7a8f840e098a1a' 
auth_token = '9d85f161adf8dd0c4ddfb823d7cc22df' 
client = Client(account_sid, auth_token) 

email = "a01196844@itesm.mx"

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

assistant_api_key = os.getenv("assistant_api_key")

txtBldr = textBuilder()
dbController = mongoController()
waController = whatsappController()

# WATSON FUNCTIONS

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
    dbController.create("requests", request_data)

    if channel == "web":
        # Si el intent identificado con Watson tiene una respuesta en MongoDB envía la respuesta indicada
        try:
            print(request_data.get("intent"), request_data.get("entity-value"))
            # Depende de cada intent el cómo se va a armar el html que verá el usuario, hay cuatro opciones: sin intent, "meet requirements", "meet activity" y "contact"
            # Debe regresar los pasos para completar la actividad especifica
            if request_data.get("intent")=="questionMeetActivityRequirements":
                # First, retrieve user status on asked activities
                user_data = dbController.retrieve_completed_activities(email,request_data.get("entity-value"))
                requirement = dbController.retrieve_requirement(request_data.get("entity-value"))
                # If activity returns one, it has been completed
                if user_data[request_data.get("entity-value")] == 1:
                    print("user has completed the ", request_data.get("entity-value"))
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "positive", channel)
                # If activity returns zero, it hasn't been completed
                elif user_data[request_data.get("entity-value")] == 0:
                    print("user hasn't completed the ", request_data.get("entity-value"))
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "negative", channel)
                response = txtBldr.merge_text(response, requirement, channel )
                print("activity requirements")
            elif request_data.get("intent")=="questionMeetActivity":
                print("activity completeness")
                # First, retrieve user status on asked activities
                user_data = dbController.retrieve_completed_activities(email,request_data.get("entity-value"))
                requirement = dbController.retrieve_requirement(request_data.get("entity-value"))
                # If activity returns one, it has been completed
                if user_data[request_data.get("entity-value")] == 1:
                    print("user has completed the ", request_data.get("entity-value"))
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "positive", channel)
                # If activity returns zero, it hasn't been completed
                elif user_data[request_data.get("entity-value")] == 0:
                    print("user hasn't completed the ", request_data.get("entity-value"))
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "negative", channel)
                response = txtBldr.merge_text(response, requirement, channel )
            elif request_data.get("intent")=="questionContact":
                # First retrieve requirement
                requirement = dbController.retrieve_requirement(request_data.get("entity-value"))
                # Then retrieve the answer
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, None, channel)
                # Substitute data in contact card with specific requirement values
                response = txtBldr.merge_text(response, requirement, channel )
                print("contact")    
            elif request_data.get("intent")=="questionIncompleteActivities":
                user_data = dbController.retrieve_completed_activities(email,None)
                user_activities = dbController.retrieve_activities_data(user_data,0)
                
                # No activities are left to complete
                if len(user_activities) == 0:
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "empty", channel)
                # User has some activities to complete
                else:
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "list", channel)
                response = txtBldr.merge_carousel(response, txtBldr.create_carousel(user_activities))
                print("incomplete")
            elif request_data.get("intent")=="questionCompletedActivities":
                user_data = dbController.retrieve_completed_activities(email,None)
                user_activities = dbController.retrieve_activities_data(user_data,1)
                # No activities have been completed
                if len(user_activities) == 0:
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "empty", channel)
                # User has some activities completed
                else:
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "list", channel)
                response = txtBldr.merge_carousel(response, txtBldr.create_carousel(user_activities))
                print("completed")

            else:
                print("other")
                user_data = dbController.retrieve_student_info(email)
                response = dbController.retrieve_answer("responses", request_data.get("intent"), request_data.get("entity-value"), None, channel)
                response = txtBldr.merge_text(response, user_data, channel )
        # De lo contrario, indica al usuario que no entendió a lo que se refería para que vuelva a ingresar la pregunta
        except:
            response = "<p>Sorry, I didn't understand</p>"
    
    elif channel == "telephone":
        if request_data.get("intent")=="questionMeetActivityRequirements":
            # First, retrieve user status on asked activities
            user_data = dbController.retrieve_completed_activities(email,request_data.get("entity-value"))
            requirement = dbController.retrieve_requirement(request_data.get("entity-value"))
            # If activity returns one, it has been completed
            if user_data[request_data.get("entity-value")] == 1:
                print("user has completed the ", request_data.get("entity-value"))
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "positive", channel)
            # If activity returns zero, it hasn't been completed
            elif user_data[request_data.get("entity-value")] == 0:
                print("user hasn't completed the ", request_data.get("entity-value"))
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "negative", channel)
            response = txtBldr.merge_text(response, requirement, channel)
            print("activity requirements")
        elif request_data.get("intent")=="questionMeetActivity":
            print("activity completeness")
            # First, retrieve user status on asked activities
            user_data = dbController.retrieve_completed_activities(email,request_data.get("entity-value"))
            requirement = dbController.retrieve_requirement(request_data.get("entity-value"))
            # If activity returns one, it has been completed
            if user_data[request_data.get("entity-value")] == 1:
                print("user has completed the ", request_data.get("entity-value"))
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "positive", channel)
            # If activity returns zero, it hasn't been completed
            elif user_data[request_data.get("entity-value")] == 0:
                print("user hasn't completed the ", request_data.get("entity-value"))
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "negative", channel)
            response = txtBldr.merge_text(response, requirement, channel )
        elif request_data.get("intent")=="questionContact":
            # First retrieve requirement
            print(request_data)
            requirement = dbController.retrieve_requirement(request_data.get("entity-value"))
            # Then retrieve the answer
            response = dbController.retrieve_answer("responses", request_data.get("intent"), None, None, channel)
            # Substitute data in contact card with specific requirement values
            print(requirement)
            response = txtBldr.merge_text(response, requirement, channel )
            print("contact")    
        elif request_data.get("intent")=="questionIncompleteActivities":
                user_data = dbController.retrieve_completed_activities(email,None)
                user_activities = dbController.retrieve_activities_data(user_data,0)
                print(user_activities)
                # No activities are left to complete
                if len(user_activities) == 0:
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "empty", channel)
                # User has some activities to complete
                else:
                    response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "list", channel)
                print(response)
                response = txtBldr.merge_carousel(response, txtBldr.create_detail_list(user_activities))
                print("incomplete")
        elif request_data.get("intent")=="questionCompletedActivities":
            user_data = dbController.retrieve_completed_activities(email,None)
            user_activities = dbController.retrieve_activities_data(user_data,1)
            # No activities have been completed
            if len(user_activities) == 0:
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "empty", channel)
            # User has some activities completed
            else:
                response = dbController.retrieve_answer("responses", request_data.get("intent"), None, "list", channel)
            response = txtBldr.merge_carousel(response, txtBldr.create_detail_list(user_activities))
            print("completed")
        else:
                print("other")
                user_data = dbController.retrieve_student_info(email)
                response = dbController.retrieve_answer("responses", request_data.get("intent"), request_data.get("entity-value"), None, channel)
                response = txtBldr.merge_text(response, user_data, channel )
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

# WHATSAPP FUNCTIONS
# Function to send message
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
        waController.send_message(number, resp)
        return

api.add_resource(GET_MESSAGE, '/getMessage')  # Route_1
api.add_resource(GET_MESSAGE_WHATSAPP, '/getMessageWhatsapp')  # Route_2

#connect to mongo
try:
    dbController.connect_mongo()
except:
    print("Couldn't connect to MongoDB")

if __name__ == '__main__':
    app.run(port='5002')
