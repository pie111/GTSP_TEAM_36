-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 06, 2022 at 05:19 AM
-- Server version: 10.5.12-MariaDB-cll-lve
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `u934542817_EmergencyVec`
--

-- --------------------------------------------------------

--
-- Table structure for table `Camera_Collections`
--

CREATE TABLE `Camera_Collections` (
  `ID` int(11) NOT NULL,
  `Latitude` double NOT NULL,
  `Longitude` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Camera_Collections`
--

INSERT INTO `Camera_Collections` (`ID`, `Latitude`, `Longitude`) VALUES
(1, 53.32055555555556, -1.7297222222222222),
(2, 53.31861111111111, -1.6997222222222224),
(3, 10.0241605, 76.3539327),
(4, 10.0166142, 76.3252825),
(5, 11.0241605, 76.3539327),
(6, 13.0166142, 76.3652825),
(7, 10.0166143, 76.3252823);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Camera_Collections`
--
ALTER TABLE `Camera_Collections`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Camera_Collections`
--
ALTER TABLE `Camera_Collections`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
