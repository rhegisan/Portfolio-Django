from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
   # context= {'name':'Rhegi', 'course':'cs'}
   # return HttpResponse("homepage")
    return render(request,'home.html')
def about(request):
    #return HttpResponse("about")
    return render(request,'about.html',)
def projects(request):
    #return HttpResponse("projects")
    return render(request,'projects.html',)
def contact(request):
    #return HttpResponse("contact")
    if request.method=="POST":
        name= request.POST['name']
        phone= request.POST['phone']
        email= request.POST['email']
        desc= request.POST['desc']
       # print(name, phone, email, desc) 
        contact= Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("data has been written in db")
    return render(request,'contact.html',)