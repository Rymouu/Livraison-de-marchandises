import sqlite3

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
    
    def setContenu(self, contenu):
        self.contenu = contenu
    
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
        self.statut_livreur = ""
        self.id_camion = ""
        self.id_localisation = ""
        
        # Vérifier si l'ID existe dans la base de données et initialiser les attributs
        self.existe_dans_base()

    def existe_dans_base(self):
        # Requête SQL pour vérifier l'existence de l'ID dans la table livreur
        cursor.execute("SELECT * FROM livreur WHERE id_livreur = ?", (self.id,))
        row = cursor.fetchone()  # Récupérer la première ligne

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

class Camion:

    def __init__(self, id):
        self.id = id
        self.autonomie = 0
        self.capacite = 0
        self.etat = ""
        
        # Vérifier si l'ID existe dans la base de données et initialiser les attributs
        self.existe_dans_base()

    def existe_dans_base(self):
        # Requête SQL pour vérifier l'existence de l'ID dans la table Camion
        cursor.execute("SELECT * FROM camion WHERE id_camion = ?", (self.id,))
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