import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import time


# Define the scopes for accessing Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file('C:\\Users\\DELL\\Music\\ppd\\Chatbot_Univ\\project_env\\Chatbot_website\\pages\\functions\\credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def read_email(service):
     try:
        last_message_id = None        
        # List messages from the inbox, but only retrieve one message
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=1).execute()
        messages = results.get('messages', [])

        if messages != last_message_id :
            message_id = messages[0]['id']
            message_details = service.users().messages().get(userId='me', id=message_id).execute()
          
            sender = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'From')
            subject = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Subject')
            date = next(header['value'] for header in message_details['payload']['headers'] if header['name'] == 'Date')

            info = []
            info.append(sender)
            info.append(subject)
            info.append(date)

            payload = message_details['payload']
            # Find the body of the message
            if 'parts' in payload:
                parts = payload['parts']
                for part in parts:
                    if part['mimeType'] == 'text/plain':
                        body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        # body = body.split('message: ')[1]
                        # print(f'Body1: {body}')
                        info.append(body)
                        return info
                        break  # Stop after finding the plain text part

            # If no plain text part is found, try getting the full message body
            if 'body' in payload:
                body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
                info.append(body)
            return info    
        # last_message_id=messages
     except Exception as e:
        print(f'An error occurred: {e}')


""" def poll_emails(service):
    while True:
        read_email(service)
        time.sleep(10)   """


def main():
    # Authenticate with the Gmail API
    credentials = authenticate()

    # Build the Gmail service
    service = build('gmail', 'v1', credentials=credentials)

    """   # Authenticate with the Gmail API
      thread=threading.Thread(target=poll_emails,args=(service,))
      thread.start() """
    return read_email(service)
    
if __name__ == '__main__':
    print(main())
