-- --CREATE DATABASE  IF NOT EXISTS `proyecto_int` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto_int

-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `categorias`
--

--DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client ;*/
/*!40101 SET @saved_cs_client     = @@character_set_client ;*/
/*!50503 SET character_set_client = utf8mb4 ;
--CREATE TABLE `categorias` (
--   `id_cat` int NOT NULL AUTO_INCREMENT,
--   `nom_categoria` varchar(45) NOT NULL,
--   `foto` varchar(500) DEFAULT NULL,
--   PRIMARY KEY (`id_cat`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- /*!40101 SET character_set_client = @saved_cs_client ;*/

--
-- Dumping data for table `categorias`
--

-- LOCK TABLES `categorias` WRITE;
-- /*!40000 ALTER TABLE `categorias` DISABLE KEYS ;*/
-- INSERT INTO `categorias` VALUES (1,'Pinturas alba',NULL),(2,'Tersuave',NULL),(3,'Plavicon',NULL),(4,'Brochas',NULL),(5,'Rodillos',NULL);
-- /*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
-- UNLOCK TABLES;

-- --
-- -- Table structure for table `prod_cat`
-- --

-- DROP TABLE IF EXISTS `prod_cat`;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE `prod_cat` (
--   `idprod_cat` int NOT NULL AUTO_INCREMENT,
--   `id_cat` int DEFAULT NULL,
--   `id_producto` int DEFAULT NULL,
--   PRIMARY KEY (`idprod_cat`),
--   KEY `FK_cat_idx` (`id_cat`),
--   KEY `FK_prod_idx` (`id_producto`),
--   CONSTRAINT `FK_cat` FOREIGN KEY (`id_cat`) REFERENCES `categorias` (`id_cat`),
--   CONSTRAINT `FK_prod` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- /*!40101 SET character_set_client = @saved_cs_client */;

-- --
-- -- Dumping data for table `prod_cat`
-- --

-- LOCK TABLES `prod_cat` WRITE;
-- /*!40000 ALTER TABLE `prod_cat` DISABLE KEYS */;
-- INSERT INTO `prod_cat` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,2,7),(8,2,8),(9,2,9),(10,2,10),(11,3,11),(12,3,12),(13,3,13),(14,3,14),(15,3,15),(16,3,16),(17,4,17),(18,4,18),(19,4,19),(20,4,20),(21,5,21),(22,5,22),(23,5,23);
-- /*!40000 ALTER TABLE `prod_cat` ENABLE KEYS */;
-- UNLOCK TABLES;

-- --
-- -- Table structure for table `productos`
-- --

-- DROP TABLE IF EXISTS `productos`;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE `productos` (
--   `id_producto` int NOT NULL AUTO_INCREMENT,
--   `nombre` varchar(100) NOT NULL,
--   `precio` float NOT NULL,
--   PRIMARY KEY (`id_producto`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- /*!40101 SET character_set_client = @saved_cs_client */;

-- --
-- -- Dumping data for table `productos`
-- --

-- LOCK TABLES `productos` WRITE;
-- /*!40000 ALTER TABLE `productos` DISABLE KEYS */;
-- INSERT INTO `productos` VALUES (1,'albatex',5400),(2,'albalux',7900),(3,'satinol',6800),(4,'albalux exterior',9900),(5,'albacryl',10900),(6,'latex constructor',7800),(7,'linea arquitectonica',12000),(8,'Linea industrial',13499),(9,'Linea automotor',9999),(10,'Linea Diluyente',10000),(11,'Plavicon Fibrado',8000),(12,'P Fibrado XP',3000),(13,'P Sobre Chapa',9000),(14,'P Ladrillos XP',16000),(15,'P Frente XP',12300),(16,'L Silicona Solvente',2131),(17,'Brocha chata',600),(18,'Brocha simple',550),(19,'Brocha Dobles',1000),(20,'Brochas especiales',1230),(21,'Rodillo Simil Lana',400),(22,'Rodillo Cuero Lanar',890),(23,'Rodillos Polyester',980);
-- /*!40000 ALTER TABLE `productos` ENABLE KEYS */;
-- UNLOCK TABLES;
-- /*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

-- /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
-- /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
-- /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
-- /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
-- /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
-- /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- -- Dump completed on 2024-07-02 20:51:31
-- CREATE DATABASE pintureria;
-- esta ultima linea la comento porque cree en mi visual una base nueva solo con la tabla para ver si funcionaba