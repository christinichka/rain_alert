import requests
from twilio.rest import Client

api_key = "a39893191f4756f82bc93259ed3d484a"
account_sid = "AC47824f371eb909359194db481dddfaff"
auth_token = "cdab63909e19f2bc3743cca0c110c2d5"

# Parameters for the weather data
parameters = {
	"lat": 38.537201,
	"lon": -90.313217,
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
	client = Client(account_sid, auth_token)
	message = client.messages \
		.create(
			body="It's going to rain today. Remember to bring an ☂️",
			from_="+19415640801", #You Twilio number
			to="(314) 827-4781‬", #Your verified number
	)
	print(message.status)


