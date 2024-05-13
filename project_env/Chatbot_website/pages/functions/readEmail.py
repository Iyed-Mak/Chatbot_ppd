from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.utils import parsedate_to_datetime
from email import message_from_bytes
from base64 import urlsafe_b64decode

import pickle
import os.path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes for accessing Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
def authenticate():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    token_file = 'token.pickle'
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:\\Users\\DELL\\Music\\ppd\\Chatbot_Univ\\project_env\\Chatbot_website\\pages\\functions\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return creds


# def read_email(service):
#     results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
#     messages = results.get('messages', [])

#     if not messages:
#         print('No messages found.')
#     else:
#         # Get the ID of each message
#         message_id = messages[0]['id']
#         # Retrieve the details of the message
#         message_details = service.users().messages().get(userId='me', id=message_id).execute()
#         # Extract basic information about the message
#         sender = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'From')
#         subject = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Subject')
#         date = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Date')
#         snippet=message_details.get('snippet','no snippet')
#         # Print the information
#         info = []
#         info.append(sender)
#         info.append(subject)
#         info.append(date)
#         info.append(snippet)
#         return info    


def read_email(service):
    try:
        last_message_id = None        
        # List messages from the inbox, but only retrieve one message
        results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])

        if messages != last_message_id:
            message_id = messages[0]['id']
            message_details = service.users().messages().get(userId='me', id=message_id).execute()
            
            sender = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'From')
            subject = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Subject')
            date = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Date')

            # Parse the original date string
            date_tuple = parsedate_to_datetime(date)
            if date_tuple is not None:
                date = date_tuple.strftime('%Y-%m-%d %H:%M:%S')

            body = ""
            if 'parts' in message_details['payload']:
                for part in message_details['payload']['parts']:
                    if part['mimeType'] == 'text/plain':
                        body_data = part['body']['data']
                        body_data_decoded = urlsafe_b64decode(body_data.encode()).decode()
                        body += body_data_decoded
            else:
                body_data = message_details['payload']['body']['data']
                body_data_decoded = urlsafe_b64decode(body_data.encode()).decode()
                body += body_data_decoded
            prompt = 'In order to assist you, I d like you to extract tasks along with their associated dates from a given message. Your task is to generate a Python dictionary where each task is mapped to their respective dates,you will provide the dates in the following format:YYYY/MM/DD HH/MM/SS. If no tasks are found in the message, the output should be an empty list. Dates can be mentioned in various formats such as "next week," "Sunday," "tomorrow," or specific date and time formats like "2024/5/01, 18:00".  message:'    
            body = prompt + body     
            info = [sender,subject,date,body]
            return info
    except Exception as e:
        print(f'An error occurred: {e}')

credentials = authenticate()
def getInfo():
  service = build('gmail','v1',credentials=credentials)
  info = read_email(service)
  return info


# print(getInfo()[3])