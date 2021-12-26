-- 10.4. Задания

/* 10.4.1. Перепишите задание 8.3.2 через синтаксис JOIN.
8.3.2 Организуйте эквисоединение, которое выводит цену и названия тех товаров, для которых цена за единицу (UnitPrice) 
в таблице Order Details меньше 20. */

-- эквисоединение
SELECT Products.ProductName, Products.UnitPrice
FROM Products, [Order Details]
WHERE Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20;

-- перепишем через синтаксис JOIN:
SELECT Products.ProductName, Products.UnitPrice
FROM Products
INNER JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20;


-- 10.4.2. Имеется запрос
SELECT Orders.Freight, Customers.CompanyName
FROM Orders INNER JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
ORDER BY Freight;
/* Проверьте этот запрос с вариантом FULL JOIN -- за счёт чего выдача получилась объёмнее? Почему значения NULL 
встречаются в обоих полях набора? */

-- Действительно, с FULL JOIN в выдаче 832 строки (вместо 830 при INNER JOIN), и первые две строки имеют значения NULL
-- в столбце Freight. Это связано с тем, что с FULL JOIN происходит объединение множеств, и добавились 2 записи, не соответствующие 
-- условиям отбора, поэтому поля, соответствующие другой таблице, заполнились значением NULL. 

-- 10.4.3. Подумайте, как с помощью предложения WHERE превратить запрос CROSS JOIN в INNER JOIN.

-- было:
SELECT Employees.FirstName, Employees.LastName, Orders.Freight
FROM Employees CROSS JOIN Orders
WHERE Employees.EmployeeID = Orders.EmployeeID;

-- стало:
SELECT Employees.FirstName, Employees.LastName, Orders.Freight
FROM Employees INNER JOIN Orders
ON Employees.EmployeeID = Orders.EmployeeID
-- т.е. запросы эквивалентны.

-- 10.4.4. Перепишите данный запрос в INNER JOIN:
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products CROSS JOIN [Order Details]
WHERE Products.ProductID = [Order Details].ProductID

-- стало:
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products INNER JOIN [Order Details]
ON Products.ProductID = [Order Details].ProductID;