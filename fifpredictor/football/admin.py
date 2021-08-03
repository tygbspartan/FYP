from django.contrib import admin
from football.models import Competition, Season, Team, Match, Standing

# Register your models here.
admin.site.register(Competition)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Standing)