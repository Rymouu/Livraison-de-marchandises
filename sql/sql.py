import sqlite3

conn = sqlite3.connect('projet.db')

cursor = conn.cursor()

cursor.execute(
    "INSERT INTO camion (capacite, autonomie, etat) \
      VALUES (15, 350, 'Très bien')"
)
cursor.execute(
    "INSERT INTO camion (capacite, autonomie, etat) \
      VALUES (10, 200, 'Moyen')"
)

cursor.execute(
    "SELECT * \
     FROM camion"
)
resultat = cursor.fetchall()
print(resultat)