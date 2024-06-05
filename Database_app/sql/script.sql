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
(1, 'test', 'test', 10000, 'test', 'test@test.cz', '+420 123 456 789'),
(2, 'Veronica Lee', 'West Nathan', 18392, '6qlRxi8m*L', 'christopherfisher@morris.com', '334.649.1109'),
(3, 'Dan Bernard', 'South Danaton', 12402, ')Q7KuQHyM!', 'jessica76@gmail.com', '184-813-8029'),
(4, 'Jonathan Thomas', 'West Tara', 18264, '%1xt58Nrx@', 'ryansummers@hotmail.com', '+1-716-065-3465x0169'),
(5, 'Jonathon Hall', 'Saundersshire', 17000, '9E*6VfAsM(', 'williamcooper@yahoo.com', '245-208-1562'),
(6, 'Amy Hart', 'Jessicaland', 10151, '+N6)F_jE8N', 'gonzalessusan@hancock.com', '887-916-5353x70431'),
(7, 'Michael Russell', 'Tiffanymouth', 13717, 'rwm#D37)!0', 'salazarchelsea@atkins.com', '778.321.6855'),
(8, 'Amy Logan', 'New Michaelland', 15364, 'zUV!3Kjxrd', 'justin64@gmail.com', '(240)353-0214'),
(9, 'Jessica Long', 'Kiddchester', 19136, '#2Cf+tcAI5', 'shirleyrussell@yahoo.com', '+1-031-936-6765x5978'),
(10, 'Dawn Hill', 'New Brittneyborough', 12037, 'P+p38MqvHK', 'leonardgriffin@williams.biz', '623.688.7343x2980');
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
                         (1,1,'2024-06-01 04:44:33'),
                         (2,1,'2024-06-02 13:13:13'),
                         (3,1,'2024-06-03 12:12:12');
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
                          (1, 'Bread', 'Food', 35),
                          (2, 'Milk', 'Food', 20),
                          (3, 'Cheese', 'Food', 60),
                          (4, 'Apple', 'Food', 7),
                          (5, 'Banana', 'Food', 6),
                          (6, 'Orange', 'Food', 10),
                          (7, 'Yogurt', 'Food', 18),
                          (8, 'Chicken Breast', 'Food', 120),
                          (9, 'Beef Steak', 'Food', 240),
                          (10, 'Pasta', 'Food', 28),
                          (11, 'Rice', 'Food', 20),
                          (12, 'Butter', 'Food', 40),
                          (13, 'Eggs', 'Food', 48),
                          (14, 'Tomato', 'Food', 12),
                          (15, 'Potato', 'Food', 10),
                          (16, 'T-Shirt', 'Clothing', 250),
                          (17, 'Jeans', 'Clothing', 1000),
                          (18, 'Jacket', 'Clothing', 1500),
                          (19, 'Sneakers', 'Clothing', 1250),
                          (20, 'Hat', 'Clothing', 375),
                          (21, 'Scarf', 'Clothing', 300),
                          (22, 'Gloves', 'Clothing', 250),
                          (23, 'Socks', 'Clothing', 125),
                          (24, 'Dress', 'Clothing', 750),
                          (25, 'Suit', 'Clothing', 2500),
                          (26, 'Shorts', 'Clothing', 500),
                          (27, 'Sweater', 'Clothing', 625),
                          (28, 'Belt', 'Clothing', 375),
                          (29, 'Shoes', 'Clothing', 1750),
                          (30, 'Coat', 'Clothing', 2000),
                          (31, 'Sofa', 'Furniture', 12500),
                          (32, 'Table', 'Furniture', 3750),
                          (33, 'Chair', 'Furniture', 1250),
                          (34, 'Bed', 'Furniture', 7500),
                          (35, 'Wardrobe', 'Furniture', 5000),
                          (36, 'Bookshelf', 'Furniture', 3000),
                          (37, 'Coffee Table', 'Furniture', 2000),
                          (38, 'Desk', 'Furniture', 3250),
                          (39, 'Dining Set', 'Furniture', 15000),
                          (40, 'Recliner', 'Furniture', 6250),
                          (41, 'Nightstand', 'Furniture', 1750),
                          (42, 'Dresser', 'Furniture', 4500),
                          (43, 'Armchair', 'Furniture', 3750),
                          (44, 'TV Stand', 'Furniture', 2500),
                          (45, 'Cabinet', 'Furniture', 5500),
                          (46, 'Smartphone', 'Electronics', 15000),
                          (47, 'Laptop', 'Electronics', 30000),
                          (48, 'TV', 'Electronics', 20000),
                          (49, 'Headphones', 'Electronics', 3750),
                          (50, 'Camera', 'Electronics', 17500),
                          (51, 'Smartwatch', 'Electronics', 5000),
                          (52, 'Tablet', 'Electronics', 10000),
                          (53, 'Printer', 'Electronics', 2500),
                          (54, 'Monitor', 'Electronics', 6250),
                          (55, 'Keyboard', 'Electronics', 2000),
                          (56, 'Mouse', 'Electronics', 1250),
                          (57, 'Router', 'Electronics', 2250),
                          (58, 'Speakers', 'Electronics', 3000),
                          (59, 'External HDD', 'Electronics', 2500),
                          (60, 'Game Console', 'Electronics', 12500),
                          (61, 'Sedan', 'Cars', 500000),
                          (62, 'SUV', 'Cars', 750000),
                          (63, 'Hatchback', 'Cars', 375000),
                          (64, 'Convertible', 'Cars', 875000),
                          (65, 'Coupe', 'Cars', 625000),
                          (66, 'Minivan', 'Cars', 700000),
                          (67, 'Pickup Truck', 'Cars', 1000000),
                          (68, 'Luxury Sedan', 'Cars', 1250000),
                          (69, 'Sports Car', 'Cars', 1500000),
                          (70, 'Electric Car', 'Cars', 875000),
                          (71, 'Hybrid Car', 'Cars', 750000),
                          (72, 'Compact Car', 'Cars', 450000),
                          (73, 'Diesel Truck', 'Cars', 1125000),
                          (74, 'Motorcycle', 'Cars', 250000),
                          (75, 'Electric Scooter', 'Cars', 50000),
                          (76, 'Gaming PC', 'Gaming', 37500),
                          (77, 'Gaming Laptop', 'Gaming', 30000),
                          (78, 'Gaming Monitor', 'Gaming', 7500),
                          (79, 'Gaming Mouse', 'Gaming', 1500),
                          (80, 'Gaming Keyboard', 'Gaming', 2500),
                          (81, 'VR Headset', 'Gaming', 10000),
                          (82, 'Gaming Chair', 'Gaming', 6250),
                          (83, 'Game Console', 'Gaming', 12500),
                          (84, 'Gaming Headset', 'Gaming', 3750),
                          (85, 'Graphics Card', 'Gaming', 17500),
                          (86, 'Gaming Desk', 'Gaming', 5000),
                          (87, 'Game Controller', 'Gaming', 1250),
                          (88, 'Gaming Mousepad', 'Gaming', 750),
                          (89, 'Gaming Speakers', 'Gaming', 2500),
                          (90, 'Streaming Kit', 'Gaming', 5000),
                          (91, 'Basketball', 'Sport', 750),
                          (92, 'Soccer Ball', 'Sport', 625),
                          (93, 'Tennis Racket', 'Sport', 2000),
                          (94, 'Running Shoes', 'Sport', 3000),
                          (95, 'Fitness Tracker', 'Sport', 3750),
                          (96, 'Yoga Mat', 'Sport', 625),
                          (97, 'Dumbbells', 'Sport', 1250),
                          (98, 'Bicycle', 'Sport', 7500),
                          (99, 'Helmet', 'Sport', 1500),
                          (100, 'Backpack', 'Sport', 1000),
                          (101, 'Sportswear', 'Sport', 1750),
                          (102, 'Swimwear', 'Sport', 1250),
                          (103, 'Tennis Balls', 'Sport', 375),
                          (104, 'Golf Clubs', 'Sport', 10000),
                          (105, 'Boxing Gloves', 'Sport', 1500);
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
                              (2,1,'2024-04-20 04:44:33',-347),
                              (7,1,'2024-01-01 00:00:00',-315),
                              (8,1,'2024-01-01 00:00:00',-315);
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
