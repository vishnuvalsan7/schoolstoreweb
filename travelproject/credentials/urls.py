from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('sub/',views.sub,name='sub'),
    path('form/', views.form, name='form'),
    path('logout/',views.logout,name='logout'),
    path('order',views.order,name='about'),
    path('returns',views.returns,name='return'),
    path('enquiry',views.enquiry,name='enquiry'),

]
