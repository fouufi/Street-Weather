from tkinter import *
import mysql.connector
from mysql.connector import errorcode
import matplotlib.pyplot as plt

root = Tk()
root.title('Street Weather')
root.geometry("640x380")

#Connexion à la base de données
try:
    bdd = mysql.connector.connect(
            host="localhost",
            user="Utilisateur",
            password="P@ssw0rd123",
            database="streetweather"
            )
except mysql.connector.Error as err:
    print("Error occured (BDD Connexion) : {}".format(err))

#Creation du curseur
cursor = bdd.cursor()
cursor.execute("SET sql_mode = '' ")

class Graph:
    def __init__(self, parent):
        self.label = Label(root, text="Ville à chercher")
        self.label.pack()
        self.E = Entry(root, width=10)
        self.E.pack()

        self.button = Button(root, text = "Valider", command = self.get_entry)
        self.button.pack(anchor = S)
        self.ville = 0
    
    def get_entry(self):
        self.ville = self.E.get()
        print (self.ville)
        self.get_info()
    
    def get_info(self):
        self.req_getVille = "SELECT Ville FROM Ville WHERE Ville = %s"
        cursor.execute(self.req_getVille, (self.ville,)) #Recherche du nom de la ville dans la bdd
        self.Ville = cursor.fetchall() #Stockage du nom de la ville
        print ('La ville demandée est bien présente dans la bdd : ', self.Ville)

#Récupération des données météo
#req_getVille = "SELECT Ville FROM Ville WHERE Ville = %s"
#cursor.execute(req_getVille, (ville,)) #Recherche du nom de la ville dans la bdd
#Ville = cursor.fetchall() #Stockage du nom de la ville
#print ('La ville demandée est : ', Ville)

#req_getTime = "SELECT Time FROM Meteo WHERE ID_Ville = %s" #Modif bdd à faire pour stocker l'heure
#req_getTemps = "SELECT Temps FROM Meteo WHERE ID_Ville = %s"
#req_getTemperature = "SELECT Temperature FROM Meteo WHERE ID_Ville = %s"


#Creation du graphe
#x=[5,8,10]
#y=[12,16,6]
#plt.plot(x,y)
#plt.title("info")
#plt.ylabel("Y axis")
#plt.xlabel("X axis")
#plt.show()

graph = Graph(root)
root.mainloop()

#Fermeture de la connexion à la bdd
cursor.close()
bdd.close()
