from tkinter import *
import requests 
import json 
from PIL import Image, ImageTk

root = Tk()
root.title('Street Weather')
root.geometry("640x380")

api_key = "http://api.openweathermap.org/data/2.5/weather?id=2990969&appid=4275cf39840e13bd2503187dce72cbab"
api_request = requests.get(api_key)
#x = api_request.jons()

try:
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error"


myLabel = Label(root, text=api, wraplength=580, bg='cyan')
myLabel.pack()

root.mainloop()

