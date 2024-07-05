from django.urls import path
from . import views
urlpatterns = [
    
path('signin/',views.Register,name='signin'),
path('profile/',views.Profile,name='profile'),
path('edit/profile/<int:id>/',views.EditProfileView.as_view(),name='edit_profile'),
path('login/',views.user_login.as_view(),name='login'),
path('logout/',views.user_logout,name='logout'),

    
]