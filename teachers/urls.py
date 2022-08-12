from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.techer_login),
    path('att/',views.attendece),
    path('marks/',views.marks),
    path('student/',views.student)
]