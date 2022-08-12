from django.shortcuts import render

# Create your views here.
def techer_login(request):
    return render (request,'home/login.html')

def attendece(request):
    return render (request,'home/addattendence.html')

def marks(request):
    return render (request,'home/addmarks.html')

def student(request):
    return render(request,'home/students.html')