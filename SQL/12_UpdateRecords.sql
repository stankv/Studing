-- 12.3. Задания

-- 12.3.1. Добавьте нового пользователя в таблицу Employees.
INSERT INTO Employees (LastName, FirstName, Title, TitleOfCourtesy, City, Country) 
VALUES ('Anderson', 'Thomas', 'Programmer', ' Mr.', 'New York', 'USA'); 

-- 12.3.2. Свяжите этого нового пользователя с какой-либо территорией с помощью таблицы EmployeeTerritories (многие-ко-многим).
INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID) 
VALUES (11, '10019'); 

-- 12.3.3. Попробуйте добавить новую запись в таблицу заказов Orders. Возникнут ли какие-либо конфликты? 
INSERT INTO Orders (CustomerID, EmployeeID) 
VALUES ('FRANS', 11); 