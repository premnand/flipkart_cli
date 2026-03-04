-- Run this once before starting app.py

CREATE DATABASE IF NOT EXISTS `hit-db-demo`;
USE `hit-db-demo`;

CREATE TABLE IF NOT EXISTS users (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    name     VARCHAR(50)  NOT NULL,
    email    VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);
