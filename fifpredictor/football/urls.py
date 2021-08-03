from django.urls import path

from . import imports
from . import views

urlpatterns = [
    path('import-teams/', imports.importTeams, name='import-teams'),
    path('import-matches/', imports.importMatches, name='import-matches'),
    path('import-standings/', imports.importStandings, name='import-standings'),
    path('import-predictions/', imports.importPredictions, name='import-predictions'),



    path('', views.fixtures, name='football-fixtures'),
    path('standings/', views.standings, name='football-standings'),
    path('predictions/', views.predictions, name='football-predictions')
]
