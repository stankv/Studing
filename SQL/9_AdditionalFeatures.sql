-- 9.4. Задания

-- 9.4.1. Найдите все пары из разных заказчиков (Customers), для которых не задан регион (поле Region).
SELECT t1.ContactName, t2.ContactName, t1.Region
FROM Customers t1, Customers t2 
WHERE (t1.Region IS NULL) AND (t2.Region IS NULL) AND
      (t1.CustomerID <> t2.CustomerID)

-- 9.4.2. Найдите вложенным запросом список заказов (Orders), в котором у заказчиков (Customers) регион не пуст (поле Region).
SELECT * FROM Orders t1 
WHERE EXISTS 
(SELECT * FROM Customers t2 
WHERE t1.CustomerID = t2.CustomerID AND t2.Region IS NOT NULL);

-- или:
SELECT OrderID
FROM Orders t1
WHERE CustomerID = ANY 
  (SELECT CustomerID FROM Customers
   WHERE Region IS NOT NULL);

/* 9.4.3. Немного условный, но показательный пример. Найдите все заказы (таблица Orders), цена за доставку товара которых 
(Freight) превышает цену любого товара (поле UnitPrice, таблица Products). */
SELECT * FROM Orders
WHERE Freight > ANY
(SELECT MAX(UnitPrice) FROM Products);
-- это не правильно. правильно вот так:
SELECT * FROM Orders
WHERE Freight > ALL
(SELECT UnitPrice FROM Products);