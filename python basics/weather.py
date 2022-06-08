import requests

api_key = "4713c3e0d4156dcdd4b0dbcf10e6e499"
city = "Orlando"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("todays forcast is", description)
temp_min = json.get("main").get("temp_min")
print("the min temperature is", temp_min)

temp_max = json.get("main").get("temp_max")
print("the max temperature is", temp_max)