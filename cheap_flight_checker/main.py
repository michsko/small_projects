import data_manager
import flight_data
import flight_search
import notification_manager
from datetime import datetime, timedelta
from user_manager import UserManager


# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

um = UserManager()
um.check_user()
dm = data_manager.DataManager()
data_sheet = dm.get_destination_data()
fs = flight_search.FlightSearch()

nm = notification_manager.NotificationManager()

for index in data_sheet["prices"]:
    if index["iataCode"] == "":
        city = index["city"]
        row = index["id"]
        iataCode = fs.get_destination_iata_code(city)
        dm.update_iata_data_sheet(iataCode, row)

today = datetime.now()
date_from = today + timedelta(days=1)
date_from = date_from.strftime("%d/%m/%Y")
date_to = today + timedelta(days=183)
date_to = date_to.strftime("%d/%m/%Y")
return_from = today + timedelta(days=8)
return_from = return_from.strftime("%d/%m/%Y")
return_to = today + timedelta(days=29)
return_to = return_to.strftime("%d/%m/%Y")

for index in data_sheet["prices"]:
    destination = index['iataCode']
    city = index["city"]
    lowest_price = index["lowestPrice"]

    flight_data = fs.get_cheap_flights(destination, lowest_price, city, date_from, date_to, return_from, return_to)

    if flight_data is not None and flight_data.price < lowest_price:
        users = um.get
        nm.send_sms(message=f"Low price alert! Only {flight_data.price} € to fly from " \
                            f"{flight_data.origin_city}-{flight_data.origin_airport} to " \
                            f"{flight_data.destination_city}-{flight_data.destination_airport}, from" \
                            f"{flight_data.out_date} to {flight_data.return_date}")
