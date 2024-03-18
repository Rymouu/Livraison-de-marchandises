import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Mission:
    def __init__(self, id, details, quantite, salaire, date_limite):
        self.id = id
        self.details = details
        self.etat = "Pas commencée"
        self.quantite = quantite
        self.salaire = salaire
        self.date_envoi = datetime.now()
        self.date_limite = date_limite
        self.id_message = ""

# Exemple de données factices pour les missions
missions = [
    Mission(1, "Livraison de colis", 10, 100.0, datetime(2024, 4, 1)),
    Mission(2, "Transport de marchandises fragiles", 5, 200.0, datetime(2024, 3, 25)),
    Mission(3, "Distribution de produits alimentaires", 20, 150.0, datetime(2024, 4, 5)),
    Mission(4, "Livraison express", 8, 180.0, datetime(2024, 3, 22)),
    Mission(5, "Transport de matériaux de construction", 15, 250.0, datetime(2024, 4, 10))
]

def valider_ajout(entry_details, entry_quantite, entry_salaire, entry_date_limite):
    # Fonction pour valider l'ajout de la mission
    details = entry_details.get()
    quantite_str = entry_quantite.get()
    salaire_str = entry_salaire.get()
    date_limite_str = entry_date_limite.get()

    # Vérifier les entrées et afficher une boîte de dialogue en cas d'erreur
    if not details or not quantite_str or not salaire_str or not date_limite_str:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    try:
        quantite = int(quantite_str)
        salaire = float(salaire_str)
        date_limite = datetime.strptime(date_limite_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez saisir des valeurs numériques valides pour la quantité et le salaire, et respecter le format de date (YYYY-MM-DD) pour la date limite.")
        return

    # Ajouter la mission à la liste de missions (simulant l'ajout à la base de données)
    missions.append(Mission(len(missions) + 1, details, quantite, salaire, date_limite))
    ajout_window.destroy()
    messagebox.showinfo("Mission ajoutée", "La mission a été ajoutée avec succès.")

# Créer une fenêtre principale
root = tk.Tk()
root.title("Centrale de Livraison")

def afficher_missions(missions_list):
    affichage_window = tk.Toplevel()
    affichage_window.title("Missions")

    # Créer un widget Listbox pour afficher les missions
    listbox_missions = tk.Listbox(affichage_window, height=10, width=50)
    listbox_missions.pack(padx=10, pady=10)

    # Ajouter les détails des missions à la Listbox
    for mission in missions_list:
        mission_details = f"Mission {mission.id}: {mission.details}"
        listbox_missions.insert(tk.END, mission_details)

    # Lier le double-clic sur une mission à l'affichage de ses détails
    listbox_missions.bind("<Double-Button-1>", lambda event: afficher_details_mission(missions_list[listbox_missions.curselection()[0]]))

affichage_window = None  # Déclarer la variable en dehors des fonctions

def afficher_dernieres_missions():
    global affichage_window  # Utiliser la variable globale dans la fonction
    # Fonction pour afficher les 10 dernières missions dans une fenêtre Tkinter
    top_10_missions = missions[-10:]  # Récupérer les 10 dernières missions
    
    affichage_window = tk.Toplevel()
    affichage_window.title("Dernières Missions")

    # Cadre pour contenir les boutons
    cadre_boutons = tk.Frame(affichage_window)
    cadre_boutons.pack(pady=5)

    # Ajouter un bouton pour afficher les missions non pourvues
    button_missions_non_pourvues = tk.Button(cadre_boutons, text="Afficher les missions non pourvues", command=afficher_missions_non_pourvues)
    button_missions_non_pourvues.pack(side=tk.LEFT, padx=5)

    # Ajouter un bouton pour afficher toutes les missions
    button_afficher_toutes_les_missions = tk.Button(cadre_boutons, text="Afficher toutes les missions", command=afficher_toutes_les_missions)
    button_afficher_toutes_les_missions.pack(side=tk.LEFT, padx=5)

    # Créer un widget Listbox pour afficher les missions
    listbox_missions = tk.Listbox(affichage_window, height=10, width=50)
    listbox_missions.pack(padx=10, pady=10)

    # Ajouter les détails des missions à la Listbox
    for mission in top_10_missions:
        mission_details = f"Mission {mission.id}: {mission.details}"
        listbox_missions.insert(tk.END, mission_details)

    # Lier le double-clic sur une mission à l'affichage de ses détails
    listbox_missions.bind("<Double-Button-1>", lambda event: afficher_details_mission(top_10_missions[listbox_missions.curselection()[0]]))

def afficher_missions_non_pourvues():
    missions_non_pourvues = [mission for mission in missions if mission.etat != "Pourvue"]
    affichage_window.destroy()  # Fermer la fenêtre actuelle
    afficher_missions(missions_non_pourvues)

def afficher_toutes_les_missions():
    affichage_window.destroy()  # Fermer la fenêtre actuelle
    afficher_missions(missions)

def afficher_details_mission(mission):
    details_window = tk.Toplevel()
    details_window.title(f"Détails Mission {mission.id}")

    details_label = tk.Label(details_window, text=f"Détails Mission {mission.id}:\n{mission.details}\nQuantité: {mission.quantite}\nSalaire: {mission.salaire}\nDate limite: {mission.date_limite}")
    details_label.pack(padx=10, pady=10)


# Fonction pour ouvrir la fenêtre d'ajout de mission
def ouvrir_ajout_window():
    ajout_window = tk.Toplevel()
    ajout_window.title("Ajouter Mission")

    # Widgets pour le formulaire
    label_details = tk.Label(ajout_window, text="Détails de la mission:")
    label_details.pack()
    entry_details = tk.Entry(ajout_window)
    entry_details.pack()

    label_quantite = tk.Label(ajout_window, text="Quantité:")
    label_quantite.pack()
    entry_quantite = tk.Entry(ajout_window)
    entry_quantite.pack()

    label_salaire = tk.Label(ajout_window, text="Salaire:")
    label_salaire.pack()
    entry_salaire = tk.Entry(ajout_window)
    entry_salaire.pack()

    label_date_limite = tk.Label(ajout_window, text="Date limite (YYYY-MM-DD):")
    label_date_limite.pack()
    entry_date_limite = tk.Entry(ajout_window)
    entry_date_limite.pack()

    button_valider = tk.Button(ajout_window, text="Valider", command=lambda: valider_ajout(entry_details, entry_quantite, entry_salaire, entry_date_limite))
    button_valider.pack()

# Bouton pour afficher les 10 dernières missions
button_afficher_missions = tk.Button(root, text="Afficher les missions", command=afficher_dernieres_missions)
button_afficher_missions.pack(pady=5)

# Bouton pour ajouter une mission
button_ajouter_mission = tk.Button(root, text="Ajouter une mission", command=ouvrir_ajout_window)
button_ajouter_mission.pack(pady=5)

# Fonction pour afficher les messages d'erreur de manière modale
def show_modal_error(title, message):
    modal = tk.Toplevel()
    modal.grab_set()  # Rendre la fenêtre modale, bloque l'accès aux autres fenêtres
    modal.title(title)
    tk.Label(modal, text=message).pack(padx=20, pady=10)
    tk.Button(modal, text="OK", command=modal.destroy).pack(pady=5)

# Rediriger les messages d'erreur vers les fenêtres modales
def show_error(title, message):
    show_modal_error(title, message)

messagebox.showerror = show_error

# Lancer la boucle principale Tkinter
root.mainloop()

