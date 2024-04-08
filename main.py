import tkinter as tk
from tkinter import messagebox
import connexion
import affichage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Application de Livraison")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self, text="Bienvenue Livreur !", font=("Arial", 24))
        self.welcome_label.pack(pady=20)

        self.info_frame = tk.Frame(self)
        self.info_frame.pack(side="left", anchor="sw", padx=20, pady=20)
        self.info_label = tk.Label(self.info_frame, text="Informations du Livreur", font=("Arial", 12))
        self.info_label.pack()
        self.username_label = tk.Label(self.info_frame, text="Nom d'utilisateur:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.info_frame)
        self.username_entry.pack()
        self.password_label = tk.Label(self.info_frame, text="Mot de passe:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.info_frame, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.info_frame, text="Se connecter", command=self.login)
        self.login_button.pack()
        self.message_label = tk.Label(self.info_frame, text="", fg="red")
        self.message_label.pack()

        self.mission_frame = tk.Frame(self)
        self.mission_frame.pack(side="right", anchor="se", padx=20, pady=20)
        self.mission_label = tk.Label(self.mission_frame, text="Dix dernières missions :", font=("Arial", 12))
        self.mission_label.pack()
        self.afficher_dernieres_missions()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "1" and password == "password":
            self.message_label.config(text="Connexion réussie", fg="green")
        else:
            self.message_label.config(text="Identifiant ou mot de passe incorrect", fg="red")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
