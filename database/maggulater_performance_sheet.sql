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
-- Table structure for table `maggulater_performance_sheet`
--

DROP TABLE IF EXISTS `maggulater_performance_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maggulater_performance_sheet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Test_Id_id` int(11) NOT NULL,
  `Student_Id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Test_Id_id` (`Test_Id_id`),
  UNIQUE KEY `Student_Id_id` (`Student_Id_id`),
  CONSTRAINT `maggu_Student_Id_id_172bf027_fk_maggulater_student_Student_Id_id` FOREIGN KEY (`Student_Id_id`) REFERENCES `maggulater_student` (`Student_Id_id`),
  CONSTRAINT `maggulater_perfor_Test_Id_id_f422b1c3_fk_maggulater_test_Test_Id` FOREIGN KEY (`Test_Id_id`) REFERENCES `maggulater_test` (`Test_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maggulater_performance_sheet`
--

LOCK TABLES `maggulater_performance_sheet` WRITE;
/*!40000 ALTER TABLE `maggulater_performance_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `maggulater_performance_sheet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-03-08 12:23:02
