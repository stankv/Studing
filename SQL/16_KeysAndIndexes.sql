-- Задание. Добавьте подходящие индексы для таблиц тестовой базы, созданной в предыдущем занятии. 

CREATE DATABASE MyTest;
USE MyTest;
CREATE TABLE Region ( 
    RegionID int IDENTITY(1,1) PRIMARY KEY,
    RegionDescription nchar(50) NOT NULL ); 
ALTER TABLE Region ADD Help nchar(16);
CREATE CLUSTERED INDEX idxRegionID ON Region (RegionID);
CREATE TABLE Territories (
	TerritoryID nvarchar(20) NOT NULL,
	TerritoryDescription nchar(50) NOT NULL,
	RegionID int  NOT NULL);
CREATE INDEX idxTerritoryID ON Territories (TerritoryID);