CREATE DATABASE  IF NOT EXISTS `goldapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `goldapp`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: goldapp
-- ------------------------------------------------------
-- Server version	8.0.27
DROP DATABASE goldapp;
CREATE DATABASE goldapp;
USE goldapp;



/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(90) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `address_line` varchar(75) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `city` varchar(70) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `zipcode` varchar(45) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `country` varchar(55) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `information` mediumtext CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `interest_interest_id` int NOT NULL,
  `eventdate` date DEFAULT NULL,
  `eventtime` time DEFAULT NULL,
  PRIMARY KEY (`event_id`),
  KEY `fk_event_interest1_idx` (`interest_interest_id`),
  CONSTRAINT `fk_event_interest1` FOREIGN KEY (`interest_interest_id`) REFERENCES `interest` (`interest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (1,'Baking Competition','Main St 50','Stockholm','90002','Sweden','Come for a bake off',7,'2022-05-09','15:00:00'),(2,'Boys Chess Tour','Allee 35','Malmo','80001','Sweden','Nice day at the park for a chess with the boys',4,'2022-08-16','13:00:00'),(3,'Art Class with Class of Wine','Edgarmar ST 100','Stockholm','90002','Sweden','Nice and cozy Saturday with some painting and wine',5,'2022-09-03','14:00:00');
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group`
--

DROP TABLE IF EXISTS `group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group` (
  `group_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(90) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `description` mediumtext CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`group_id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group`
--

LOCK TABLES `group` WRITE;
/*!40000 ALTER TABLE `group` DISABLE KEYS */;
/*!40000 ALTER TABLE `group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info` (
  `info_id` int NOT NULL AUTO_INCREMENT,
  `heading` varchar(70) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL COMMENT 'Name or a heading',
  `phone` int NOT NULL,
  `type` varchar(45) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `category` enum('general','mentalHelp') CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL COMMENT 'Only 2 types (mental health or just helpful such as volunteers information etc.)',
  `description` mediumtext CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`info_id`),
  UNIQUE KEY `info_id_UNIQUE` (`info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interest`
--

DROP TABLE IF EXISTS `interest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interest` (
  `interest_id` int NOT NULL AUTO_INCREMENT,
  `interest` varchar(90) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `image_path` varchar(1024) CHARACTER SET utf8 COLLATE utf8_esperanto_ci DEFAULT NULL,
  PRIMARY KEY (`interest_id`),
  UNIQUE KEY `interest_UNIQUE` (`interest`),
  UNIQUE KEY `interest_id_UNIQUE` (`interest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest`
--

LOCK TABLES `interest` WRITE;
/*!40000 ALTER TABLE `interest` DISABLE KEYS */;
INSERT INTO `interest` VALUES (1,'Fishing','\\fishing.jpg'),(2,'Cooking','cooking.jpg'),(3,'Cinema/Theater','cinema.jpg'),(4,'Chess','chess.jpg'),(5,'Art','art.jpg'),(6,'Music','music.jpg'),(7,'Baking','baking.jpg'),(8,'Hunting','hunting.jpg'),(9,'Taking walks','walk.jpg');
/*!40000 ALTER TABLE `interest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `place` varchar(100) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Skåne'),(2,'Stockholm'),(3,'Kristianstad');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_has_event`
--

DROP TABLE IF EXISTS `location_has_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location_has_event` (
  `location_location_id` int NOT NULL,
  `event_event_id` int NOT NULL,
  PRIMARY KEY (`location_location_id`,`event_event_id`),
  KEY `fk_location_has_event_event1_idx` (`event_event_id`),
  KEY `fk_location_has_event_location1_idx` (`location_location_id`),
  CONSTRAINT `fk_location_has_event_event1` FOREIGN KEY (`event_event_id`) REFERENCES `event` (`event_id`),
  CONSTRAINT `fk_location_has_event_location1` FOREIGN KEY (`location_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_has_event`
--

LOCK TABLES `location_has_event` WRITE;
/*!40000 ALTER TABLE `location_has_event` DISABLE KEYS */;
INSERT INTO `location_has_event` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `location_has_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location_has_info`
--

DROP TABLE IF EXISTS `location_has_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location_has_info` (
  `location_location_id` int NOT NULL,
  `info_info_id` int NOT NULL,
  PRIMARY KEY (`location_location_id`,`info_info_id`),
  KEY `fk_location_has_info_info1_idx` (`info_info_id`),
  KEY `fk_location_has_info_location1_idx` (`location_location_id`),
  CONSTRAINT `fk_location_has_info_info1` FOREIGN KEY (`info_info_id`) REFERENCES `info` (`info_id`),
  CONSTRAINT `fk_location_has_info_location1` FOREIGN KEY (`location_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location_has_info`
--

LOCK TABLES `location_has_info` WRITE;
/*!40000 ALTER TABLE `location_has_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `location_has_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `email` varchar(90) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `fname` varchar(30) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `lname` varchar(30) CHARACTER SET utf8 COLLATE utf8_esperanto_ci DEFAULT NULL,
  `username` varchar(45) CHARACTER SET utf8 COLLATE utf8_esperanto_ci DEFAULT NULL,
  `pwd` varchar(120) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  `phone` int DEFAULT NULL,
  `facebook_connect` varchar(45) CHARACTER SET utf8 COLLATE utf8_esperanto_ci DEFAULT NULL,
  `location_location_id` int DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `phone_UNIQUE` (`phone`),
  UNIQUE KEY `facebook_connect_UNIQUE` (`facebook_connect`),
  KEY `fk_user_location1_idx` (`location_location_id`),
  CONSTRAINT `fk_user_location1` FOREIGN KEY (`location_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('example@gmail.com','first','last',NULL,'gAAAAABiamwmZQTndgruoTKynqxMlupWEZNnX325vZ4lUqxGyX29PlffwQSA1YqGs3D9vTBqG1h_6aFjmuuDaHyTaezUIQFDNw==',10101010,NULL,2);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_has_group`
--

DROP TABLE IF EXISTS `user_has_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_has_group` (
  `group_group_id` int NOT NULL,
  `user_email` varchar(90) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`group_group_id`,`user_email`),
  KEY `fk_user_has_group_group1_idx` (`group_group_id`),
  KEY `fk_user_has_group_user1_idx` (`user_email`),
  CONSTRAINT `fk_user_has_group_group1` FOREIGN KEY (`group_group_id`) REFERENCES `group` (`group_id`),
  CONSTRAINT `fk_user_has_group_user1` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_group`
--

LOCK TABLES `user_has_group` WRITE;
/*!40000 ALTER TABLE `user_has_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_has_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_has_interest`
--

DROP TABLE IF EXISTS `user_has_interest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_has_interest` (
  `interest_interest_id` int NOT NULL,
  `user_email` varchar(90) CHARACTER SET utf8 COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`interest_interest_id`,`user_email`),
  KEY `fk_user_has_interest_interest1_idx` (`interest_interest_id`),
  KEY `fk_user_has_interest_user1_idx1` (`user_email`),
  CONSTRAINT `fk_user_has_interest_interest1` FOREIGN KEY (`interest_interest_id`) REFERENCES `interest` (`interest_id`),
  CONSTRAINT `fk_user_has_interest_user1` FOREIGN KEY (`user_email`) REFERENCES `user` (`email`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_interest`
--

LOCK TABLES `user_has_interest` WRITE;
/*!40000 ALTER TABLE `user_has_interest` DISABLE KEYS */;
INSERT INTO `user_has_interest` VALUES (4,'example@gmail.com'),(5,'example@gmail.com'),(7,'example@gmail.com');
/*!40000 ALTER TABLE `user_has_interest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 10:53:52
