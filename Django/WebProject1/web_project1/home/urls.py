from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='web_home'),
    path('about/', views.about, name='web_about'),
]