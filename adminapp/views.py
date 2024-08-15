from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib import messages
from adminapp.models import FeedbackModel,UserModel,FiledataModel
from django.core.paginator import Paginator
from django.core.mail import EmailMultiAlternatives
from depression_chatbot.settings import DEFAULT_FROM_EMAIL
import pandas as pd
from textblob import TextBlob
import os
# Create your views here.

def admin_login(request):
    if request.method == "POST":
        user = request.POST.get('name')
        password = request.POST.get('password')

        if user == "admin" and password == "admin":
            messages.success(request,"Successfully logged In")
            return redirect('admin_dashboard')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('home_admin') 
    
    return render(request,'admin/home-admin.html')

def admin_logout(request):
    messages.success(request,"successfully logged out")
    return redirect('home')

def admin_index(request):
    register_count = UserModel.objects.all().count()
    approved_count = UserModel.objects.filter(status='Accept').count()
    return render(request,'admin/admin-index.html',{'rc':register_count,'ac':approved_count})

def pending_users(request):
    pending = UserModel.objects.filter(status='pending').order_by('-user_id')
    paginator = Paginator(pending,3)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,'admin/pending-users.html',{'p':page})

def accept_user(request,id):
    user = UserModel.objects.get(pk=id)
    user.status = 'Accept'
    user.save(update_fields=['status'])
    user.save()

    mail = user.user_email
    html_content = f" Hello Mr/Miss.{user.user_name} thank you for showing interest in joining with us.....<br/><b>Your Login credentails</b>  <p> Name : <strong>{user.user_email}  </strong> <br/> password: <strong>{user.user_password}</strong><br/> "
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [mail]
    print(to_mail,from_mail)

    try:
        print('try')
        msg = EmailMultiAlternatives("Authentication ", html_content, from_mail, to_mail)
        a = msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, 'Email has been sent successfully')
        return redirect('pending_users')
        
    except:
        print('except')
        messages.info(request,"Unsuccessfull")
        return redirect('pending_users')

def all_users(request):
    all = UserModel.objects.filter(status='Accept').order_by("-user_id")
    paginator = Paginator(all,3)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,'admin/all-users.html',{'p':page})

def delete_user(request,id):
    dd = UserModel.objects.get(pk=id)
    dd.delete()
    messages.success(request,'Deleted Successfully')
    return redirect('all_users')

def upload_data(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        data = FiledataModel.objects.create(data_file=excel_file)
        file_path = 'media/'+ str(data.data_file)
        df = pd.read_csv(file_path, delimiter = '|',on_bad_lines='skip',names=['A','B','C','D','E','F','G','H','I','J'],usecols = [1,4,5])
        products_list = df.values.tolist()
        print(products_list)
        gh = []
        count = 0
        dp_count = 0
        udp_count = 0
        for i in products_list:
            tweet = {} 
            tweet["date"] = i[0]
            tweet["name"] = i[1]
            tweet["tweet"] = i[2]

            count+=1
            analysis = TextBlob(str(i))
            a = analysis.sentiment
            sentiment = ''
            print(analysis.polarity)
            if analysis.polarity > 0:
                sentiment = 'Depressed'
                print(sentiment,'hello')
                dp_count += 1
            else:
                analysis.polarity <= 0
                sentiment = 'Undepressed'
                print(sentiment,'hy')
                udp_count +=1
            tweet["sentiment"] = sentiment
            gh.append(tweet)
       
        dep = dp_count
        undep = udp_count
        FiledataModel.objects.create(Undepressed=undep,depressed=dep)
        return render(request,"admin/data_graph.html",{
            'dp':dp_count,
            'udp':udp_count,
            'i': gh,  
        })
    return render(request,'admin/upload-data.html')

    
def user_feedback(request):

    analysis = FeedbackModel.objects.all().order_by('-pk')
    paginator = Paginator(analysis,10)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,'admin/user-feedback.html',{'a':page})

def admin_graph(request): 
    positive = FeedbackModel.objects.filter(sentiment="Positive").count()
    negative = FeedbackModel.objects.filter(sentiment="Negitive").count()
    neutral = FeedbackModel.objects.filter(sentiment="Neutral").count()
    Vnegative = FeedbackModel.objects.filter(sentiment="Very Negitive").count()
    Vpositive = FeedbackModel.objects.filter(sentiment="Very Positive").count()
    return render(request,'admin/admin-graph.html',{'positive':positive,'negative':negative,'neutral':neutral,'Vnegative':Vnegative,'Vpositive':Vpositive})

def excel_graph(request,dp,udp):

    return render(request,'admin/exceldata.html',{'dp':dp,'udp':udp})


def excel_data_analysis(request):
    
    return render(request,"admin/data-analysis.html")
