import requests
import json

api_key = "c6a426a8dc6caf1e7550cc891aa2e1ec"

url = "http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=c6a426a8dc6caf1e7550cc891aa2e1ec"

def weather(city):
	r = requests.get(url, params=city)
	return json.loads(r.text)

print(weather("nairobi"))