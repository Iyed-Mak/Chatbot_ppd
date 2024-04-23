from django.urls import path
from . import views

urlpatterns = [
  path('home',views.index,name="indexPage"),
  path('contact',views.contact,name="contactPage"),
  path('signup',views.sign,name="signPage"),
  path('email',views.emails,name="emailPage"),

]