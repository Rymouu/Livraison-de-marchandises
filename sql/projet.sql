-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mar 27 Février 2024 à 16:28
-- Version du serveur :  5.6.20-log
-- Version de PHP :  5.4.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `projet`
--

-- --------------------------------------------------------

--
-- Structure de la table `camion`
--

CREATE TABLE IF NOT EXISTS `camion` (
`id_camion` int(11) NOT NULL,
  `capacité` int(11) NOT NULL,
  `autonomie` int(11) NOT NULL,
  `etat` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `centrale`
--

CREATE TABLE IF NOT EXISTS `centrale` (
`id_centrale` int(11) NOT NULL,
  `id_localisation` int(11) NOT NULL,
  `nom_centrale` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `livreur`
--

CREATE TABLE IF NOT EXISTS `livreur` (
  `id_livreur` int(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `statut_livreur` varchar(100) NOT NULL,
  `id_camion` int(11) NOT NULL,
  `id_localisation` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `localisation`
--

CREATE TABLE IF NOT EXISTS `localisation` (
`id_localisation` int(11) NOT NULL,
  `adresse` varchar(1000) NOT NULL,
  `code_postale` int(11) NOT NULL,
  `ville` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `message`
--

CREATE TABLE IF NOT EXISTS `message` (
`id` int(11) NOT NULL,
  `contenu` text NOT NULL,
  `date_envoie` date NOT NULL,
  `id_mission` int(11) NOT NULL,
  `id_livreur` int(11) NOT NULL,
  `id_centrale` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Structure de la table `mission`
--

CREATE TABLE IF NOT EXISTS `mission` (
`id_message` int(11) NOT NULL,
  `etat` tinyint(1) NOT NULL,
  `details` text NOT NULL,
  `quantite` int(11) NOT NULL,
  `salaire` float NOT NULL,
  `date_envoie` date NOT NULL,
  `date_limite` date NOT NULL,
  `id_livreur` int(11) NOT NULL,
  `id_localisation` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `camion`
--
ALTER TABLE `camion`
 ADD PRIMARY KEY (`id_camion`);

--
-- Index pour la table `centrale`
--
ALTER TABLE `centrale`
 ADD PRIMARY KEY (`id_centrale`);

--
-- Index pour la table `localisation`
--
ALTER TABLE `localisation`
 ADD PRIMARY KEY (`id_localisation`);

--
-- Index pour la table `message`
--
ALTER TABLE `message`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `mission`
--
ALTER TABLE `mission`
 ADD PRIMARY KEY (`id_message`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `camion`
--
ALTER TABLE `camion`
MODIFY `id_camion` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `centrale`
--
ALTER TABLE `centrale`
MODIFY `id_centrale` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `localisation`
--
ALTER TABLE `localisation`
MODIFY `id_localisation` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `message`
--
ALTER TABLE `message`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `mission`
--
ALTER TABLE `mission`
MODIFY `id_message` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
