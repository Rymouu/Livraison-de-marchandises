import sqlite3
from datetime import datetime
import sys
from class_projet import *
import geopy,certifi,ssl
from geopy.geocoders import Nominatim

def ajouter_livreur_bdd(nom, prenom, statut_livreur, capacite, autonomie, etat, id_localisation):

    conn = sqlite3.connect('projet.db')
    cursor = conn.cursor()
    # Requête SQL pour insérer un livreur dans la table Livreur
    cursor.execute("INSERT INTO camion (capacite, autonomie, etat) VALUES (?,?,?)", (capacite, autonomie, etat))
    conn.commit()
    print("Camion ajouté à la base de données")
    id_camion = cursor.lastrowid
    cursor.execute("INSERT INTO livreur VALUES (?,?,?,?,?)", (nom, prenom, statut_livreur, id_camion, id_localisation))
    conn.commit()
    print("Livreur ajouté à la base de données")
    conn.close()

def coordonnees_from_adresse(adresse):
    # Créer un géocodeur Nominatim
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    # Création d'un objet géocodeur Nominatim
    geolocator = Nominatim(user_agent="my_geocoder")
    # Géocodage d'une adresse
    location = geolocator.geocode(adresse)
    # Affichage des informations de localisation
    return location.latitude, location.longitude

def get_id_localisation(longi, lattitude):
    conn = sqlite3.connect('projet.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_localisation FROM localisation WHERE longitude = ? AND latitude = ?", (float(longi), float(lattitude)))
    row = cursor.fetchone()
    if row is not None:
        conn.close()
        return row[0]
    else:
        cursor.execute("INSERT INTO localisation (longitude, latitude) VALUES (?,?)", (float(longi), float(lattitude)))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    
def afficher_colonnes_table(nom_table):
    conn = sqlite3.connect('projet.db')
    cursor = conn.cursor()

    # Exécute la requête pour récupérer les informations sur la table
    cursor.execute("PRAGMA table_info({})".format(nom_table))

    # Récupère les résultats de la requête
    results = cursor.fetchall()

    # Affiche les noms des colonnes
    print("Colonnes de la table {}:".format(nom_table))
    for row in results:
        print(row[1])  # La colonne "name" contient le nom de la colonne

    # Ferme la connexion
    conn.close()
