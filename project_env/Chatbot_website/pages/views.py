from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'Contact/Contact.html')   

def emails(request):
    return render(request,'Emails/Emails.html') 

def sign(request):
    return render(request,'Signup/Signup.html')
