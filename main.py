from tkinter import *
import requests 
import json 
from PIL import Image, ImageTk

root = Tk()
root.title('Street Weather')
root.geometry("640x380")

api_key = "http://api.openweathermap.org/data/2.5/weather?id=2990969&appid=4275cf39840e13bd2503187dce72cbab"
api_request = requests.get(api_key)

try:
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error"

weather = json.dumps(api["weather"])
print(weather)

main = json.dumps(api["main"])
print(main)

clouds = json.dumps(api["clouds"])
print(clouds)

country = json.dumps(api["sys"]["country"])
print(country)

city = json.dumps(api["name"])
print(city)



myLabel1 = Label(root, text=api["weather"], wraplength=580, bg='cyan')
myLabel2 = Label(root, text=api["main"], wraplength=580, bg='cyan')
myLabel3 = Label(root, text=api["clouds"], wraplength=580, bg='cyan')
myLabel4 = Label(root, text=api["sys"], wraplength=580, bg='cyan')
myLabel5 = Label(root, text=api["name"], wraplength=580, bg='cyan')

myLabel1.pack()
myLabel2.pack()
myLabel3.pack()
myLabel4.pack()
myLabel5.pack()

root.mainloop()
