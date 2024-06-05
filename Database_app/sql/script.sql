-- MySQL dump 10.13  Distrib 8.0.32, for macos
--
-- Host: 127.0.0.1    Database: rocnikovka
-- ------------------------------------------------------
-- Server version	8.0.32

-- Tento skript obsahuje dump databáze `rocnikovka`, včetně vytvoření tabulek a vložení dat.

-- Nastavení a úpravy na začátku dumpu
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
# Uložení původního nastavení znakové sady klienta
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
# Uložení původního nastavení znakové sady výsledků
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
# Uložení původního nastavení kolace spojení
/*!50503 SET NAMES utf8 */;
# Nastavení znakové sady na utf8
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
# Uložení původního časového pásma
/*!40103 SET TIME_ZONE='+00:00' */;
# Nastavení časového pásma na UTC
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
# Zakázání kontrol jedinečnosti pro zvýšení rychlosti importu
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
# Zakázání kontrol cizích klíčů pro zvýšení rychlosti importu
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
# Nastavení SQL módu
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
# Zakázání SQL poznámek

-- Struktura tabulky `customer`
DROP TABLE IF EXISTS `customer`;
# Odstranění tabulky `customer`, pokud existuje
/*!40101 SET @saved_cs_client     = @@character_set_client */;
# Uložení aktuálního nastavení znakové sady klienta
/*!50503 SET character_set_client = utf8mb4 */;
# Nastavení znakové sady klienta na utf8mb4
CREATE TABLE `customer` (
                            `ID` int NOT NULL AUTO_INCREMENT,
                            `Name` varchar(255) NOT NULL,
                            `City` varchar(255) NOT NULL,
                            `CreditPoints` float NOT NULL,
                            `password` varchar(255) NOT NULL,
                            `email` varchar(255) DEFAULT NULL,
                            `telephone` varchar(250) DEFAULT NULL,
                            PRIMARY KEY (`ID`),
                            UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# Vytvoření tabulky `customer` se sloupci ID, Name, City, CreditPoints, password, email, telephone
# Nastavení primárního klíče na sloupec ID a unikátního klíče na sloupec email
/*!40101 SET character_set_client = @saved_cs_client */;
# Obnovení původního nastavení znakové sady klienta

-- Vložení dat do tabulky `customer`
LOCK TABLES `customer` WRITE;
# Uzamčení tabulky `customer` pro zápis
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
# Zakázání klíčů pro rychlejší import dat
INSERT INTO `customer` VALUES
                           (1,'dyntr','Praha',7587,'dyntr','dyntr@spsejecna.cz','+420 607 111 006'),
                           (2,'adam','adam',10000,'pablo','adam@spsejecna.com',NULL),
                           (3,'koblb','unknown',10000,'jouda','koblb@spsejecna.cz',NULL),
                           (4,'billy patrik','unknown',10000,'billy','billy@gmail.com',NULL),
                           (5,'mandik','unknown',6305,'mandik','manidk@spsejecna.cz','unknown'),
                           (6,'John Doe','New York',100,'password','john.doe@example.com',NULL);
# Vložení dat do tabulky `customer`
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
# Povolení klíčů
UNLOCK TABLES;
# Odemčení tabulky `customer`

-- Struktura tabulky `orderitem`
DROP TABLE IF EXISTS `orderitem`;
# Odstranění tabulky `orderitem`, pokud existuje
/*!40101 SET @saved_cs_client     = @@character_set_client */;
# Uložení aktuálního nastavení znakové sady klienta
/*!50503 SET character_set_client = utf8mb4 */;
# Nastavení znakové sady klienta na utf8mb4
CREATE TABLE `orderitem` (
                             `ID` int NOT NULL AUTO_INCREMENT,
                             `OrderID` int NOT NULL,
                             `ProductID` int NOT NULL,
                             `Quantity` int NOT NULL,
                             PRIMARY KEY (`ID`),
                             KEY `OrderID` (`OrderID`),
                             KEY `ProductID` (`ProductID`),
                             CONSTRAINT `orderitem_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `orders` (`ID`),
                             CONSTRAINT `orderitem_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# Vytvoření tabulky `orderitem` se sloupci ID, OrderID, ProductID, Quantity
# Nastavení primárního klíče na sloupec ID
# Nastavení cizích klíčů pro sloupce OrderID a ProductID
/*!40101 SET character_set_client = @saved_cs_client */;
# Obnovení původního nastavení znakové sady klienta

-- Vložení dat do tabulky `orderitem`
LOCK TABLES `orderitem` WRITE;
# Uzamčení tabulky `orderitem` pro zápis
/*!40000 ALTER TABLE `orderitem` DISABLE KEYS */;
# Zakázání klíčů pro rychlejší import dat
INSERT INTO `orderitem` VALUES
                            (2,1,14,1),
                            (3,2,1,5),
                            (4,3,1,5);
# Vložení dat do tabulky `orderitem`
/*!40000 ALTER TABLE `orderitem` ENABLE KEYS */;
# Povolení klíčů
UNLOCK TABLES;
# Odemčení tabulky `orderitem`

-- Struktura tabulky `orders`
DROP TABLE IF EXISTS `orders`;
# Odstranění tabulky `orders`, pokud existuje
/*!40101 SET @saved_cs_client     = @@character_set_client */;
# Uložení aktuálního nastavení znakové sady klienta
/*!50503 SET character_set_client = utf8mb4 */;
# Nastavení znakové sady klienta na utf8mb4
CREATE TABLE `orders` (
                          `ID` int NOT NULL AUTO_INCREMENT,
                          `CustomerID` int NOT NULL,
                          `OrderDate` datetime NOT NULL,
                          PRIMARY KEY (`ID`),
                          KEY `CustomerID` (`CustomerID`),
                          CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# Vytvoření tabulky `orders` se sloupci ID, CustomerID, OrderDate
# Nastavení primárního klíče na sloupec ID
# Nastavení cizího klíče pro sloupec CustomerID
/*!40101 SET character_set_client = @saved_cs_client */;
# Obnovení původního nastavení znakové sady klienta

-- Vložení dat do tabulky `orders`
LOCK TABLES `orders` WRITE;
# Uzamčení tabulky `orders` pro zápis
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
# Zakázání klíčů pro rychlejší import dat
INSERT INTO `orders` VALUES
                         (1,1,'2023-04-20 04:44:33'),
                         (2,1,'2022-01-01 00:00:00'),
                         (3,1,'2022-01-01 00:00:00');
# Vložení dat do tabulky `orders`
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
# Povolení klíčů
UNLOCK TABLES;
# Odemčení tabulky `orders`

-- Struktura tabulky `product`
DROP TABLE IF EXISTS `product`;
# Odstranění tabulky `product`, pokud existuje
/*!40101 SET @saved_cs_client     = @@character_set_client */;
# Uložení aktuálního nastavení znakové sady klienta
/*!50503 SET character_set_client = utf8mb4 */;
# Nastavení znakové sady klienta na utf8mb4
CREATE TABLE `product` (
                           `ID` int NOT NULL AUTO_INCREMENT,
                           `Name` varchar(255) NOT NULL,
                           `Type` enum('Food','Clothing','Furniture','Electronics','Cars','Gaming','Sport') NOT NULL,
                           `Price` float NOT NULL,
                           PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# Vytvoření tabulky `product` se sloupci ID, Name, Type, Price
# Nastavení primárního klíče na sloupec ID
/*!40101 SET character_set_client = @saved_cs_client */;
# Obnovení původního nastavení znakové sady klienta

-- Vložení dat do tabulky `product`
LOCK TABLES `product` WRITE;
# Uzamčení tabulky `product` pro zápis
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
# Zakázání klíčů pro rychlejší import dat
INSERT INTO `product` VALUES
                          (1,'Beef Burger','Food',63),
                          (2,'Pizza Margherita','Food',128),
                          (3,'Tomato Soup','Food',52),
                          (4,'Bread','Food',18),
                          (5,'Chicken Curry','Food',83),
                          (6,'Taco','Food',45),
                          (7,'Cheese Sandwich','Food',29),
                          (8,'Salmon Sushi Roll','Food',110),
                          (9,'Spaghetti Bolognese','Food',74),
                          (10,'Roast Beef','Food',105),
                          (11,'Chocolate Cake','Food',41),
                          (12,'Cotton T-Shirt','Clothing',207),
                          (13,'Leather Boots','Clothing',705),
                          (14,'Denim Jeans','Clothing',347),
                          (15,'Sunglasses','Clothing',248),
                          (16,'Sweatpants','Clothing',192),
                          (17,'Leather Jacket','Clothing',951),
                          (18,'Running Shoes','Clothing',399),
                          (19,'Swim Shorts','Clothing',134),
                          (20,'Winter Hat','Clothing',89),
                          (21,'Casual Shirt','Clothing',164),
                          (22,'Coffee Table','Furniture',3829),
                          (23,'Armchair','Furniture',2617),
                          (24,'Bookcase','Furniture',4737),
                          (25,'Dining Table','Furniture',5186),
                          (26,'Wardrobe','Furniture',8263),
                          (27,'Bedside Table','Furniture',1608),
                          (28,'Sofa','Furniture',5741),
                          (29,'Bean Bag Chair','Furniture',1679),
                          (30,'Ottoman','Furniture',2149),
                          (31,'TV Stand','Furniture',2547),
                          (32,'Smartphone','Electronics',14359),
                          (33,'Laptop','Electronics',19877),
                          (34,'Bluetooth Speaker','Electronics',2359),
                          (35,'Smart Watch','Electronics',9292),
                          (36,'Tablet','Electronics',8456),
                          (37,'Wireless Earbuds','Electronics',3267),
                          (38,'Gaming Mouse','Gaming',1204),
                          (39,'Gaming Keyboard','Gaming',1673),
                          (40,'Gaming Headset','Gaming',2579),
                          (41,'Gaming Chair','Gaming',4836),
                          (42,'Gaming Monitor','Gaming',6412),
                          (43,'PS5','Gaming',18399),
                          (44,'Xbox Series X','Gaming',18762),
                          (45,'Nintendo Switch','Gaming',9491),
                          (46,'Soccer Ball','Sport',476),
                          (47,'Basketball','Sport',803),
                          (48,'Tennis Racket','Sport',2279),
                          (49,'Running Shoes','Sport',1212),
                          (50,'Swim Goggles','Sport',605),
                          (51,'Dumbbells','Sport',3527),
                          (52,'Yoga Mat','Sport',820),
                          (53,'Resistance Bands','Sport',1474),
                          (54,'Jump Rope','Sport',409),
                          (55,'Exercise Bike','Sport',9903),
                          (56,'SUV','Cars',856052),
                          (57,'Sedan','Cars',735159),
                          (58,'Pickup Truck','Cars',999393),
                          (59,'Hatchback','Cars',531236),
                          (60,'Sports Car','Cars',2556200),
                          (61,'Convertible','Cars',1925640),
                          (62,'Minivan','Cars',600478),
                          (63,'Motorcycle','Cars',321124),
                          (64,'Electric Car','Cars',1237750);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
# Povolení klíčů
UNLOCK TABLES;
# Odemčení tabulky `product`

-- Struktura tabulky `transaction`
DROP TABLE IF EXISTS `transaction`;
# Odstranění tabulky `transaction`, pokud existuje
/*!40101 SET @saved_cs_client     = @@character_set_client */;
# Uložení aktuálního nastavení znakové sady klienta
/*!50503 SET character_set_client = utf8mb4 */;
# Nastavení znakové sady klienta na utf8mb4
CREATE TABLE `transaction` (
                               `ID` int NOT NULL AUTO_INCREMENT,
                               `CustomerID` int NOT NULL,
                               `Date` datetime NOT NULL,
                               `CreditPoints` float NOT NULL,
                               PRIMARY KEY (`ID`),
                               KEY `CustomerID` (`CustomerID`),
                               CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# Vytvoření tabulky `transaction` se sloupci ID, CustomerID, Date, CreditPoints
# Nastavení primárního klíče na sloupec ID
# Nastavení cizího klíče pro sloupec CustomerID
/*!40101 SET character_set_client = @saved_cs_client */;
# Obnovení původního nastavení znakové sady klienta

-- Vložení dat do tabulky `transaction`
LOCK TABLES `transaction` WRITE;
# Uzamčení tabulky `transaction` pro zápis
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
# Zakázání klíčů pro rychlejší import dat
INSERT INTO `transaction` VALUES
                              (2,1,'2023-04-20 04:44:33',-347),
                              (7,1,'2022-01-01 00:00:00',-315),
                              (8,1,'2022-01-01 00:00:00',-315);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
# Povolení klíčů
UNLOCK TABLES;
# Odemčení tabulky `transaction`

-- Obnovení původních nastavení
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
# Obnovení původního časového pásma

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
# Obnovení původního SQL módu
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
# Obnovení kontrol cizích klíčů
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
# Obnovení kontrol jedinečnosti
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
# Obnovení původního nastavení znakové sady klienta
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
# Obnovení původního nastavení znakové sady výsledků
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
# Obnovení původního nastavení kolace spojení
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
# Obnovení SQL poznámek

-- Dump completed on 2023-04-20  8:50:44
# Dokončení dumpu databáze
