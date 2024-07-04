from django.urls import path
from . import views
urlpatterns = [
    
   path('add_brand/',views.Add_brand.as_view(),name='add_brand'),
    
]