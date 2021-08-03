from django.shortcuts import render, redirect
# from football.models import Competition, Season, Team, Match, Standing
from django.http import HttpResponse, JsonResponse
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from usermanagement.forms import ProfileUpdateForm

from .models import *
from .forms import CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('football-fixtures')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + ' has been successfully registered!')

                return redirect('user-login')
            

        context = {'form' :form}
        return render(request, 'account/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('football-fixtures')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('football-fixtures')
            else:
                messages.info(request, 'Username or Password is incorrect!!')

        context = {}
        return render(request, 'account/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('user-login')


@login_required(login_url='user-login')
def displayProfile(request):

    

    return render(request, "account/profile.html", {})


def updateProfile(request):
    if request.POST:
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)

        if p_form.is_valid():
            p_form.save()
            # messages.success(request, 'Your account has been updated')
            return redirect('/profile/')
    else:
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        
        'p_form': p_form
    }
    return render(request, "account/editprofile.html", context)