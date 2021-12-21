-- Задания

/* 8.3.1. Сформируйте список названий товаров (таблица Products) с указанием для каждого из них соответствующей 
категории (таблица Categories). */
SELECT Products.ProductName, Categories.CategoryName
FROM Products, Categories
WHERE Products.CategoryID = Categories.CategoryID;

/* 8.3.2. Организуйте эквисоединение, которое выводит цену и названия тех товаров, для которых цена за единицу 
(UnitPrice) в таблице Order Details меньше 20. */
SELECT Products.ProductName, [Order Details].UnitPrice
FROM Products, [Order Details]
WHERE Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20;

-- 8.3.3. Добавьте к предыдущему запросу третью таблицу Categories, и выведите в дополнение к названию товара его категорию. 
SELECT Products.ProductName, Categories.CategoryName, [Order Details].UnitPrice
FROM Products, Categories, [Order Details]
WHERE (Products.ProductID = [Order Details].ProductID AND [Order Details].UnitPrice < 20) AND
      (Products.CategoryID = Categories.CategoryID);