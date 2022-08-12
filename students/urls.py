from django.urls import path
from . import views

urlpatterns=[
    path('login',views.student_login),
    path('marks',views.student_marks),
    path('att',views.student_att)
]