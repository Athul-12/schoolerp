from django.shortcuts import render

# Create your views here.
def sc_adminlogin(request):
    return render(request,'home/login.html')
def sc_adminstudent(request):
    return render(request,'home/viewstudents.html')
def sc_adminteachers(request):
    return render(request,'home/viewteachers.html')