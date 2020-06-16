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
        print ("Ville entrée : ", self.ville)
        self.get_info()
    
    def get_info(self):
        #Stockage nom ville
        self.req_getVille = "SELECT Ville FROM ville WHERE Ville = %s"
        cursor.execute(self.req_getVille, (self.ville,)) #Recherche du nom de la ville dans la bdd
        self.Ville = cursor.fetchall()
        for row in self.Ville:
            self.Ville = row[0]
            print ('La ville demandée est bien présente dans la bdd : ', self.Ville)

        #Stockage heures enregistrées
        self.req_getTime = "SELECT Date FROM meteo WHERE ID_Ville = %s"
        
        self.req_getIDVille = "SELECT ID_Ville FROM ville WHERE Ville = %s" #Récupération de l'id
        cursor.execute(self.req_getIDVille, (self.ville,)) #Execution de la requete
        self.ID_Ville = cursor.fetchall()
        for row in self.ID_Ville:
            self.ID_Ville = row[0]
            print ("ID de la Ville est : ", self.ID_Ville)


        cursor.execute(self.req_getTime, (self.ID_Ville,)) #Récupération de l'heure de l'enregistrement
        self.Time = cursor.fetchall()
        for row in self.Time:
            print (row)
        
        #Stockage des températures observées
        req_getTemperature = "SELECT Temperature FROM meteo WHERE ID_Ville = %s"


        #Creation du graphe
        #x=[5,8,10]
        #y=[12,16,6]
        #plt.plot(x,y)
        #plt.title("info")
        #plt.ylabel("Y axis")
        #plt.xlabel("X axis")
        #plt.show()


graph = Graph(root) #Création instance
root.mainloop()

#Fermeture de la connexion à la bdd
cursor.close()
bdd.close()
