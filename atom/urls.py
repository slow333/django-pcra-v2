from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pcra-home'),
    path('about/', views.about, name='pcra-about'),
]
