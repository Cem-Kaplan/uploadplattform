from django.urls import path
from hauptseite import views

urlpatterns = [
    path('', views.show_home, name='home'),
    path('about/', views.show_about, name='about'),
    path('upload/', views.show_upload, name='upload'),
    path('login/', views.show_login, name='login')

]