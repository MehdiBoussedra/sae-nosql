# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importation des modules utilisés
import sqlite3
import pandas

# Création de la connexion
conn = sqlite3.connect("ClassicModel.sqlite")

# Récupération du contenu de Customers avec une requête SQL
Customers = pandas.read_sql_query("SELECT * FROM Customers;", conn)

# Fermeture de la connexion : IMPORTANT à faire dans un cadre professionnel
conn.close()

print(Customers)

q1 = pandas.read_sql_query(

"""
SELECT c.customerNumber, c.customerName
FROM Customers c
LEFT JOIN Orders o ON c.customerNumber = o.customNumber
WHERE o.orderNumber IS NULL;

""",
conn
)

print(q1)

# Pour chaque employé, le nombre de clients, le nombre de commandes et le montant total de celles-ci

q2 = pandas.read_sql_query(
    
"""
SELECT e.employeeNumber, e.firstname, e.lastname,
COUNT(DISTINCT c.customersNumbers) AS CustomerCount,
COUNT(DISTINCT Orders.OrdersNumbers) AS OrdersCount,
SUM(OrdersDetails.priceEach * OrdersDetails.QuantityOrdered) AS TotalOrdersCount,
FROM Employee
LEFT JOIN Customers ON Employees.employeeNumber = Customers.salesRepEmployeeNumber
LEFT JOIN Orders ON Customers.customerNumber = Orders.customerNumber
LEFT JOIN OrderDetails ON Orders.orderNumber = OrderDetails.orderNumber
GROUP BY Employees.employeeNumber;

"""

q3 = pandas.read_sql_query(

"""
SELECT
 o.officeCode,
 o.city,
 o.country AS officeCountry,
 COUNT(DISTINCT c.customerNumber) AS numberOfCustomers,
 COUNT
