import sqlite3
from datetime import datetime
import sys
sys.path.append('/class_p')
from class_p import class_projet

conn = sqlite3.connect('projet.db')

cursor = conn.cursor()

def ajouter_livreur_bdd(nom, prenom, statut_livreur, capacite, autonomie, etat, id_localisation):
    # Requête SQL pour insérer un livreur dans la table Livreur
    cursor.execute("INSERT INTO camion (capacite, autonomie, etat) VALUES (?,?,?)", (capacite, autonomie, etat))
    conn.commit()
    print("Camion ajouté à la base de données")
    id_camion = cursor.lastrowid
    cursor.execute("INSERT INTO livreur VALUES (?,?,?,?,?)", (nom, prenom, statut_livreur, id_camion, id_localisation))
    conn.commit()
    print("Livreur ajouté à la base de données")