-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: goldapp
-- ------------------------------------------------------
-- Server version	8.0.27

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

CREATE DATABASE IF NOT EXISTS goldapp;
USE goldapp;

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(90) COLLATE utf8_esperanto_ci NOT NULL,
  `address_line` varchar(75) COLLATE utf8_esperanto_ci NOT NULL,
  `city` varchar(70) COLLATE utf8_esperanto_ci NOT NULL,
  `zipcode` varchar(45) COLLATE utf8_esperanto_ci NOT NULL,
  `country` varchar(55) COLLATE utf8_esperanto_ci NOT NULL,
  `information` mediumtext COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
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
  `name` varchar(90) COLLATE utf8_esperanto_ci NOT NULL,
  `description` mediumtext COLLATE utf8_esperanto_ci NOT NULL,
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
  `heading` varchar(70) COLLATE utf8_esperanto_ci NOT NULL COMMENT 'Name or a heading',
  `phone` int NOT NULL,
  `type` varchar(45) COLLATE utf8_esperanto_ci NOT NULL,
  `category` enum('general','mentalHelp') COLLATE utf8_esperanto_ci NOT NULL COMMENT 'Only 2 types (mental health or just helpful such as volunteers information etc.)',
  `description` mediumtext COLLATE utf8_esperanto_ci NOT NULL,
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
  `interest` varchar(90) COLLATE utf8_esperanto_ci NOT NULL,
  PRIMARY KEY (`interest_id`),
  UNIQUE KEY `interest_UNIQUE` (`interest`),
  UNIQUE KEY `interest_id_UNIQUE` (`interest_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest`
--

LOCK TABLES `interest` WRITE;
/*!40000 ALTER TABLE `interest` DISABLE KEYS */;
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
  `place` varchar(100) COLLATE utf8_esperanto_ci NOT NULL,
  `user_user_id` int NOT NULL,
  PRIMARY KEY (`location_id`),
  KEY `fk_location_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_location_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
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
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `login_id` int NOT NULL AUTO_INCREMENT,
  `pwd` varchar(90) COLLATE utf8_esperanto_ci NOT NULL COMMENT 'Password hash\nShould be like 60 characters...',
  `email` varchar(90) COLLATE utf8_esperanto_ci NOT NULL,
  `secret_question` varchar(255) COLLATE utf8_esperanto_ci NOT NULL,
  `secret_answer` varchar(45) COLLATE utf8_esperanto_ci NOT NULL,
  `user_user_id` int NOT NULL,
  PRIMARY KEY (`login_id`),
  UNIQUE KEY `password_UNIQUE` (`pwd`),
  UNIQUE KEY `login_id_UNIQUE` (`login_id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_login_user_idx` (`user_user_id`),
  CONSTRAINT `fk_login_user` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(30) COLLATE utf8_esperanto_ci NOT NULL,
  `lname` varchar(30) COLLATE utf8_esperanto_ci DEFAULT NULL,
  `username` varchar(45) COLLATE utf8_esperanto_ci NOT NULL,
  `phone` int DEFAULT NULL,
  `facebook_connect` varchar(45) COLLATE utf8_esperanto_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `phone_UNIQUE` (`phone`),
  UNIQUE KEY `facebook_connect_UNIQUE` (`facebook_connect`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_has_group`
--

DROP TABLE IF EXISTS `user_has_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_has_group` (
  `user_user_id` int NOT NULL,
  `group_group_id` int NOT NULL,
  PRIMARY KEY (`user_user_id`,`group_group_id`),
  KEY `fk_user_has_group_group1_idx` (`group_group_id`),
  KEY `fk_user_has_group_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_user_has_group_group1` FOREIGN KEY (`group_group_id`) REFERENCES `group` (`group_id`),
  CONSTRAINT `fk_user_has_group_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`)
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
  `user_user_id` int NOT NULL,
  `interest_interest_id` int NOT NULL,
  PRIMARY KEY (`user_user_id`,`interest_interest_id`),
  KEY `fk_user_has_interest_interest1_idx` (`interest_interest_id`),
  KEY `fk_user_has_interest_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_user_has_interest_interest1` FOREIGN KEY (`interest_interest_id`) REFERENCES `interest` (`interest_id`),
  CONSTRAINT `fk_user_has_interest_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_esperanto_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_interest`
--

LOCK TABLES `user_has_interest` WRITE;
/*!40000 ALTER TABLE `user_has_interest` DISABLE KEYS */;
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

-- Dump completed on 2022-04-25 15:13:26