from django.urls import path
from . import views

# apps/aistore/
urlpatterns = [
    path('', views.home, name='aistore-home'),
]
