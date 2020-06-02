from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='dresses_home'),
    path('<int:id>', views.detail, name='dress_detail')
]