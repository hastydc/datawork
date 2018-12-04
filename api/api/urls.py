from django.contrib import admin
from django.urls import path
from quickstart import views

urlpatterns = [
    #path('index/', views.index, name='login'),
		path('', views.login, name='login'),
		path('login/', views.login, name='login'),
		path('home-company/', views.homeCompany, name='homeCompany'),
		path('home-person/', views.homePerson, name='homePerson'),
		path('result-company/', views.resultCompany, name='resultCompany'),
		path('result-person/', views.resultPerson, name='resultPerson'),
]
