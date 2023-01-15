import requests  # Modulul care preia informatiile de la un API
from twilio.rest import Client  # Modului pentru API Auto SMS sent
import os

api_key = "7421506ef521ff77bf0e29de433ea699"  # Open weather map password
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"  # Open weather map end point
account_sid = "AC07309b3dd56eead2c2b286fa0865eace"  # Twilio user - auto sent message
auth_token = "acf08e07427c983d7c64ec2d833f58e1"  # Twilio password - auto sent message

parameters = {
    "lat": 45.24,
    "lon": 11.08,
    "appid": api_key
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()

data = response.json()
weather_now_code = data["weather"][0]["id"]
weather_now = data["weather"][0]["main"]

if weather_now_code >= 500:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's rainy outside, take an umbrella.",
        from_='+12232178563',
        to='+40728046203'
    )
    print(message.status)
else:
    print(f"Braila Outside weather now : {weather_now}")
