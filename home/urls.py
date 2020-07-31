from django.urls import path,include
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('handlelogin', views.handlelogin, name='handlelogin'),
    path('handlelogout', views.handlelogout, name='handlelogout')
]

