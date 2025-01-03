from datetime import datetime
import requests

def get_temperature(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m" \
                  f"&temperature_unit=celsius"
    now = datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    return temp