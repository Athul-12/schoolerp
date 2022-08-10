from django.urls import path
from . import views

urlpattern=[
    path('login',views.student_login),
    path('marks',views.student_marks),
    path('att',views.student_att)
]