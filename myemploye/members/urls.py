from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='members-home'),
    path('about/', views.about, name='members-about'),
]