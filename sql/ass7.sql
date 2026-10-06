create database shop_db;
use shop_db;

create table customers (customer_id int primary key,name varchar(50),city varchar(50));
create table orders (order_id int primary key,customer_id int,order_date date,amount int);
create table products (product_id int primary key,product_name varchar(50),price int);
create table order_items (order_id int,product_id int,quantity int); 

insert into customers values(1, 'Rahul', 'Surat'),(2, 'Amit', 'Navsari'),(3, 'Neha', 'Vadodara'),(4, 'Pooja', 'Surat'),(5, 'Karan', 'Ahmedabad'),(6, 'Meera', 'Navsari');

insert into orders values(101, 1, '2026-01-10', 20000),(102, 1, '2026-02-15', 35000),(103, 2, '2026-01-20', 15000),(104, 3, '2026-02-25', 60000),(105, 4, '2026-03-10', 25000),(106, 5, '2026-03-15', 45000),(107, 2, '2026-03-20', 40000);

insert into products values(1, 'Laptop', 50000),(2, 'Mouse', 1000),(3, 'Keyboard', 2000),(4, 'Monitor', 15000);

insert into order_items values(101, 1, 1),(101, 2, 2),(102, 1, 1),(102, 4, 1),(103, 2, 3),(104, 1, 2),(105, 3, 2),(106, 4, 2),(107, 1, 1); 

-- 1. Total orders per customer

select c.name, count(o.order_id) as total_orders from customers c join orders o on c.customer_id = o.customer_id group by c.name;

-- 2. Customers who never placed an order

select c.name from customers c left join orders o on c.customer_id = o.customer_id where o.order_id is null;

-- 3. Highest selling product

select p.product_name, sum(o.quantity) as total_sold from products p join order_items o on p.product_id = o.product_id group by p.product_name order by total_sold desc limit 1;

-- 4. Monthly sales report

select month(order_date) as month, sum(amount) as total_sales from orders group by month(order_date);

-- 5. Customers with total purchase > 50,000

select c.name, sum(o.amount) as total_purchase from customers c join orders o on c.customer_id = o.customer_id group by c.name having sum(o.amount) > 50000;

-- 6. Top 3 cities by revenue

select c.city, sum(o.amount) as revenue from customers c join orders o on c.customer_id = o.customer_id group by c.city order by revenue desc limit 3; 