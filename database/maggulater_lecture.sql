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
-- Table structure for table `maggulater_lecture`
--

DROP TABLE IF EXISTS `maggulater_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maggulater_lecture` (
  `Lecture_Id` int(11) NOT NULL AUTO_INCREMENT,
  `Link` varchar(100) NOT NULL,
  `Course_Id_id` int(11) NOT NULL,
  `Topic` varchar(100) NOT NULL,
  PRIMARY KEY (`Lecture_Id`),
  KEY `maggulater__Course_Id_id_5df06ec5_fk_maggulater_course_course_id` (`Course_Id_id`),
  CONSTRAINT `maggulater__Course_Id_id_5df06ec5_fk_maggulater_course_course_id` FOREIGN KEY (`Course_Id_id`) REFERENCES `maggulater_course` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maggulater_lecture`
--

LOCK TABLES `maggulater_lecture` WRITE;
/*!40000 ALTER TABLE `maggulater_lecture` DISABLE KEYS */;
INSERT INTO `maggulater_lecture` VALUES (1,'None',1,'SQL Queries'),(2,'None',1,'SQL Queries'),(3,'None',1,'SQL Queries'),(4,'None',1,'SQL Queries'),(5,'None',1,'SQL Queries'),(6,'None',1,'SQL Queries'),(7,'None',1,'SQL Queries');
/*!40000 ALTER TABLE `maggulater_lecture` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-08 12:22:58
