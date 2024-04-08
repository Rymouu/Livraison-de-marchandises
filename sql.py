import sqlite3

conn = sqlite3.connect('projet.db')

cursor = conn.cursor()

cursor.execute(
    "INSERT INTO camion (capacite, autonomie, etat) \
      VALUES (15, 350, 'Très bien')"
)
cursor.execute(
    "INSERT INTO livreur (nom, prenom, statut_livreur, id_camion, id_localisation) \
      VALUES ('Dupont', 'Jean', 1, 1, 1)"
)

cursor.execute(
    "SELECT * \
     FROM livreur"
)
resultat = cursor.fetchall()
print(resultat)
conn.commit()
conn.close()