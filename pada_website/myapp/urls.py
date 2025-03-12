from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('home/', views.home_view, name='home_view'), 
    # path('map/', views.map_view, name='map'),
    path('redirect/', views.redirect_view, name='redirect_view'),
]
