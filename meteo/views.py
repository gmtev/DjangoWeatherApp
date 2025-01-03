from django.views import View
from django.http import HttpResponse, request
from django.template import loader
import geocoder

from meteo.models import WorldCities
from meteo.utils import get_temperature


class TemperatureCurrentPlaceView(View):

    def get(self, request):
        location = geocoder.ip('me').latlng
        temp = get_temperature(location)
        template = loader.get_template('your-place.html')
        context = {'temp': temp}
        return HttpResponse(template.render(context, request))


class TemperatureRandomPlaceView(View):

    def get(self, request):
        random_item = WorldCities.objects.all().order_by('?').first()
        city = random_item.city
        location = [random_item.lat, random_item.lng]
        temp = get_temperature(location)
        template = loader.get_template("random-place.html")
        context = {
            'city': city,
            'temp': temp
        }
        return HttpResponse(template.render(context, request))