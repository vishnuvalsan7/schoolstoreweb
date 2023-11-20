from django.contrib import admin

# Register your models here.
from .models import place, Team, Front

admin.site.register(place)
admin.site.register(Team)
admin.site.register(Front)
