from tkinter import *
import matplotlib.pyplot as plt
import mysql.connector as mariadb
from mysql.connector import errorcode

root = Tk()
root.title('Street Weather - Graphs')
root.geometry("640x380")

#Connexion à la base de données
try:
    mariadb_connection = mariadb.connect(
            host="localhost",
            user='Utilisateur',
            password='P@ssw0rd123',
            database='streetweather'
            )
except mysql.connector.Error as err:
    print("Error occured (BDD Connexion) : {}".format(err))

#Creation du curseur
cursor = mariadb_connection.cursor()
cursor.execute("SET sql_mode = '' ")
