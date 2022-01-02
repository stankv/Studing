-- Задания

-- Попробуйте разобраться по исходному коду запросов:

-- 14.1. Чем представление Invoices отличается от таблицы Orders?
-- Таблица Orders хранит конкретные значения. Представление Invoices отбирает значения из таблиц Orders и 
-- Shippers, Products, Employees, Customers согласно заданным условиям, а также выводит результат вычисления
-- CONVERT(money, (dbo.[Order Details].UnitPrice * dbo.[Order Details].Quantity) * (1 - dbo.[Order Details].Discount) / 100) * 100 


-- 14.2. Что делает представление "CategorySales for 1997"?
-- Отбирает значения из представления dbo.[Product Sales for 1997] и выдает таблицу из 2-х столбцов: CategoryName и CategorySales,
-- где значения CategorySales есть суммы SUM(ProductSales). Результат выдачи сортируется по CategoryName.


-- 14.3. Что делает представление "Sales Total by Amount"?
-- Отбирает конкретные значения из представления [Order Subtotals] и таблиц Orders и Customers согласно заданным условиям:
-- [Order Subtotals].Subtotal > 2500) AND (dbo.Orders.ShippedDate BETWEEN '19970101' AND '19971231')


-- 14.4. Что делает представление "Products Above Average Price"?
-- Используется вложенный запрос. Отбираются значения полей ProductName и UnitPrice таблицы Products, но только те, 
-- для которых значение поля UnitPrice больше среднего всех значений этого поля.

-- 14.5. Что делает представление "Summary of Sales by Quarter"? 
-- Отбираются значения полей ShippedDate и OrderID таблицы Orders, а также значения поля Subtotal представления
-- [Order Subtotals], по соответствию ключей Orders.OrderID = [Order Subtotals].OrderID, при условии что значения поля
-- Orders.ShippedDate не пустые.