from django.urls import path
from . import views

urlpatterns = [
    path('', views.for_you_page, name='for_you'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('upload/', views.upload, name='upload'),
]
