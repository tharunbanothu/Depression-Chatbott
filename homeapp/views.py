from django.shortcuts import render
from adminapp.models import UserModel


# Create your views here.

def home(request):
          reg_count = UserModel.objects.all().count()
          user_count = UserModel.objects.filter(status='accept').count()
          return render(request,'home/home-index.html',{'r':reg_count,'u':user_count})

def home_about(request):
          return render(request,'home/about.html')

def home_contact(request):
          return render(request,'home/contact.html')
