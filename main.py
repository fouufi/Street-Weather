import tkinter
import requests 
import json 
from PIL import Image, ImageTk

root = Tk()
root.title('test titre')
root.geometry("400x400")

api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2990969&appid=4275cf39840e13bd2503187dce72cbab")
try:
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error"

myLabel = Label(root, text=api)
myLabel.pack()