from django.urls import path
from . import views
urlpatterns = [
   path('buyCar/<int:id>/',views.buy_car,name='buy_car'),
]