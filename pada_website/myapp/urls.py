from django.urls import path
from . import views

urlpatterns = [
    path('<str:qr_code>/', views.home_view, name='home_view'),
    path('redirect/', views.redirect_view, name='redirect_view'),
]
