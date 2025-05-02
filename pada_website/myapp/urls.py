from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('redirect/', views.redirect_view, name='redirect_view'),
    path('<str:qr_code>/', views.home_view, name='home_view'),
    re_path(r'^(?P<qr_code>[^/]+)/media/(?P<photo_path>.*)$', views.serve_personnalite_photo, name='serve-personnalite-photo'),

    path('<str:qr_code>/submit-suggestion/', views.submit_suggestion, name='submit_suggestion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)