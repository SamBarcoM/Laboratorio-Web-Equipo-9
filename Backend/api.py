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

uri = ""
db = None

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

assistant_api_key = os.getenv("assistant_api_key")


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

def watson_response(session_id1, message):
    
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

    ## Insertar el intent, activities y la pregunta
    try:
        request_data = {
            "intent": response.get("response").get("output").get("intents")[0].get("intent"),
            "entity-value": response.get("response").get("output").get("entities")[0].get("value"),
            "message": message,
        }
    except:
        request_data = {
            "intent": response.get("response").get("output").get("intents")[0].get("intent"),
            "entity-value": None,
            "message": message,
        }
    
    # Almacena el request en la colección requests
    print(request_data)
    create("requests", request_data)

    ## Conectar a MongoDB buscar en web coleccion responses el documento con intent de la respuesta 
    try:
        htmlresponse = retrieve("responses", request_data.get("intent"), request_data.get("entity-value"))
    except:
        htmlresponse = "<p>error: No html-response found</p>"
    
    return htmlresponse

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

# Mongo functions
def connect_mongo():
    global db
    client = pymongo.MongoClient(uri)
    db = client.get_default_database()

# CRUD

def create( collection_name, document ):
    global db
    collection = db[collection_name]
    collection.insert_one(document)

def retrieve( collection_name, intent, entity ):
    global db
    collection = db[collection_name]
    if entity == None:
        result = collection.find_one({"intent":intent})
    else:
        result = collection.find_one({"intent":intent, "entity":entity})
    return result.get("html")


class GET_MESSAGE(Resource):
    def post(self):
        message = request.json["message"]

        print ("message: "+ message )

        resp = watson_response(watson_create_session(), request.json["message"] )
        # return jsonify( este_es_el_mensaje = request.json["message"])
        return jsonify(
            text=resp,
            # intent=resp['response']['output']['intents'][0]["intent"],
        )


api.add_resource(GET_MESSAGE, '/getMessage')  # Route_1

#connect to mongo
try:
    connect_mongo()
except:
    print("Couldn't connect to MongoDB")

if __name__ == '__main__':
    app.run(port='5002')
