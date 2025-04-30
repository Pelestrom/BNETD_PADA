from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    # path('login/', views.login_view, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<str:qr_code>/', views.home_view, name='home_view'),
    path('redirect/', views.redirect_view, name='redirect_view'),
    path('<str:qr_code>/submit-suggestion/', views.submit_suggestion, name='submit_suggestion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)