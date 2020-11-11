import os
from dotenv import load_dotenv

#Twilio
from twilio.rest import Client 

class whatsappController():
    def __init__( self ):
        self.account_sid = os.getenv("account_sid")
        self.auth_token = os.getenv("auth_token")
        self.client = Client(self.account_sid, self.auth_token) 
        return

    def send_message( self, phone, message ):
        message = message.replace("\\n","""
        """)
        self.client.messages.create( 
                                from_= 'whatsapp:+14155238886',  
                                body = message,      
                                to = phone 
                            ) 
        return
    