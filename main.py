from tkinter import *
import requests 
import json 
from PIL import Image, ImageTk
import mysql.connector as mariadb
from mysql.connector import errorcode
from datetime import datetime
import sys
from controller import graphic 

#--------------------------------------------------------------

api_key = "http://api.openweathermap.org/data/2.5/weather?id=2990969&appid=4275cf39840e13bd2503187dce72cbab"
api_request = requests.get(api_key)

try:
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error"

meteo = json.dumps(api["weather"])
print(meteo)

temps = json.dumps(api["weather"][0]["main"])
print(temps)

description = json.dumps(api["weather"][0]["description"])
print(description)

ttemp = json.dumps(api["main"]["temp"])
ftemp = float(ttemp)
ftemp = ftemp - 273
temp = str(ftemp)
print(temp)

trtemp = json.dumps(api["main"]["feels_like"])
frtemp = float( trtemp)
frtemp -= 273
rtemp = str(frtemp)
print(rtemp)

humidity = json.dumps(api["main"]["humidity"])
print(humidity)

clouds = json.dumps(api["clouds"]["all"])
print(clouds)

country = json.dumps(api["sys"]["country"])
print(country)

city = json.dumps(api["name"])
print(city)

city_id = json.dumps(api["id"])
print(city_id)

date = (datetime.now())
print(str(date))

#--------------------------------------------------------------

root = Tk()
root.title('Street Weather')
root.geometry("640x380")

hi_there = Button(root)
hi_there["text"] = "Pour voir le résultat\n(clique ici)"
#hi_there["command"] = say_hi
hi_there.pack(side="top")
quit = Button(root, text="QUIT", fg="red")#,command=destroy)
quit.pack(side="bottom")

myLabel1 = Label(root, text=api["weather"], wraplength=580, bg='cyan').pack()
myLabel2 = Label(root, text=api["main"], wraplength=580, bg='cyan').pack()
myLabel3 = Label(root, text=api["clouds"], wraplength=580, bg='cyan').pack()
myLabel4 = Label(root, text=api["sys"], wraplength=580, bg='cyan').pack()
myLabel5 = Label(root, text=api["name"], wraplength=580, bg='cyan').pack()

#--------------------------------------------------------------

mariadb_connection = mariadb.connect(user='Utilisateur', password='P@ssw0rd123', database='streetweather')
cursor = mariadb_connection.cursor()
cursor.execute("SET sql_mode = '' ")

sqlvalues1 = ("INSERT INTO meteo" 
                "( Temps, Description, Temperature, Temp_Ressentie, Humidite, Nuages, Date, ID_Ville)" 
                "VALUES(%(Temps)s,%(Description)s,%(Temperature)s,%(Temp_Ressentie)s,%(Humidite)s,%(Nuages)s,%(Date)s,%(ID_Ville)s)")
sqlvalue1 = {
    'Temps':temps,
    'Description':description,
    'Temperature':temp,
    'Temp_Ressentie':rtemp,
    'Humidite':humidity,
    'Nuages':clouds,
    'Date': date,
    'ID_Ville':'Humidite'
    }
cursor.execute(sqlvalues1,sqlvalue1)
mariadb_connection.commit()


sqlvalues2 = ("INSERT INTO pays" 
                "(Pays)" 
                "VALUES(%(Pays)s) ON DUPLICATE KEY UPDATE ID_Pays = ID_Pays+1")
sqlvalue2={
    'Pays':country,
    }
cursor.execute(sqlvalues2,sqlvalue2)
mariadb_connection.commit()

sqlvalues3 = ("INSERT INTO ville" 
                "(Ville)" 
                "VALUES(%(Ville)s) ON DUPLICATE KEY UPDATE ID_Ville = ID_Ville")
sqlvalue3={
    'ID_Ville':city_id,
    'Ville':city,
    }
cursor.execute(sqlvalues3,sqlvalue3)
mariadb_connection.commit()


root.mainloop()

cursor.close()
mariadb_connection.close()
