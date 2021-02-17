from twilio.rest import Client

import requests

OWM_API_KEY = "OWM_API_KEY"
MY_LAT = "YOUR LOCATION LATITUDE"
MY_LON = "YOUR LOCATION LONGITUDE"
TWILIO_ACCOUNT_SID = "TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"

willrain = False

parameters = {
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily",
    "lat": MY_LAT,
    "lon": MY_LON
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

hourly: [] = response.json()["hourly"][:12]

for tempdata in hourly:
    if tempdata["weather"][0]["id"] < 700:
        willrain = True

if willrain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella.",
            from_="YOUR TWILIO PHONE NUMBER",
            to="YOUR PHONE NUMBER"
        )

    print(message.status)
