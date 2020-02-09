from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.
def req(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=08abdab899d508b6804e6a70f2584d3f&lang=ru'
    city = 'Новосибирск'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    myDate = datetime.now()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    context = {'weather' : weather}


    return render(request, 'weather/index.html', context, {
         'Mydate': myDate
    } ) #returns the index.html template