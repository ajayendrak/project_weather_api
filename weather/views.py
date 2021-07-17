from django.shortcuts import render
import requests


# Create your views here.

def weather2(request):
    
    if request.method=='POST':

        url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=ce52d96e2b3404b6ae74e544fb6d198d'
        
        search=request.POST.get('search')
        city=search.capitalize()
        

        r=requests.get(url.format(city)).json()
        
        if r['cod'] == 200:

            city_weather={
                'city': city,
                'temperature': int((r['main']['temp'])-273.15),
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'humidity': r['main']['humidity'], 
            }
            context = {'city_weather' : city_weather}
            return render(request, 'weather2.html', context)
        else:
            city_weather={
                'message': 'Please enter valid city name',
            }
            context = {'city_weather' : city_weather}
            return render(request, 'weather2.html', context)

        
    
    return render(request, 'weather2.html')





# {"coord":{"lon":73.8553,"lat":18.5196},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":299.28,"feels_like":299.28,"temp_min":299.28,"temp_max":299.28,"pressure":1005,"humidity":71,"sea_level":1005,"grnd_level":944},"visibility":10000,"wind":{"speed":3.68,"deg":284,"gust":4.43},"clouds":{"all":96},"dt":1625901320,"sys":{"country":"IN","sunrise":1625877265,"sunset":1625924701},"timezone":19800,"id":1259229,"name":"Pune","cod":200}[10/Jul/2021 12:48:19] "GET /weather HTTP/1.1" 200 1808