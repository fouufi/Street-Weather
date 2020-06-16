-- --------------------------------------------------------
-- Hôte :                        localhost
-- Version du serveur:           10.4.12-MariaDB - mariadb.org binary distribution
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Listage de la structure de la base pour streetweather
CREATE DATABASE IF NOT EXISTS `streetweather` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `streetweather`;

-- Listage de la structure de la table streetweather. meteo
CREATE TABLE IF NOT EXISTS `meteo` (
  `ID_Temps` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Temps` text DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `Temperature` float DEFAULT NULL,
  `Temp_Ressentie` float DEFAULT NULL,
  `Humidite` float DEFAULT NULL,
  `Nuages` float DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `ID_Ville` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`ID_Temps`),
  KEY `ID_Ville` (`ID_Ville`),
  CONSTRAINT `Meteo_ibfk_1` FOREIGN KEY (`ID_Ville`) REFERENCES `ville` (`ID_Ville`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de la table streetweather. pays
CREATE TABLE IF NOT EXISTS `pays` (
  `ID_Pays` int(10) unsigned NOT NULL,
  `Pays` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Pays`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de la table streetweather. ville
CREATE TABLE IF NOT EXISTS `ville` (
  `ID_Ville` int(10) unsigned NOT NULL,
  `Ville` varchar(50) DEFAULT NULL,
  `ID_Pays` int(10) unsigned NOT NULL,
  PRIMARY KEY (`ID_Ville`),
  KEY `ID_Pays` (`ID_Pays`),
  CONSTRAINT `Ville_ibfk_1` FOREIGN KEY (`ID_Pays`) REFERENCES `pays` (`ID_Pays`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Les données exportées n'étaient pas sélectionnées.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
