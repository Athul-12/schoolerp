from django.shortcuts import render

# Create your views here.
def student_login(request):
    return render(request,'hom/login.html')

def student_marks(request):
    return render(request,'hom/viewmarks.html')

def student_att(request):
    return render(request,'hom/view_attendence.html')
