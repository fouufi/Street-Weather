-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: streetweather
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `meteo`
--

DROP TABLE IF EXISTS `meteo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meteo` (
  `ID_Temps` int unsigned NOT NULL AUTO_INCREMENT,
  `Temps` text,
  `Description` text,
  `Temperature` float DEFAULT NULL,
  `Temp_Ressentie` float DEFAULT NULL,
  `Humidite` float DEFAULT NULL,
  `Nuages` float DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `ID_Ville` int unsigned DEFAULT NULL,
  PRIMARY KEY (`ID_Temps`),
  KEY `ID_Ville` (`ID_Ville`),
  CONSTRAINT `Meteo_ibfk_1` FOREIGN KEY (`ID_Ville`) REFERENCES `ville` (`ID_Ville`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meteo`
--

LOCK TABLES `meteo` WRITE;
/*!40000 ALTER TABLE `meteo` DISABLE KEYS */;
INSERT INTO `meteo` VALUES (34,'Clouds','Few clouds',18.3,15.05,63,20,'2020-06-16 20:22:49',1),(35,'Clouds','Few clouds',17,15.2,62,21,'2020-06-17 12:22:49',1),(36,'Clouds','Few clouds',16,12.2,62,21,'2020-06-17 12:44:49',1),(37,'Clouds','Few clouds',15,13.2,62,21,'2020-06-17 14:24:49',1),(38,'Clouds','Few clouds',14,13.2,62,21,'2020-06-17 14:45:49',1),(39,'Clouds','Few clouds',14.3,13.1,62,21,'2020-06-17 14:55:49',1),(40,'Clouds','Few clouds',14.2,13,62,21,'2020-06-17 14:55:49',1),(41,'Clouds','Few clouds',14.1,13,62,21,'2020-06-17 14:55:49',1),(42,'Clouds','Few clouds',14.2,13,62,21,'2020-06-17 14:55:49',2),(43,'Clouds','Few clouds',16.3,14,62,21,'2020-06-17 14:00:49',2),(44,'Clouds','Few clouds',16,13.8,62,21,'2020-06-17 13:20:49',2),(45,'Clouds','Few clouds',14,13.2,62,21,'2020-06-17 12:20:49',2);
/*!40000 ALTER TABLE `meteo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pays`
--

DROP TABLE IF EXISTS `pays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pays` (
  `ID_Pays` int unsigned NOT NULL AUTO_INCREMENT,
  `Pays` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID_Pays`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pays`
--

LOCK TABLES `pays` WRITE;
/*!40000 ALTER TABLE `pays` DISABLE KEYS */;
INSERT INTO `pays` VALUES (1,'FR'),(2,'UK'),(3,'USA'),(4,'GE'),(5,'BE'),(6,'NI');
/*!40000 ALTER TABLE `pays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ville`
--

DROP TABLE IF EXISTS `ville`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ville` (
  `ID_Ville` int unsigned NOT NULL,
  `Ville` varchar(50) DEFAULT NULL,
  `ID_Pays` int unsigned NOT NULL,
  PRIMARY KEY (`ID_Ville`),
  KEY `ID_Pays` (`ID_Pays`),
  CONSTRAINT `Ville_ibfk_1` FOREIGN KEY (`ID_Pays`) REFERENCES `pays` (`ID_Pays`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ville`
--

LOCK TABLES `ville` WRITE;
/*!40000 ALTER TABLE `ville` DISABLE KEYS */;
INSERT INTO `ville` VALUES (1,'Nantes',1),(2,'Laval',1),(3,'Paris',1),(4,'Rennes',1),(5,'Lilles',1),(6,'Strasbourg',1),(7,'Brest',1),(8,'Nice',1),(9,'Toulouse',1),(10,'Perpignan',1),(11,'Izé',1),(12,'Bais',1),(13,'Londres',2),(14,'Manchester',2),(15,'Bristol',2),(16,'Birmingham',2),(17,'Oxford',2),(18,'Liverpool',2),(19,'Cambridge',2),(20,'New York',3),(21,'Washington',3),(22,'Boston',3),(23,'Las Vegas',3),(24,'Los Angeles',3),(25,'Seattle',3),(26,'San Francisco',3),(27,'Miami',3),(28,'Chicago',3);
/*!40000 ALTER TABLE `ville` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-17 14:55:47
