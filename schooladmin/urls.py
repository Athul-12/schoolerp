from django.urls import path
from . import views

urlpatterns=[
    path('login',views.sc_adminlogin),
    path('student',views.sc_adminstudent),
    path('teachers',views.sc_adminteachers)
]