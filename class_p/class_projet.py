import sqlite3
from datetime import datetime
import geopy,certifi,ssl
from geopy.geocoders import Nominatim

conn = sqlite3.connect('projet.db')

cursor = conn.cursor()

class Message:

    def __init__(self, id):
        self.id = id
        self.contenu = ""
        self.date_envoie = "" 
        self.id_livreur = ""
        self.id_centrale = ""
        self.id_mission = ""
    
    def setContenu(self, contenu):  #self represente un message particulier 
        self.contenu = contenu       # ici contenu d'un message en particulier
    
    def envoyer(self, date, contenu, id_livreur, id_centrale, id_mission):
        global cursor
        cursor.execute(
            "INSERT INTO message (contenu, date_envoie, id_mission, id_livreur, id_centrale) \
            VALUES (?, ?, ?, ?, ?)", (contenu, date, id_mission, id_livreur, id_centrale)
        )
        
        print("Message envoyé")

class Livreur:

    def __init__(self, id):
        self.id = id
        self.nom = ""
        self.prenom = ""
        self.statut_livreur = True
        self.id_camion = ""
        self.id_localisation = ""
        
        # Vérifier si l'ID existe dans la base de données et initialiser les attributs
        self.existe_dans_base()

    def existe_dans_base(self):
        # Requête SQL pour vérifier l'existence de l'ID dans la table livreur
        cursor.execute("SELECT * FROM livreur WHERE id_livreur = ?", (self.id,))  # , après id pour créer un tuple avec un seul élément
        row = cursor.fetchone()  # Récupérer le premier attribut du tuple

        # Fermer la connexion à la base de données
        conn.close()

        # Vérifier si une ligne a été retournée par la requête
        if row is not None:
            # Assigner les valeurs de la base de données aux attributs de l'objet Livreur
            self.nom = row[1]
            self.prenom = row[2]
            self.statut_livreur = row[3]
            self.id_camion = row[4]
            self.id_localisation = row[5]
        else:
            raise ValueError("Aucun livreur avec cet ID trouvé dans la base de données")
        
    def est_volontaire(self):
        return self.statut_livreur and self.id_camion != ""
    
    def afficher_informations(self):
        print("Nom:", self.nom)
        print("Prénom:", self.prenom)
        print("Statut:", self.statut_livreur)
        print("ID localisation:", self.id_localisation)
        camion = Camion(self.id_camion)
        print("Capacité du camion:", camion.capacite)
        print("Autonomie du camion:", camion.autonomie)
        print("Etat du camion: ", camion.etat)
        
class Centrale:

    def __init__(self, id):
        self.id = id
        self.nom = ""
        self.id_localisation = ""
        self.missions = []  

    def ajouter_mission(self,mission):
        self.missions.append(mission)

    def attribuer_mission(self,livreur,mission):
        if livreur.est_volontaire():
            livreur.ajouter_mission(mission)
            self.ajouter_mission(mission)
    
    def repondre_aux_messages(self):
        pass
        


class Camion:

    def __init__(self, id):
        self.id = id
        self.autonomie = 0
        self.capacite = 0
        self.etat = ""
        
        # Vérifier si l'ID existe dans la base de données et initialiser les attributs  (on a le droit en python d'appeler la fonction avant meme de la definir tant qu'on la defini a un endroit dans la classe)
        self.existe_dans_base()

    def existe_dans_base(self):
        # Requête SQL pour vérifier l'existence de l'ID dans la table Camion
        cursor.execute("SELECT * FROM camion WHERE id_camion = ?", (self.id,))  #cursor objet de la classe sqlite3, permet d'executer des requetes sql
        row = cursor.fetchone()  # Récupérer la première ligne

        # Fermer la connexion à la base de données
        conn.close()

        # Vérifier si une ligne a été retournée par la requête
        if row is not None:
            # Assigner les valeurs de la base de données aux attributs de l'objet Camion
            self.capacite = row[1]
            self.autonomie = row[2]
            self.etat = row[3]
        else:
            raise ValueError("Aucun camion avec cet ID trouvé dans la base de données")
        
    def mettre_a_jour_capacite(self,nouvelle_capacite):
        if self.etat == "Disponible":
           self.capacite = nouvelle_capacite
        else:
            self.capacite = 0
        
class Mission:

    def __init__(self, id):
        self.id = id
        self.details = ""
        self.etat = "Pas commencée"
        self.quantite = ""
        self.salaire = 0
        self.date_envoi = datetime.now()
        self.date_limite = None
        self.id_message = ""

    def ajouter_livraison(self, livraison):
        self.livraisons.append(livraison)             #QUESTION 1

class Localisation:

    def __init__(self, id):
        self.id = id
        self.longitude = 0
        self.latitude = 0
        self.adresse = ""
        self.existe_dans_base()

    def existe_dans_base(self):
        # Requête SQL pour vérifier l'existence de l'ID dans la table Localisation
        cursor.execute("SELECT * FROM localisation WHERE id_localisation = ?", (self.id,))  # , après id pour créer un tuple avec un seul élément
        row = cursor.fetchone()  # Récupérer le premier attribut du tuple

        # Fermer la connexion à la base de données
        conn.close()

        # Vérifier si une ligne a été retournée par la requête
        if row is not None:
            # Assigner les valeurs de la base de données aux attributs de l'objet Livreur
            self.longitude = float(row[1])
            self.latitude = float(row[2])
        else:
            raise ValueError("Aucune localisation avec cet ID trouvé dans la base de données")
    
    def get_adresse(self):
        geopy.geocoders.options.default_ssl_context = ssl.create_default_context(cafile=certifi.where()) #QUESTION 2
        geolocator = Nominatim(user_agent="projet")
        location = geolocator.reverse((self.latitude, self.longitude))
        self.adresse = location.address


#fermer la connexion a la toute fin au lieu de fermer a l'interieur de chaque classe