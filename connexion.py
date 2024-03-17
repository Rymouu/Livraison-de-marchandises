import tkinter as tk

def login():
    """Fonction pour vérifier les informations de connexion."""
    username = username_entry.get()
    password = password_entry.get()

    # Vérification des informations de connexion
    if username == "1":
        # Fermer la fenêtre de connexion
        root.destroy()
        # Ouvrir la fenêtre d'affichage
        import affichage
    else:
        message_label.config(text="Identifiant ou mot de passe incorrect", fg="red")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Livraison de Marchandise")  # Titre principal

# Ajout de marges autour de la fenêtre principale
root.configure(padx=20, pady=20)

# Création des widgets
title_label = tk.Label(root, text="Livraison de Marchandise", font=("Arial", 20), pady=10)  # Titre principal en gros
subtitle_label = tk.Label(root, text="Version Livreur", font=("Arial", 12))  # Sous-titre
username_label = tk.Label(root, text="Nom d'utilisateur:")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Mot de passe:")
password_entry = tk.Entry(root, show="*")  # Pour masquer le mot de passe
login_button = tk.Button(root, text="Se connecter", command=login)
message_label = tk.Label(root, text="")

# Placement des widgets dans la grille
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")  # Centrage vertical et horizontal
subtitle_label.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Centrage vertical et horizontal
username_label.grid(row=2, column=0, padx=5, pady=5)
username_entry.grid(row=2, column=1, padx=5, pady=5)
password_label.grid(row=3, column=0, padx=5, pady=5)
password_entry.grid(row=3, column=1, padx=5, pady=5)
login_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")  # Centrage vertical et horizontal
message_label.grid(row=5, column=0, columnspan=2, sticky="nsew")  # Centrage vertical et horizontal

# Ajout de lignes et colonnes vides pour centrer tous les éléments
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Lancement de la boucle principale
root.mainloop()
