import sqlite3

conn = sqlite3.connect('projet.db')

cursor = conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS `camion` (
`id_camion` INTEGER PRIMARY KEY AUTOINCREMENT,
  `capacite` int(11) NOT NULL,
  `autonomie` int(11) NOT NULL,
  `etat` varchar(100) NOT NULL
); ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS `centrale` (
`id_centrale` INTEGER PRIMARY KEY AUTOINCREMENT,
  `id_localisation` int(11) NOT NULL,
  `nom_centrale` varchar(100) NOT NULL
) ; ''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS `livreur` (
  `id_livreur` INTEGER PRIMARY KEY AUTOINCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `statut_livreur` varchar(100) NOT NULL,
  `id_camion` int(11) NOT NULL,
  `id_localisation` int(11) NOT NULL
); ''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS `localisation` (
`id_localisation` INTEGER PRIMARY KEY AUTOINCREMENT,
  `adresse` varchar(1000) NOT NULL,
  `code_postale` int(11) NOT NULL,
  `ville` varchar(100) NOT NULL
) ; ''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS `message` (
`id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `contenu` text NOT NULL,
  `date_envoie` date NOT NULL,
  `id_mission` int(11) NOT NULL,
  `id_livreur` int(11) NOT NULL,
  `id_centrale` int(11) NOT NULL
) ; ''')

cursor.execute('''

CREATE TABLE IF NOT EXISTS `mission` (
`id_message` INTEGER PRIMARY KEY AUTOINCREMENT,
  `etat` tinyint(1) NOT NULL,
  `details` text NOT NULL,
  `quantite` int(11) NOT NULL,
  `salaire` float NOT NULL,
  `date_envoie` date NOT NULL,
  `date_limite` date NOT NULL,
  `id_livreur` int(11) NOT NULL,
  `id_localisation` int(11) NOT NULL
)  ; ''')

conn.close()