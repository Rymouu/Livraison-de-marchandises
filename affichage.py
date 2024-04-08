import tkinter as tk
from tkinter import messagebox
import sqlite3
from class_projet import *
from fonctions import *
import webbrowser

# Connexion à la base de données
conn = sqlite3.connect('projet.db')
cursor = conn.cursor()

# Fonction pour afficher les informations du livreur et les 10 dernières missions dans une seule fenêtre
def afficher_informations(livreur):
    missions = recuperer_missions()[-10:]  # Récupérer les 10 dernières missions
    
    fenetre_info = tk.Toplevel()
    fenetre_info.title("Informations Livreur et Missions")

    # Cadre pour les informations du livreur
    cadre_livreur = tk.Frame(fenetre_info)
    cadre_livreur.pack(pady=10)

    # Affichage des informations du livreur dans le cadre
    informations_livreur_label = tk.Label(cadre_livreur, text=livreur.afficher_informations(), justify="left")
    informations_livreur_label.pack(side="left", padx=20)

    # Bouton pour modifier les informations du livreur
    bouton_modifier = tk.Button(cadre_livreur, text="Modifier", command=lambda: modifier_informations(livreur, fenetre_info, informations_livreur_label))
    bouton_modifier.pack(side="right", padx=20)

    # Cadre pour les missions
    cadre_missions = tk.Frame(fenetre_info)
    cadre_missions.pack(pady=10)

    # Créer un widget Listbox pour afficher les missions
    listbox_missions = tk.Listbox(cadre_missions, height=10, width=50)
    listbox_missions.pack(padx=10, pady=10)

    # Ajouter les détails des missions à la Listbox
    for mission in missions:
        mission_details = f"Mission {mission.id}: {mission.details}"
        listbox_missions.insert(tk.END, mission_details)

    # Lier le double-clic sur une mission à l'affichage de ses détails
    listbox_missions.bind("<Double-Button-1>", lambda event: afficher_details_mission(missions[listbox_missions.curselection()[0]], fenetre_info))

# Fonction pour afficher les détails d'une mission sélectionnée
# Fonction pour afficher les détails d'une mission sélectionnée
def afficher_details_mission(mission, fenetre_parent):
    details_window = tk.Toplevel(fenetre_parent)
    details_window.title(f"Détails Mission {mission.id}")

    # Afficher les informations de la mission
    label_id = tk.Label(details_window, text=f"ID: {mission.id}")
    label_id.grid(row=1, column=0, sticky="w")

    label_etat = tk.Label(details_window, text=f"État: {mission.etat}")
    label_etat.grid(row=2, column=0, sticky="w")

    label_details = tk.Label(details_window, text=f"Détails: {mission.details}")
    label_details.grid(row=3, column=0, sticky="w")

    label_quantite = tk.Label(details_window, text=f"Quantité: {mission.quantite}")
    label_quantite.grid(row=4, column=0, sticky="w")

    label_salaire = tk.Label(details_window, text=f"Salaire: {mission.salaire}")
    label_salaire.grid(row=5, column=0, sticky="w")

    label_date_limite = tk.Label(details_window, text=f"Date limite: {mission.date_limite}")
    label_date_limite.grid(row=6, column=0, sticky="w")

    loc = Localisation(mission.id_localisation_a)

    label_id_localisation_a = tk.Label(details_window, text=f"Localisation d'arrivée: {loc.adresse}")
    label_id_localisation_a.grid(row=7, column=0, sticky="w")

    # Bouton pour ouvrir Google Maps avec l'itinéraire vers la mission
    bouton_itineraire = tk.Button(details_window, text="Itinéraire", command=lambda: ouvrir_itineraire(loc.latitude, loc.longitude))
    bouton_itineraire.grid(row=8, column=0, pady=5)

    # Bouton pour candidater à la mission
    bouton_candidater = tk.Button(details_window, text="Candidater", command=lambda: candidater_a_mission(mission))
    bouton_candidater.grid(row=9, column=0, pady=5)

# Fonction pour ouvrir Google Maps avec l'itinéraire vers la mission
def ouvrir_itineraire(latitude, longitude):
    # Générer l'URL pour l'itinéraire vers la mission
    url = f"https://www.google.com/maps/dir/?api=1&destination={longitude},{latitude}"

    # Ouvrir Google Maps dans le navigateur par défaut
    webbrowser.open(url)

# Fonction pour permettre au livreur de candidater à la mission
def candidater_a_mission(mission):
    # Code pour permettre au livreur de candidater à la mission
    if mission.etat == "Disponible":
        cursor.execute("UPDATE mission SET id_livreur = ?, etat = ? WHERE id_message = ?", (livreur.id, "En attente", mission.id))
        conn.commit()
        tk.messagebox.showinfo("Succès", "Vous avez candidaté à la mission avec succès.")
    else:
        tk.messagebox.showerror("Erreur", "La mission n'est plus disponible.")


# Fonction pour modifier les informations du livreur
def modifier_informations(livreur, fenetre_parent, informations_livreur_label):
    # Fonction pour valider les modifications
    camion = Camion(livreur.id_camion)
    def valider_modifications():
        try:
            # Effectuer les assertions
            assert len(champ_nom.get()) > 0, "Le nom ne peut pas être vide"
            assert len(champ_prenom.get()) > 0, "Le prénom ne peut pas être vide"
            assert len(champ_adresse.get()) > 0, "L'adresse ne peut pas être vide"
            assert len(champ_capacite.get()) > 0, "La capacité ne peut pas être vide"
            assert len(champ_autonomie.get()) > 0, "L'autonomie ne peut pas être vide"
            assert len(champ_etat.get()) > 0, "L'état ne peut pas être vide"
            longitude, latitude = coordonnees_from_adresse(champ_adresse.get())
            id_localisation = get_id_localisation(longitude, latitude)

            # Mettre à jour les informations du livreur
            livreur.nom = champ_nom.get()
            livreur.prenom = champ_prenom.get()
            livreur.id_localisation = id_localisation
            camion.capacite = champ_capacite.get()
            camion.autonomie = champ_autonomie.get()
            camion.etat = champ_etat.get()
        
            # Mettre à jour les informations dans la base de données
            cursor.execute("UPDATE livreur SET nom = ?, prenom = ?, id_localisation = ?, id_camion = ? WHERE id_livreur = ?",
                        (livreur.nom, livreur.prenom, livreur.id_localisation, livreur.id_camion, livreur.id))
            conn.commit()

            # Mettre à jour l'affichage
            informations_livreur_label.config(text=livreur.afficher_informations())

            # Afficher un message de succès
            tk.messagebox.showinfo("Succès", "Les modifications ont été enregistrées avec succès.")
        except AssertionError as e:
            # Afficher un message d'erreur
            tk.messagebox.showerror("Erreur", str(e))


    # Créer une fenêtre pour la modification des informations
    fenetre_modification = tk.Toplevel(fenetre_parent)
    fenetre_modification.title("Modifier Informations")

    # Créer des champs de saisie pour le nom, le prénom, l'adresse et l'ID du camion
    tk.Label(fenetre_modification, text="Nom :").grid(row=0, column=0, sticky="w")
    tk.Label(fenetre_modification, text="Prénom :").grid(row=1, column=0, sticky="w")
    tk.Label(fenetre_modification, text="Adresse :").grid(row=2, column=0, sticky="w")
    tk.Label(fenetre_modification, text="Capacité du camion :").grid(row=3, column=0, sticky="w")
    tk.Label(fenetre_modification, text="Autonomie du camion :").grid(row=4, column=0, sticky="w")   
    tk.Label(fenetre_modification, text="Etat du camion :").grid(row=5, column=0, sticky="w")

    champ_nom = tk.Entry(fenetre_modification)
    champ_nom.grid(row=0, column=1, padx=5, pady=5)
    champ_nom.insert(tk.END, livreur.nom)

    champ_prenom = tk.Entry(fenetre_modification)
    champ_prenom.grid(row=1, column=1, padx=5, pady=5)
    champ_prenom.insert(tk.END, livreur.prenom)

    loc = Localisation(livreur.id_localisation)
    loc.get_adresse()
    champ_adresse = tk.Entry(fenetre_modification)
    champ_adresse.grid(row=2, column=1, padx=5, pady=5)
    champ_adresse.insert(tk.END, loc.adresse)


    champ_capacite = tk.Entry(fenetre_modification)
    champ_capacite.grid(row=3, column=1, padx=5, pady=5)
    champ_capacite.insert(tk.END, camion.capacite)

    champ_autonomie = tk.Entry(fenetre_modification)
    champ_autonomie.grid(row=4, column=1, padx=5, pady=5)
    champ_autonomie.insert(tk.END, camion.autonomie)

    champ_etat = tk.Entry(fenetre_modification)
    champ_etat.grid(row=5, column=1, padx=5, pady=5)
    champ_etat.insert(tk.END, camion.etat)

    # Bouton pour valider les modifications
    bouton_valider = tk.Button(fenetre_modification, text="Valider", command=valider_modifications)
    bouton_valider.grid(row=6, columnspan=2, padx=5, pady=5)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Application de livraison")
livreur = Livreur(1)  # ID du livreur à récupérer
camion = Camion(livreur.id_camion)
# Création et placement des éléments dans la fenêtre
welcome_label = tk.Label(root, text="Bienvenue livreur !", font=("Arial", 24))
welcome_label.pack(pady=20)

# Bouton pour afficher les informations du livreur et les 10 dernières missions
button_afficher_infos = tk.Button(root, text="Afficher Informations", command=lambda: afficher_informations(livreur))
button_afficher_infos.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
