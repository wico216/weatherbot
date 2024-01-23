import requests
import os
from dotenv import load_dotenv

load_dotenv()# load environment variables from .env.

APIKEY=os.getenv('APIKEY')# get the API key from the environment variable.

userzipcode = input("Enter your zipcode: ")

url = "http://api.weatherapi.com/v1/current.json?key="+APIKEY+"&q="+userzipcode
response = requests.get(url)

response_json = response.json()


print(f"Current temperature in {response_json['location']['name']} is {response_json['current']['temp_f']} degrees Fahrenheit.")