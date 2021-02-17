import datetime
import requests
import time

MY_LAT = -22.823450
MY_LNG = -43.058868


def issposition():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    position = response.json()["iss_position"]
    latitude = float(position["latitude"])
    longitude = float(position["longitude"])
    return {
        "lat": latitude,
        "lng": longitude
    }


def sunrisesunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return {
        "rise": sunrise,
        "set": sunset
    }


def isnight():
    now = datetime.datetime.now()
    sun = sunrisesunset()
    return now.hour <= sun["rise"] or now.hour >= sun["set"]


def isissoverhead():
    iss = issposition()
    hasequallat = MY_LAT - 5 <= iss["lat"] <= MY_LAT + 5
    hasequallng = MY_LNG - 5 <= iss["lng"] <= MY_LNG + 5
    return hasequallat and hasequallng


while True:
    if isissoverhead() and isnight():
        print("Look up! The ISS is above you in the sky!")
    else:
        print("Not yet.")
    print("Waiting 1 minute...")
    time.sleep(60)
