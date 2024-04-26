import nltk
import datetime
import random
from nltk.chat.util import reflections,Chat
import google.generativeai as genai
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the scopes for accessing Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials
def create_email(sender,to,subject,message_text):
    message=MIMEMultipart()
    message['to']=to
    message['sender']=sender
    message['subject']=subject
    msg=MIMEText(message_text)
    message.attach(msg)
    raw_message = {
        'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()
    }
    return raw_message


def send_message(service, user_id, message):
    """Send an email message."""
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message sent successfully!')
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
def read_email(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        print('Messages:')
        for message in messages:
            # Get the ID of each message
            message_id = message['id']
            # Retrieve the details of the message
            message_details = service.users().messages().get(userId='me', id=message_id).execute()
            # Extract basic information about the message
            sender = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'From')
            subject = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Subject')
            date = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Date')
            snippet=message_details.get('snippet','no snippet')
            # Print the information
            print(f'Sender: {sender}')
            print(f'Subject: {subject}')
            print(f'Date: {date}')
            print(f'snippet:{snippet}')
            print('---')




SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials




genai.configure(api_key="AIzaSyCFnNB6dqWfufLNPAZEXn5TJtuTOtF-AFI")    # Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
     }

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])




patterns = [
    (r'hi|hello|hey there', ['Hello!', 'Hey!', 'Hi there!']),
    (r'how are you?', ['I am fine, thank you.', 'I\'m doing well, thanks.']),
    (r'what is your name?', ['My name is ChatBot.', 'You can call me ChatBot.']),
    
]





tasks = {
    'give me the time': 'okay',
    'display me emails':'okay',
    'read me emails':'okay',
    'read emails':'okay',
    'show emails':'okay',
    'answer this email':'pkay'
    
    
    
}

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")


class MyChatBot(Chat):
    def respond(self, input_message):
        for pattern, responses in self._pairs:
            match = nltk.re.match(pattern, input_message.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response
        convo.send_message(input_message)
        return convo.last.text
    def task_response(self, task):
        if task in tasks:
            return tasks[task]
        else:
            convo.send_message(task)
            return convo.last.text

    def perform_task(self, task,service):
        if task == 'time':
            return get_time()
        if (task=='display me emails'or task=='read emails' or task=='read me emails' or task=='show me emails') :
            read_email(service)
        # if task=='send an email':
        #     send_message(service,user_id=000,message='hzbad')

        # Add more tasks and their corresponding functions here
 
def main():

    credentials = authenticate()
    # Build the Gmail service
    service = build('gmail', 'v1', credentials=credentials)
    # Authenticate with the Gmail API
   

    chatbot = MyChatBot(patterns)
    print("ChatBot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        elif user_input.lower() in tasks:
            print("ChatBot:", chatbot.task_response(user_input.lower()))
            print("ChatBot:", chatbot.perform_task(user_input.lower(),service))
        else:
            print("ChatBot:", chatbot.respond(user_input))
    print("wahtever else you want me to help you on?\n")
if __name__ == "__main__":
    main()
 

