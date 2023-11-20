from django.shortcuts import render
from .models import place, Team, Front


# Create your views here.

def demo(request):
    obb = place.objects.all()
    tm = Team.objects.all()
    frnt = Front.objects.all()

    return render(request, "index.html", {'obb': obb,'tm':tm,'frnt':frnt})
