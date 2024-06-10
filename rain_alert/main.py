import requests

api_key = "333f079013642e73777f4188d2334ebd"
latitude = 41.021647
longitude = 29.014418

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_cond = response.json()
print(weather_cond)

for hour in weather_cond["list"]:
    condition = hour["weather"][0]["id"]
    if int(condition) < 700:
        print("Bring an umbrella.")
