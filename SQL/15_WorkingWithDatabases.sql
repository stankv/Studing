-- 15.7. Задание
-- Создайте в новой базе таблицу Territories со структурой, аналогичной структуре таблицы Territories из учебной базы. 
-- Добавьте в неё и таблицу Region несколько значений так, чтобы они оказались связаны друг с другом через FK. 

CREATE DATABASE MyTest;
USE MyTest;
CREATE TABLE Region ( 
    RegionID int NOT NULL, 
    RegionDescription nchar(50) NOT NULL ); 
ALTER TABLE Region ADD Help nchar(16);
CREATE TABLE Territories (
	TerritoryID nvarchar(20) NOT NULL,
	TerritoryDescription nchar(50) NOT NULL,
	RegionID int  NOT NULL);
INSERT INTO Region (RegionID, RegionDescription) VALUES 
    (1,'Eastern'), (2,'Western'), (3,'Norethern'), (4,'Southern');
INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID) VALUES
    ('01581','Westboro',1), ('60601','Chicago',2),('03049','Hollis',3),('29202','Columbia',4);
-- Связи между таблицами созданы с помощью "Диаграммы баз данных" как описано в 
-- https://www.bestprog.net/ru/2017/07/04/creating-a-one-to-many-relationship-between-tables-in-a-microsoft-sql-server-database_ru/#p04_3