# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers
where id not in (
    select CustomerId from Orders
);