-- 11.5. Задания

-- 11.5.1. Отберите с помощью LEFT JOIN все записи из таблицы Customers, для которых FK-ключ таблицы Orders пустой.
SELECT Customers.*, Orders.CustomerID FROM Customers 
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID AND Orders.CustomerID IS NULL
ORDER BY Customers.CompanyName; 

/* 11.5.2. Выведите конкретную информацию по всем пользователям Customers и поставщикам Suppliers - имя контактной 
персоны, город и страну, а также идентификацию группы (пользователь или поставщик). */
SELECT 'Customer' As Type, ContactName, City, Country FROM Customers 
WHERE Country='USA' 
UNION 
SELECT 'Supplier' As Type, ContactName, City, Country FROM Suppliers 
WHERE Country='USA' 
ORDER BY City; 