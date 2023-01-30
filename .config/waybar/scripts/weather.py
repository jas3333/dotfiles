import requests
import os

weather_icons = {
    '200': '🌩',
    '201': '⛈',
    '202': '⛈',
    '210': '🌩',
    '211': '🌩',
    '212': '🌩',
    '221': '🌩',
    '230': '🌩',
    '232': '⛈',  
    '300': '🌧',
    '301': '🌧',
    '302': '🌧',
    '310': '🌨',
    '311': '🌨',
    '312': '🌨',
    '313': '🌨',
    '314': '🌨',
    '321': '🌧', 
    '500': '🌧',
    '501': '🌧',
    '502': '🌧',
    '503': '🌧',
    '504': '🌧',
    '511': '🌧',
    '520': '🌧',
    '521': '🌧',
    '522': '🌧',
    '531': '🌧', 
    '600': '❄️',
    '601': '❄️',
    '602': '❄️',
    '611': '❄️',
    '612': '❄️',
    '613': '❄️',
    '615': '❄️',
    '616': '❄️',
    '620': '❄️',
    '621': '❄️',
    '622': '❄️',  
    '701': '🌫',
    '711': '🌫',
    '721': '🌫',
    '731': '🌫',
    '741': '🌫',
    '751': '🌫',
    '761': '🌫',
    '762': '🌫',
    '771': '🌫',
    '781': '🌫', 
    '800': '🌞', 
    '801': '⛅️',
    '802': '⛅️',
    '803': '⛅️',
    '804': '☁️',
}

API_KEY = os.environ.get('OPEN_WEATHER_KEY')
LAT = os.environ.get('LAT') 
LON = os.environ.get('LON')
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&units=imperial&appid={API_KEY}"

response = requests.get(URL)
data = response.json()

icon_id = str(data['weather'][0]['id'])
current_icon = weather_icons[icon_id]
weather_desc = data['weather'][0]['main']
temp = int(data['main']['temp'])
output = f"{current_icon} {weather_desc} {temp}F"

print(output)








