-- create_database.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS FinVitality;

-- Use the database
USE FinVitality;

-- Create the user and grant privileges
CREATE USER IF NOT EXISTS 'FinVitality'@'localhost' IDENTIFIED BY 'Portfolio_101877';
GRANT ALL PRIVILEGES ON FinVitality.* TO 'FinVitality'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
