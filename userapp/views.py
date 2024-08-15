from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from userapp.models import UserModel
from adminapp.models import FeedbackModel
from django.contrib import messages
import random
from django.core.mail import EmailMultiAlternatives
from depression_chatbot.settings import DEFAULT_FROM_EMAIL
from textblob import TextBlob

# Create your views here.

def home_user_register(request):
    
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0987654321"
    symbols = "@#$%^&*"
    all = lower+upper+number+symbols
    length = 8
    password = "".join(random.sample(all,length))
    print(password)     
    if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            city = request.POST.get('city')
            profile = request.FILES['profile']

            UserModel.objects.create(user_name=name,user_email=email,user_password=password,user_phone=contact,
            user_city=city,user_profile=profile)
            
            
            messages.success(request, 'Registered successfully')
            return redirect('home_userlogin')
            

    return render(request,'user/home-user-register.html')

def home_userlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)

        try: 
            check = UserModel.objects.get(user_email = email , user_password = password)
            print(check)
            if check.status == 'Accept':
                request.session["user_id"] = check.user_id
                messages.success(request,"Logged In successfully")
                return redirect('user_index')
            else:
                messages.warning(request,'You have not approved yet')
        
        except:
            print('except')     
            messages.warning(request,"Invalid email and password")
            return redirect('home_userlogin')

    return render(request,'user/home-userlogin.html')

def user_index(request):
    user_id = request.session['user_id']
    a = UserModel.objects.get(user_id = user_id)
    user_count = UserModel.objects.all().count
    approved_count = UserModel.objects.filter(status='Accept').count()
    return render(request,'user/user-index.html',{'a':a,'user_count':user_count,'ac':approved_count})

def chatbot(request):
    user_id = request.session['user_id']
    nav = UserModel.objects.get(user_id=user_id)
    return render(request,'user/chatbot.html',{'a':nav})

def user_myprofile(request):
    user_id = request.session['user_id']
    print(user_id)
    profile = UserModel.objects.get(user_id = user_id)
    print(profile)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        city = request.POST.get('city')

        if not request.FILES.get('profileimage',False):
            profile.user_name = name
            profile.user_email = email
            profile.user_password = password
            profile.user_phone = contact
            profile.user_city = city

        if request.FILES.get('profileimage',False):
            image = request.FILES['profileimage']
            profile.user_name = name
            profile.user_email = email
            profile.user_password = password
            profile.user_phone = contact
            profile.user_city = city
            profile.user_profile = image
        
        profile.save()
        messages.success(request,"Updated Successfully")
        return redirect('user_myprofile')

    return render(request,'user/user-myprofile.html',{'profile':profile})

def feedback(request): 
    user_id = request.session['user_id']
    u = UserModel.objects.get(user_id = user_id)
    all = FeedbackModel.objects.all()
    positive = FeedbackModel.objects.filter(sentiment="Positive").count()
    negative = FeedbackModel.objects.filter(sentiment="Negitive").count()
    neutral = FeedbackModel.objects.filter(sentiment="Neutral").count()
    Vnegative = FeedbackModel.objects.filter(sentiment="Very Negitive").count()
    Vpositive = FeedbackModel.objects.filter(sentiment="Very Positive").count()
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        print(feedback)
        analysis = TextBlob(feedback)
        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral' 

        FeedbackModel.objects.create(feedback=feedback,user=u,sentiment=sentiment)
        messages.success(request,'Feedback submitted successfully')
    return render(request,'user/feedback.html',{'a':all,'u':u,'postivie':positive,'negative':negative,'neutral':neutral,'vpositive':Vpositive,'vnegative':Vnegative})

def logout_user(request):
    messages.success(request,"Logged Out")
    return redirect('home') 