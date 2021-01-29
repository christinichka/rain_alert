import requests

api_key = "a39893191f4756f82bc93259ed3d484a"

# Parameters for the weather data
parameters = {
	"lat": 34.052235,
	"lon": -118.243683,
	"appid": api_key,
	"exclude": "current,minutely,daily"
}

# Makes request to One Call API
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=38.537201&lon=-90.313217&appid=a39893191f4756f82bc93259ed3d484a", params=parameters)
# If there is a problem and we don't get the correct code an exception will be made.
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
	condition_code = hour_data["weather"][0]["id"]
	if int(condition_code) < 700:
		will_rain = True

if will_rain:		
	print("Bring an umbrella.")

# print(weather_data["hourly"][0]["weather"][0]["id"])

#5 Copy-paste the response to an online JSON viewer (e.g. jsonviewer.stack.hu).





