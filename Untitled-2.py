import requests

city_name= 'Tanuku'
API_Key = 'f31c20f7c993602b222e4f85539dd7f9'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'
response =requests.get(url)
if response.status_code == 200:
  data=response.json()
  print( 'Weather is', data['weather'][0]['description'])
  print('Current Temerature is',data['main']['temp'])
  print('Current Temepature Feels like is',data['main']['feels_like'])
  print('Current Temperature feels like is',data['main']['humidity'])