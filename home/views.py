import email
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse
#from Portfolio.home.models import Contact
from home.models import Contact

# Create your views here.

def home(request):
    #return HttpResponse("<html> <head>This is my homepage (/)</head></html>")
    context = {'name': "Shruti", 'Course': "Django"}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("This is my about (/about)")
    context = {'name': "Shruti", 'Course': "Django"}
    return render(request, 'about.html', context)

def projects(request):
    #return HttpResponse("This is my projects (/projects)")
    return render(request, 'projects.html')

def contact(request):
    if request.method =="POST":
        print("This is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written to db")
        

    #return HttpResponse("This is my contact (/contact)")
    return render(request, 'contact.html')