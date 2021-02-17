from datetime import datetime

import os
import requests

NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_APP_KEY = os.environ["NUTRITIONIX_APP_KEY"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
PROJECT_NAME = os.environ["PROJECT_NAME"]
SHEET_NAME = os.environ["SHEET_NAME"]
SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
USER_ID = os.environ["USER_ID"]
USERNAME = os.environ["USERNAME"]

nutritionix = requests.post(url=NUTRITIONIX_ENDPOINT, json={
    "query": input("Tell me what exercises you did: "),
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 30
}, headers={
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
})

workouts = [{
    "calories": workout["nf_calories"],
    "duration": workout["duration_min"],
    "exercise": workout["name"].title()
} for workout in nutritionix.json()["exercises"]]

for workout in workouts:
    sheety = requests.post(url=f"{SHEETY_ENDPOINT}/{USER_ID}/{PROJECT_NAME}/{SHEET_NAME}", json={
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": workout["exercise"],
            "duration": workout["duration"],
            "calories": workout["calories"]
        }
    }, headers={
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    })
    print(sheety.text)
