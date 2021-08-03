from django.db import models
from django.utils import timezone

# Create your models here.
class Competition(models.Model):
	app_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	plan = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Season(models.Model):
	app_id = models.IntegerField(unique=True)
	startDate = models.DateField(blank=True, null=True)
	endDate = models.DateField(blank=True, null=True)
	currentMatchday = models.IntegerField()
	winner = models.IntegerField(blank=True, null=True)

class Team(models.Model):
	app_id = models.IntegerField(unique=True)
	name = models.CharField(max_length=100, null=True)
	shortName = models.CharField(max_length=100, null=True)
	tla = models.CharField(max_length=100, null=True)
	crestUrl = models.CharField(max_length=100, null=True)
	address = models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=100, null=True)
	website = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100, null=True)
	founded = models.IntegerField(null=True)
	clubColors = models.CharField(max_length=100, null=True)
	venue = models.CharField(max_length=100, null=True)
	lastUpdated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Match(models.Model):
	app_id = models.IntegerField(unique=True)
	season = models.ForeignKey(Season, to_field='app_id', on_delete=models.CASCADE)
	utcDate = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=100, null=True)
	matchday = models.IntegerField()
	stage = models.CharField(max_length=100, null=True)
	group = models.CharField(max_length=100, null=True)
	lastUpdated = models.DateTimeField(default=timezone.now)
	score_winner = models.CharField(max_length=100, null=True)
	score_duration = models.CharField(max_length=100, null=True)
	score_fullTime_homeTeam = models.IntegerField(null=True)
	score_fullTime_awayTeam = models.IntegerField(null=True)
	score_halfTime_homeTeam = models.IntegerField(null=True)
	score_halfTime_awayTeam = models.IntegerField(null=True)
	score_extraTime_homeTeam = models.IntegerField(null=True)
	score_extraTime_awayTeam = models.IntegerField(null=True)
	score_penalties_homeTeam = models.IntegerField(null=True)
	score_penalties_awayTeam = models.IntegerField(null=True)
	homeTeam = models.ForeignKey(Team, to_field='app_id', on_delete=models.CASCADE, related_name='homeTeam')
	awayTeam = models.ForeignKey(Team, to_field='app_id', on_delete=models.CASCADE, related_name='awayTeam')

	def __str__(self):
		return "Gameweek " + str(self.matchday) + ": " + self.homeTeam.name + " - " + self.awayTeam.name


class Standing(models.Model):
	position = models.IntegerField(null=True)
	team = models.ForeignKey(Team, to_field='app_id', on_delete=models.CASCADE, related_name='team')
	playedGames = models.IntegerField(null=True)
	form = models.CharField(max_length=100, null=True)
	won = models.IntegerField(null=True)
	draw = models.IntegerField(null=True)
	lost = models.IntegerField(null=True)
	points = models.IntegerField(null=True)
	goalsFor = models.IntegerField(null=True)
	goalsAgainst = models.IntegerField(null=True)
	goalDifference = models.IntegerField(null=True)

	def __str__(self):
		return self.team.name

class Predictions(models.Model):
	# app_id = models.IntegerField(unique=True)
	awayWinPercent = models.FloatField(null=True)
	drawPercent = models.FloatField(null=True)
	homeWinPercent = models.FloatField(null=True)
	predictedResult = models.CharField(max_length=100, null=True)
	home = models.CharField(max_length=100, null=True)
	away = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.predictedResult
