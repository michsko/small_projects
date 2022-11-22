import requests
import flight_search

FLIGHTDEALS_SHEET_URL = "https://api.sheety.co/357df803cdf8a30e2c5b639060f7bf96/flightDeals/prices"
HEADER = {"Authorization": f"Bearer sdkfhskdhfksadkfsdkfhkj"}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=FLIGHTDEALS_SHEET_URL, headers=HEADER)
        self.destination_data = response.json()
        response.raise_for_status()

        return self.destination_data


    def update_iata_data_sheet(self, iataCode,id):

        update_url = "https://api.sheety.co/357df803cdf8a30e2c5b639060f7bf96/flightDeals/prices/"
        parameters = {"price": {"iataCode": iataCode}}

        response = requests.put(url=f"{update_url}{id}", json=parameters)
        response.raise_for_status()
        print(response.text)


