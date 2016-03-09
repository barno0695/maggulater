-- MySQL dump 10.13  Distrib 5.5.47, for debian-linux-gnu (i686)
--
-- Host: 10.5.18.68    Database: 13CS30009
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `maggulater_myuser`
--

DROP TABLE IF EXISTS `maggulater_myuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maggulater_myuser` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `link_to_dp` varchar(100) NOT NULL,
  `type_flag` int(11) NOT NULL,
  `dob` date NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maggulater_myuser`
--

LOCK TABLES `maggulater_myuser` WRITE;
/*!40000 ALTER TABLE `maggulater_myuser` DISABLE KEYS */;
INSERT INTO `maggulater_myuser` VALUES (1,'test','test@gmail.com','link',1,'1900-01-01','test'),(2,'t','t@gmail.com','link',1,'1900-01-01','test'),(3,'shubham','shubham.agrawal.0473@gmail.com','link',1,'2016-03-08','shubham123'),(4,'shubham','shubham@gmail.com','link',1,'2016-03-23','6a95c0df38e54945180f4d5e66b69b86'),(6,'dummy','dummy@gmail.com','link',1,'2016-03-15','900150983cd24fb0d6963f7d28e17f72'),(7,'abc','abc@gmail.com','link',1,'1900-01-01','900150983cd24fb0d6963f7d28e17f72'),(8,'aaa','aaa@gmail.com','link',1,'1900-01-01','47bce5c74f589f4867dbd57e9ca9f808'),(9,'aaaa','aaaa@gmail.com','link',1,'1900-01-01','74b87337454200d4d33f80c4663dc5e5'),(14,'NewStudent','st@student.com','link',1,'2012-01-01','ad6a280417a0f533d8b670c61667e1a0'),(16,'alpha','aplha@gmail.com','link',2,'2015-11-30','f3ede926587776a8cd79fb2afe4e07b4'),(17,'beta','beta@gmail.com','link',2,'2015-11-30','f3ede926587776a8cd79fb2afe4e07b4'),(18,'gamma','gamma@gmail.com','link',2,'2015-11-30','f3ede926587776a8cd79fb2afe4e07b4'),(19,'Barno','barno@barno.com','link',1,'1900-01-01','1cfa9a86513c5756ce05e6d12b9379b5'),(20,'barno Fac','faculty@faculty.com','link',2,'1900-01-01','85b954cf9565b9c54add85f09281a50b'),(21,'Vadde','vaddesantosh96@gmail.com','link',1,'2015-11-30','f3ede926587776a8cd79fb2afe4e07b4');
/*!40000 ALTER TABLE `maggulater_myuser` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-08 12:22:49
