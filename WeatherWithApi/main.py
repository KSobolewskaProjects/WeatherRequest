import requests

API_key="426c9813913bc1f705017f61f7ea85d0"
Url_Base ="https://api.openweathermap.org/data/2.5/weather"

city =input("Enter a city name: ")
request_url = f"{Url_Base}?appid={API_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    date = response.json() #json is python dictionary
    weather = date['weather'][0]['description']
    print("Weather: ", weather)
    temperature = round(date['main']['temp']-272.15,1)
    print("Temperature: ", temperature, "celsius")
else:
    print("Request doesn't work")