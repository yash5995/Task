from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from datetime import datetime

username =''
created_at =''
def index(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'sign_up.html')
def register(request):
    customer = User()
    if request.method == 'POST':
        customer.first_name = request.POST.get('fname')
        customer.last_name = request.POST.get('lname')
        customer.email = request.POST.get('email')
        customer.username = request.POST.get('Name')
        customer.password = request.POST.get('Password')
        customer.save()
        return redirect('index')
def check_user(request):
    global username
    customer = User()
    if request.method == 'POST':
        username = request.POST.get('Name')
        password = request.POST.get('Password')
        user = User.objects.filter(username=username,password=password)
        if user:
            return render(request,'post_page.html',{'username':username})
        else:
            return redirect('index')
def post_get(request):
    global username,created_at
    post = Post()
    print(post.pk)
    if request.method == 'POST':
        post.text = request.POST.get('text')
        post.created_at = datetime.now()
        post.updated_at = datetime.now()

        created_at = post.created_at
        updated_at = post.updated_at
        text = post.text
        updated_post0(request,text,updated_at,created_at)
        return render(request,'post_page1.html',{'created_at':created_at,'updated_at':updated_at,'text':text,'username':username})

def updated_post0(request,text,updated_at,created_at):
    global username
    user = User.objects.filter(username = username)
    post,created = Post.objects.get_or_create(user=user[0],text=text,created_at=created_at,updated_at=updated_at)
    post.save()
    return render(request,'post_page1.html',{'created_at':created_at,'updated_at':updated_at,'text':text,'username':username})
def updated_post(request):
    global username,created_at
    post = Post()
    if request.method == 'POST':
        post.text = request.POST.get('text')
        post.updated_at = datetime.now()
        text = request.POST.get('text')
        updated_at = datetime.now()
        updated_post1(request,text,updated_at)
        return render(request, 'post_page1.html',
                      {'created_at': created_at, 'updated_at': updated_at, 'text': text, 'username': username})
def updated_post1(request,text,updated_at):
    global username,created_at
    user = User.objects.filter(username = username)
    post,created = Post.objects.get_or_create(user=user[0],text=text,created_at=created_at,updated_at=updated_at)
    post.save()
    return render(request,'post_page1.html',{'created_at':created_at,'updated_at':updated_at,'text':text,'username':username})
