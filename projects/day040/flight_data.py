import datetime


class FlightData:
    def __init__(
            self,
            arrival_airport_city,
            arrival_airport_code,
            arrival_city_code,
            departure_airport_city,
            departure_airport_code,
            inbound_date,
            outbound_date,
            price,
            stopovers=0,
            via_city=None
    ):
        if via_city is None:
            via_city = []
        self.arrival_airport_city = arrival_airport_city
        self.arrival_airport_code = arrival_airport_code
        self.arrival_city_code = arrival_city_code
        self.departure_airport_city = departure_airport_city
        self.departure_airport_code = departure_airport_code
        self.inbound_date: datetime.datetime = inbound_date
        self.outbound_date: datetime.datetime = outbound_date
        self.price = price
        self.stopovers = stopovers
        self.via_city = via_city
