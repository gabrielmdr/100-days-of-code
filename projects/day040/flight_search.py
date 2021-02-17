from flight_data import FlightData
from urllib.parse import urlencode

import datetime
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "TEQUILA_API_KEY"


def get_destination_code(city_name):
    json = {
        "apikey": TEQUILA_API_KEY,
        "term": city_name
    }
    tequila = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query?{urlencode(json)}")
    tequila.raise_for_status()
    code = tequila.json()["locations"][0]["code"]
    return code


def search(city_names: str) -> [FlightData]:
    flights = check_flights(city_names, 0)
    cities = city_names.split(",")
    if len(flights) < len(cities):
        for flight in flights:
            if flight.arrival_city_code in cities:
                cities.remove(flight.arrival_city_code)
        missing = ",".join(cities)
        missing_flights = check_flights(missing, 1)
        flights += missing_flights
    return flights


def check_flights(fly_to, max_stopovers) -> [FlightData]:
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    within_six_months = tomorrow + datetime.timedelta(days=180)

    json = {
        "apikey": TEQUILA_API_KEY,
        "fly_from": "LON",
        "fly_to": fly_to,
        "date_from": tomorrow.strftime("%d/%m/%Y"),
        "date_to": within_six_months.strftime("%d/%m/%Y"),
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "curr": "GBP",
        "max_stopovers": max_stopovers
    }

    tequila = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search?{urlencode(json)}")
    tequila.raise_for_status()

    flights = []

    for flight_data in tequila.json()["data"]:
        flight = FlightData(
            arrival_airport_city=flight_data["cityTo"],
            arrival_airport_code=flight_data["flyTo"],
            arrival_city_code=flight_data["cityCodeTo"],
            departure_airport_city=flight_data["cityFrom"],
            departure_airport_code=flight_data["flyFrom"],
            inbound_date=flight_data["route"][(max_stopovers + 1) * 0]["utc_departure"].split("T")[0],
            outbound_date=flight_data["route"][(max_stopovers + 1) * 1]["utc_departure"].split("T")[0],
            price=flight_data["price"],
            stopovers=max_stopovers,
            via_city=flight_data["route"][0]["cityTo"]
        )
        flights.append(flight)

    return flights
