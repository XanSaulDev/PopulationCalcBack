from django.urls import path
from .views import CalculatePopulation

urlpatterns = [
    path('calculate-population', CalculatePopulation.as_view())
]