import tkinter as tk
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('projet.db')
cursor = conn.cursor()

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
        cursor.execute("SELECT * FROM livreur WHERE id_livreur = ?", (self.id,))  
        row = cursor.fetchone()  

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
        return f"Nom: {self.nom}\nPrénom: {self.prenom}\nStatut: {self.statut_livreur}\nID localisation: {self.id_localisation}"

# Fonction pour récupérer et afficher les 10 dernières missions de la base de données
def afficher_dernieres_missions():
    cursor.execute("SELECT * FROM mission ORDER BY id_message DESC LIMIT 10")
    missions = cursor.fetchall()
    for mission in missions:
        mission_details = f"État: {mission[1]}\nDétails: {mission[2]}\nQuantité: {mission[3]}\nSalaire: {mission[4]}\nDate envoi: {mission[5]}\nDate limite: {mission[6]}\nID livreur: {mission[7]}\nID localisation: {mission[8]}\n"
        tk.Label(missions_frame, text=mission_details).pack()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Application de livraison")

# Création et placement des éléments dans la fenêtre
welcome_label = tk.Label(root, text="Bienvenue livreur !", font=("Arial", 24))
welcome_label.pack(pady=20)

# Affichage des informations du livreur en bas à gauche
livreur = Livreur(1)  # ID du livreur à récupérer
informations_label = tk.Label(root, text=livreur.afficher_informations(), justify="left")
informations_label.pack(side="left", anchor="sw", padx=20, pady=20)

# Affichage des 10 dernières missions en bas à droite
missions_frame = tk.Frame(root)
missions_frame.pack(side="right", anchor="se", padx=20, pady=20)
missions_label = tk.Label(missions_frame, text="Dix dernières missions :")
missions_label.pack()
afficher_dernieres_missions()

# Lancement de la boucle principale
root.mainloop()

# Fermeture de la connexion à la base de données
conn.close()

