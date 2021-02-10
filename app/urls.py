from django.urls import path
from . import views

urlpatterns = [
    path('', views.BuscaCep.as_view())
]