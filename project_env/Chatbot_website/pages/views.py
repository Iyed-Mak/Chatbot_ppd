from django.shortcuts import render
from django.http import JsonResponse
from .functions import geminapi
from . import database
from .database import display_all_data
from .database import addTask
from .database import delete_task_by_id
from .database import display_message
from .functions.test import main
from .functions.readEmail import getInfo

user_input='In order to assist you, I d like you to extract tasks along with their associated dates from a given message. Your task is to generate a Python dictionary where each task is mapped to their respective dates,you will provide the dates in the following format:YYYY/MM/DD HH/MM/SS. If no tasks are found in the message, the output should be an empty list. Dates can be mentioned in various formats such as "next week," "Sunday," "tomorrow," or specific date and time formats like "2024/5/01, 18:00".  message: i am inviting you for the wedding of my sister next saturday and dont forget to attend the tp session next monday at 11,and preparing slides and materials for an upcoming client presentation due on May 15, 2024,dont forget to create a workshop for the next fridaye}'

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'Contact/Contact.html')   

def emails(request):
    return render(request,'Emails/Emails.html') 

def sign(request):
    return render(request,'Signup/Signup.html')

def chat(request):
    if(geminapi.response!=''):
      return render(request,'Chat/chat.html',{'count': 1 , 'response': geminapi.response})
    else:
      return render(request,'Chat/chat.html')
          

def tasks(request):
    dates_tasks = main(getInfo()[3])
    print(dates_tasks)
    if not dates_tasks:
        print("empty tasks")
    else:
        for date_task in dates_tasks:
            date = date_task[0]
            task = date_task[1]
            print(date)
            print(task)
            addTask(getInfo()[0],getInfo()[2], task, date)
    
    return render(request,'Task/task.html',{'rows': display_all_data()})




def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        database.delete_task_by_id(int(task_id))
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

def done_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        database.update_task_status_by_id(int(task_id))
        return JsonResponse({'message': 'Task update successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    
def chatReponse(request):
    if request.method == 'POST':
        input = request.POST.get('input')
        geminapi.response = geminapi.chat(input)
        return JsonResponse({'message': 'input request successfully'})
    else:
        return JsonResponse({'message': 'input request method'})    