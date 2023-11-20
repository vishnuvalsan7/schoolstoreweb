from django.urls import path
from travelapp import views

app_name = 'travelapp'
urlpatterns = [
    path('', views.demo, name='demo')
]
