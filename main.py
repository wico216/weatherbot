import requests
import socket
from pprint import pp #to print the json in a pretty way.
import os
from dotenv import load_dotenv

load_dotenv()# load environment variables from .env.

APIKEY=os.getenv('APIKEY')# get the API key from the environment variable.
hostname=socket.gethostname()# get the hostname of the computer.
ip=socket.gethostbyname(hostname)# get the ip address of the computer.



cityname = input("Enter a city name: ")
#userpref = input("Enter a temperature preference (F or C): ")

url = "http://api.weatherapi.com/v1/current.json?q="+cityname+"&key="+APIKEY

response = requests.get(url)
response_json = response.json()
date, time = response_json['location']['localtime'].split(" ")# split the date and time from the localtime string.




try:
    print(f"Weather in {response_json['location']['name']} is {response_json['current']['condition']['text']}, temperature is {response_json['current']['temp_f'] } F and time is {time}")
    #pp(response_json)
except:
    print("Error: " + response_json['error']['message'])