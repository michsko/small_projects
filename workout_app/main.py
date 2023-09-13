import requests
import datetime

API_KEY = '4bb4a7af9e1d51c77bf88db46f2bfc27'
API_ID = 'e18e3eb4'

GENDER = "male"
WEIGHT = 108
HEIGHT = 169
AGE = 40

USERNAME = "sheety"
PASSWORD = "sheety"


url = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercises you did: ")

parameters = {"query":exercise, "gender":GENDER, "weight_kg":WEIGHT, "height_cm":HEIGHT, "age":AGE}

headers = {
	"x-app-id": API_ID, 
	"x-app-key": API_KEY}

response = requests.post(url, json=parameters, headers=headers)

result = response.json()

print(result) 

sheety_url = 'https://api.sheety.co/1195251ae8e671c612c74902c2775d90/myWorkouts/workouts'


datetime = datetime.datetime.now()

date = datetime.strftime("%d/%M/%Y")
time = datetime.strftime("%X")

for exercise in result["exercises"]:
	sheety_input = {
	"workout":{
		"date": date,
		"time": time,
		"exercise": exercise["name"].title(),
		"duration": exercise["duration_min"],
		"calories": exercise["nf_calories"]
	}
    }
    
"""   
response_sheety = requests.post(
    sheety_url, json=sheety_input
    )

"""

# basic authentication 
response_sheety = requests.post(sheety_url, json=sheety_input, 
    auth=(
    USERNAME,
    PASSWORD,
  )
  )
  
"""
# bearer token authentication 
bearer_headers = {
  
    "Authorization":"Bearer Token"}
	
  }


response_sheety = requests.post(
    sheety_url, 
    json=sheety_input, 
    headers=bearer_headers
  )

"""

print (response_sheety.text)



