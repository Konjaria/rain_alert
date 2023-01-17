import requests  # importing requests library
import os  # importing os library
from twilio.rest import Client  # importing twilio library

# Tbilisi lat and lon
tbilisi_lat = 41.693630
tbilisi_lon = 44.801620

# getting api_key from environment variable
api_key = os.environ.get('api_key')

# setting parameters for API call
parameters = {
    "lat": 42.419250,
    "lon": 11.870290,
    "appid": api_key
}

# getting account_sid and auth_token from environment variable
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

# making API call
api_call = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)

# checking for the status of API call
api_call.raise_for_status()

# parsing json data from API call
data = api_call.json()

# checking the weather status
if data.get("weather")[0]["id"] < 700:
    BODY = "Don't forget to bring an umbrella, it goes to start rain ☔"
    # creating twilio client
    client = Client(account_sid, auth_token)
    # sending SMS message
    message = client.messages.create(body=BODY, from_='+13xxxxxxxx1', to='+995xxxxxxxxx')
