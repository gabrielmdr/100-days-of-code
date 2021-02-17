from data_manager import DataManager
from flight_data import FlightData
from flight_search import search
from notification_manager import send_emails

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

flights: [FlightData] = search(",".join(destinations.keys()))

for flight in flights:
    if flight.price < destinations[flight.arrival_city_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.departure_airport_city}-{flight.departure_airport_code} to {flight.arrival_airport_city}-{flight.arrival_airport_code}, from {flight.outbound_date} to {flight.inbound_date}."

        if flight.stopovers > 0:
            message += f"\nFlight has {flight.stopovers} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.departure_airport_code}.{flight.arrival_airport_code}.{flight.outbound_date}*{flight.arrival_city_code}.{flight.departure_airport_code}.{flight.inbound_date}"

        send_emails(emails, message, link)
