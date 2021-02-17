import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7a0228184b86434a89d81b30cace3475/flightDeals/prices"
SHEETY_PRICES_TOKEN = "SHEETY_PRICES_TOKEN"
SHEET_USERS_ENDPOINT = "https://api.sheety.co/7a0228184b86434a89d81b30cace3475/flightDeals/users"
SHEETY_USERS_TOKEN = "SHEETY_USERS_TOKEN"


class DataManager:
    def __init__(self):
        self.customer_data = {}
        self.destination_data = {}

    def get_customer_emails(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_USERS_TOKEN}"
        }
        response = requests.get(url=SHEET_USERS_ENDPOINT, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_PRICES_TOKEN}"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            newdata = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            headers = {
                "Authorization": f"Bearer {SHEETY_PRICES_TOKEN}"
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=newdata,
                headers=headers
            )
            print(response.text)
