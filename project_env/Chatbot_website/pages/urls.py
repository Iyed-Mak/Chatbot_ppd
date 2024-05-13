from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name="indexPage"),
  path('contact',views.contact,name="contactPage"),
  path('signup',views.sign,name="signPage"),
  path('email',views.emails,name="emailPage"),
  path('chat',views.chat,name='chatPage'),
  path('tasks',views.tasks,name='tasks'),
  path('delete_task/', views.delete_task, name='delete_task'),
  path('done_task/', views.done_task, name='task_done'),
  path('chatReponse/', views.chatReponse, name='chatResponse'),
]