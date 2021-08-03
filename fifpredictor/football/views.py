from django.shortcuts import render
from football.models import Competition, Season, Team, Match, Standing, Predictions
from django.http import HttpResponse, JsonResponse
import requests
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='user-login')
def fixtures(request): 
	fixtures = Match.objects.all()
	paginator = Paginator(fixtures, 10) # Show a match week matches per page.
	page_number = request.GET.get('page')
	matches = paginator.get_page(page_number)
	context = {
		'matches':matches
	}

	return render(request, 'football/fixtures.html', context)

@login_required(login_url='user-login')
def standings(request):
	context = {
		'standings': Standing.objects.all()
	}

	return render(request, 'football/standings.html', context)

@login_required(login_url='user-login')
def predictions(request):
	predictions = Predictions.objects.all()
	paginator = Paginator(predictions, 25) # Show 25predictions per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'football/predictions.html', {'page_obj': page_obj})