from django.urls import path
from hauptseite import views

urlpatterns = [
    path('', views.show_home, name='home')
]