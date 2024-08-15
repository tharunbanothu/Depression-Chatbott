from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_userlogin',views.home_userlogin,name='home_userlogin'),
    path('home_user_register',views.home_user_register,name='home_user_register'),
    path('',views.user_index,name='user_index'),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('user_myprofile',views.user_myprofile,name='user_myprofile'),
    path('feedback',views.feedback,name='feedback'),
    path('logout_user',views.logout_user,name="logout_user"),
]