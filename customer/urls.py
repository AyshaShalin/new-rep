from importlib.resources import path
from django.urls import path
from . import views

urlpatterns=[ 
    path('User login',views.login),
    path('signup',views.signup)
]