from tkinter import *
import requests 
import json 

#http://api.openweathermap.org/data/2.5/weather?id=2990969&appid=4275cf39840e13bd2503187dce72cbab

api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2990969&appid=4275cf39840e13bd2503187dce72cbab")
try:
    api = json.loads(api_request.content)
except Exception as e