"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



genai.configure(api_key="AIzaSyCFnNB6dqWfufLNPAZEXn5TJtuTOtF-AFI")

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials



def read_email(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    
    landmark2 = messages[0].get('snippet', 'snippet not available')
    landmark1="hi hacen i wanted to tell you to attend  the meeting that i have orgonized with the members of my group next tomorow at 11 and dont forget to bring your tools next monday to start the project "
    

    prompt_parts = [
    """you are a helpful assistant your task is to extract tasks from the message
     that have a relation with time and output these tasks in json file each task has 
     his own date as a key  ommit any other content from the response,message:you have to assisst to a meeting  at 11 am next monday to discuss some issues about the project,and dont forget to bring your tools for the event that we have orginezed tommorow """
    ]

    response = model.generate_content(prompt_parts)
    # response_dict = response._result['candidates'][0]
    # # task_dict = response_dict['content']['parts'][0]['text']
    # tasks = json.loads(task_dict)
    print(response)


    # Assuming there's only one candidate, access the first one
    #  response_dict = response._result['candidates'][0]

    # # The tasks are already formatted as a dictionary within 'content']['parts'][0]['text']
    # tasks = response_dict['content']['parts'][0]['text']

    # # No need for json.loads since it's already a dictionary
    

# Set up the model
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
#set a prompt for gemini to extract tasks if there is any
convo = model.start_chat(history=[
])


def chat(input):
  # input = input("Enter message : ")
  response = model.generate_content(input)
  return response.text

response = ''

