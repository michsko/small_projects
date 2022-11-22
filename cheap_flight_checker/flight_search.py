import requests
from flight_data import FlightData

APIKEY = "_zHmSvmbwdsrbTBUp-K7Lx8pR8MWYfK_"
LOCATION_URL = "https://api.tequila.kiwi.com/locations/query"
header = {"apikey": APIKEY}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API

    def get_destination_iata_code(self, city):
        parameters = {"term": city,
                      "location_types": "city"}
        response = requests.get(url=LOCATION_URL, headers=header, params=parameters)
        location_data = response.json()
        self.destination_iata_code = location_data['locations'][0]["code"]

        return self.destination_iata_code

    def get_cheap_flights(self, destination, price, city, date_from, date_to, return_from, return_to):

        search_url = "https://api.tequila.kiwi.com/v2/search"
        search_parameters = {"fly_from": 'PRG',
                             "fly_to": destination,
                             "date_from": date_from,
                             "date_to": date_to,
                             "return_from": return_from,
                             "return_to": return_to,
                             "flight_type": "round",
                             "curr": "EUR",
                             "price_from": 0,
                             "price_to": price,
                             "max_stopovers": 0}

        response = requests.get(url=search_url, headers=header, params=search_parameters)
        try:
            cheap_flight_data = response.json()["data"][0]
            print(f"{city}: €{cheap_flight_data['price']}")
        except IndexError:
            print(f"No flights found for {city}")
            return None
        else:
            flight_data = FlightData(
                price=cheap_flight_data["price"],
                origin_city=cheap_flight_data["route"][0]["cityFrom"],
                origin_airport=cheap_flight_data["route"][0]["flyFrom"],
                destination_city=cheap_flight_data["route"][0]["cityTo"],
                destination_airport=cheap_flight_data["route"][0]["flyTo"],
                out_date=cheap_flight_data["route"][0]["local_departure"].split("T")[0],
                return_date=cheap_flight_data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
