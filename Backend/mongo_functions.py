import os
from dotenv import load_dotenv

#MongoDB
import sys
import pymongo

load_dotenv()

class mongoController():
    # Singleton instance.
    INSTANCE = None

    def __init__( self ):
        self.uri = os.getenv("mongo_uri")
        self.db = None
        return
    
    # Connect to mongoDB
    def connect_mongo( self ):
        print(self.uri)
        client = pymongo.MongoClient(self.uri)
        self.db = client.get_default_database()
        return

    # CRUD
    # Insert 'document' in collection 'collection_name'
    def create( self, collection_name, document ):
        collection = self.db[collection_name]
        collection.insert_one(document)
        return
    
    # Retrieve all requests.
    def retrieve_requests(self):
        collection = self.db["requests"]
        requests = []
        for request in collection.find():
            requests.append(request)
        return requests
    
    def get_unique_users_per_month(self):
        collection = self.db["requests"]
        months = []
        calculation_cursor = collection.aggregate([
            {
                '$project': {
                    'user_email': 1,
                    'month': { '$month': '$created_at'},
                }
            },
            {
                '$group': {
                    '_id': '$month',
                    'total': { '$sum': 1 }
                }
            }
        ])

        for calculation in calculation_cursor:
            months.append(calculation)
        
        return months

    # Retrieve all users.
    def retrieve_students(self):
        collection = self.db["students"]
        requests = []
        for request in collection.find():
            requests.append(request)
        return requests
    
    # Get count of students with a certain field.
    def get_student_field_count(self, field_name):
        collection = self.db["students"]
        return collection.count_documents({ field_name: 1 })
    
    def get_student_completed_count(self):
        collection = self.db["students"]
        return collection.count_documents({
            'career exam': 1,
            'CENEVAL': 1,
            'e sign': 1,
            'education credit': 1,
            'english exam': 1,
            'financial services': 1,
            'graduation request': 1,
            'library': 1,
            'photography': 1,
            'social service': 1,
        })
    
    def get_students_count(self):
        collection = self.db["students"]
        return collection.count_documents({})
    
    # Retrieve a document given intent, entity, status
    def retrieve_answer( self, collection_name, intent, entity, status, channel):
        collection = self.db[collection_name]
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

    # Retrieve entity's document (Watson's entity)
    def retrieve_event( self, eventId ):
        print(eventId)
        collection = self.db["events"]
        result = collection.find_one({"id":eventId})
        print("event is",result)
        return result
    
    # Retrieve event's document
    def retrieve_requirement( self, entity ):
        collection = self.db["requirements"]
        if entity == None:
            return "error on retrieveRequirement"
        else:
            result = collection.find_one({"id":entity})
        return result

    # Retrieve student'completed activities
    def retrieve_completed_activities( self, student_mail, entity ):
        collection = self.db["students"]
        if entity == None:
            result = collection.find_one({"mail":student_mail}, {"_id":0,"name":0,"mail":0,"campus":0,"student_number":0})
        else:
            result = collection.find_one({"mail":student_mail}, {entity:1})
        return result

    # Retrieve student's data
    def retrieve_student_info( self, student_mail ):
        collection = self.db["students"]
        result = collection.find_one({"mail":student_mail}, {"_id":0,"name":1,"mail":1,"campus":1,"student_number":1})
        return result

    # Retrieve details of each activity given a user
    def retrieve_activities_data( self, student_data, completeness ):
        collection = self.db["requirements"]
        activities = []
        for key, value in student_data.items():
            if value == completeness:
                activities.append(collection.find_one({"id":key}))
        return activities

    def get_entity_amount(self, entity):
        collection = self.db["requests"]
        requests = collection.find({"entity-value":entity}).count()
        return requests

    
mongoController.INSTANCE = mongoController()