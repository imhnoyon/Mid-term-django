from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.Home,name='homepages'),
    path('brands/<slug:brand_slug>/',views.Home,name='brandlist'),
    path('addcar/',views.AddCar_model.as_view(),name='Add_car'),
    path('details/<int:id>/',views.CarDetailView.as_view(),name='details'),
   
    
]
