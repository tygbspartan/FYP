from django.shortcuts import render
from football.models import Competition, Season, Team, Match, Standing
from django.http import HttpResponse, JsonResponse
import requests
import csv
from .models import Predictions
from .models import Team

def importPredictions(request):
	with open('../EPL-predict-2020/dataset/Final-Results/Predicted_Result_With_Fixture_Data.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0] != '':
				_, created = Predictions.objects.get_or_create(
					awayWinPercent = row[8][:4],
					drawPercent = row[9][:4],
					homeWinPercent = row[10][:4],
					predictedResult = row[7],
					home = row[4],
					away = row[5],
					)
		return HttpResponse('Imported matches')

def importTeams(request):
	# Call api
	url = "http://api.football-data.org/v2/competitions/2021/teams"
	payload={}
	headers = {'X-Auth-Token': 'd605b982e75f4f979754e5cc268a48cb'}
	response = requests.request("GET", url, headers=headers, data=payload)

	# Get data
	data = response.json()

	for team in data['teams']:
		oldteam = Team.objects.filter(app_id = team['id']).first()
		if(oldteam):
			oldteam.app_id = team["id"]
			oldteam.name = team["name"]
			oldteam.shortName = team["shortName"]
			oldteam.tla = team["tla"]
			oldteam.crestUrl = team["crestUrl"]
			oldteam.address = team["address"]
			oldteam.phone = team["phone"]
			oldteam.website = team["website"]
			oldteam.email = team["email"]
			oldteam.founded = team["founded"]
			oldteam.clubColors = team["clubColors"]
			oldteam.venue = team["venue"]
			oldteam.lastUpdated = team["lastUpdated"]
			oldteam.save()
		else:
			newteam = Team(
				app_id = team["id"],
				name = team["name"],
				shortName = team["shortName"],
				tla = team["tla"],
				crestUrl = team["crestUrl"],
				address = team["address"],
				phone = team["phone"],
				website = team["website"],
				email = team["email"],
				founded = team["founded"],
				clubColors = team["clubColors"],
				venue = team["venue"],
				lastUpdated = team["lastUpdated"],
			)

			newteam.save()

	return HttpResponse('Imported teams')

def importMatches(request):
	# Call api
	url = "http://api.football-data.org/v2/competitions/2021/matches"
	payload={}
	headers = {'X-Auth-Token': 'd605b982e75f4f979754e5cc268a48cb'}
	response = requests.request("GET", url, headers=headers, data=payload)

	# Get data
	data = response.json()

	for match in data['matches']:
		oldmatch = Match.objects.filter(app_id = match['id']).first()

		season = Season.objects.filter(app_id = match['season']['id']).first()
		homeTeam = Team.objects.filter(app_id = match['homeTeam']['id']).first()
		awayTeam = Team.objects.filter(app_id = match['awayTeam']['id']).first()
		if(oldmatch):
			oldmatch.app_id = match["id"]
			oldmatch.season = season
			oldmatch.utcDate = match['utcDate']
			oldmatch.status = match['status']
			oldmatch.matchday = match['matchday']
			oldmatch.group = match['group']
			oldmatch.lastUpdated = match['lastUpdated']
			oldmatch.score_winner = match['score']['winner']
			oldmatch.score_duration = match['score']['duration']
			oldmatch.score_fullTime_homeTeam = match['score']['fullTime']['homeTeam']
			oldmatch.score_fullTime_awayTeam = match['score']['fullTime']['awayTeam']
			oldmatch.score_halfTime_homeTeam = match['score']['halfTime']['homeTeam']
			oldmatch.score_halfTime_awayTeam = match['score']['halfTime']['awayTeam']
			oldmatch.score_extraTime_homeTeam = match['score']['extraTime']['homeTeam']
			oldmatch.score_extraTime_awayTeam = match['score']['extraTime']['awayTeam']
			oldmatch.score_penalties_homeTeam = match['score']['penalties']['homeTeam']
			oldmatch.score_penalties_awayTeam = match['score']['penalties']['awayTeam']
			oldmatch.homeTeam = homeTeam
			oldmatch.awayTeam = awayTeam
			oldmatch.save()
		else:
			newmatch = Match(
				app_id = match["id"],
				season = season,
				utcDate = match['utcDate'],
				status = match['status'],
				matchday = match['matchday'],
				group = match['group'],
				lastUpdated = match['lastUpdated'],
				score_winner = match['score']['winner'],
				score_duration = match['score']['duration'],
				score_fullTime_homeTeam = match['score']['fullTime']['homeTeam'],
				score_fullTime_awayTeam = match['score']['fullTime']['awayTeam'],
				score_halfTime_homeTeam = match['score']['halfTime']['homeTeam'],
				score_halfTime_awayTeam = match['score']['halfTime']['awayTeam'],
				score_extraTime_homeTeam = match['score']['extraTime']['homeTeam'],
				score_extraTime_awayTeam = match['score']['extraTime']['awayTeam'],
				score_penalties_homeTeam = match['score']['penalties']['homeTeam'],
				score_penalties_awayTeam = match['score']['penalties']['awayTeam'],
				homeTeam = homeTeam,
				awayTeam = awayTeam,
			)

			newmatch.save()

	return HttpResponse('Imported matches')

def importStandings(request):
	# Call api
	url = "http://api.football-data.org/v2/competitions/2021/standings"
	payload={}
	headers = {'X-Auth-Token': 'd605b982e75f4f979754e5cc268a48cb'}
	response = requests.request("GET", url, headers=headers, data=payload)

	# Get data
	data = response.json()

	# Delete old data
	Standing.objects.all().delete()

	# Add new data
	for standing in data['standings'][0]['table']:
		team = Team.objects.filter(app_id = standing['team']['id']).first()

		std = Standing(
			position = standing['position'],
			team = team,
			playedGames = standing['playedGames'],
			form = standing['form'],
			won = standing['won'],
			draw = standing['draw'],
			lost = standing['lost'],
			points = standing['points'],
			goalsFor = standing['goalsFor'],
			goalsAgainst = standing['goalsAgainst'],
			goalDifference = standing['goalDifference']
		)
		std.save()


	return HttpResponse('Imported Standings')
