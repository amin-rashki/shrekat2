from django.urls import path
from . import views

urlpatterns = [
    path('farm/', views.farm)
]
