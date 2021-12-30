-- 13.3. Задания

-- 13.3.1. Увеличьте скидку (Discount) в таблице Order Details до 20% (0.20) для тех единиц товара, которых на складе 
-- хранится больше 50 (поле Quantity). Напишите запрос, но не выполняйте, чтобы не вносить изменения в таблицу.
UPDATE [Order Details]
SET Discount = 0.20
WHERE Quantity > 50;

-- 13.3.2. В таблице Contacts измените все контактные данные, ранее приходившиеся на Berlin (поле City) и Germany 
-- (поле Country), соответственно на Piter и Russia. Напишите запрос, но не выполняйте, чтобы не вносить изменения в таблицу.
UPDATE Contacts
SET City = 'Piter', Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Russia';

-- 13.3.3. Добавьте и затем удалите несколько записей в таблице Shippers. По какому критерию вы удаляли свежие записи? 

-- добавляем:
INSERT INTO Shippers (CompanyName) 
VALUES ('MetaCortex'); 

INSERT INTO Shippers (CompanyName) 
VALUES ('Matrix', '(503) 555-4321'); 

-- удаляем
DELETE FROM Shippers 
WHERE Phone IS NULL; 