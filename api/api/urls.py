"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quickstart import views

urlpatterns = [
    #path('index/', views.index, name='login'),
		path('', views.index, name='login'),
		path('login/', views.login, name='login'),
		path('home-company/', views.homeCompany, name='homeCompany'),
		path('home-person/', views.homePerson, name='homePerson'),
		path('result-company/', views.resultCompany, name='resultCompany'),
		path('result-person/', views.resultPerson, name='resultPerson'),
]
