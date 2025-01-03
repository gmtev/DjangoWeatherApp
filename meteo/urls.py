from django.urls import path
from meteo import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('meteo/', views.TemperatureCurrentPlaceView.as_view(), name='temperature_current_place'),
    path('meteo/random', views.TemperatureRandomPlaceView.as_view(), name='temperature_random_place'),
]


