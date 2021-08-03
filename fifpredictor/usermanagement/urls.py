from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='user-login'),
    path('register/', views.registerPage, name='user-register'),
    
    path('logout/', views.logoutUser, name='user-logout'),
    path('profile/', views.displayProfile, name='user-profile'),
    path('editprofile/', views.updateProfile, name='edit-profile'),
]