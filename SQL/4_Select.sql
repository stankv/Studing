-- 4.3. Задания

-- 4.3.1. Найдите всех пользователей (Customers), фамилия контактной персоны которых (ContactName) начинается с C.
SELECT * FROM Customers WHERE ContactName LIKE '% C%';

/* 4.3.2. Найдите все заказы, плата за груз у которых (Freight) лежит в диапазоне от 100 до 200, а 
страна-поставщик ShipCountry -- либо USA, либо France.  */
SELECT * FROM Orders WHERE Freight BETWEEN 100 AND 200 AND ShipCountry IN ('USA', 'France');

/* 4.3.3. Отфильтруйте таблицу EmployeeTerritories, задающую отношение многие-ко-многим между сотрудниками 
и территориальными подразделениями, так, чтобы значение связующего поля TerritoryID находилось в 
промежутке от 6897 до 31000. */
SELECT * FROM EmployeeTerritories WHERE TerritoryID BETWEEN 6897 AND 31000;