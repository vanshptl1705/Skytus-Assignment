CREATE DATABASE company_db;

USE  company_db;

CREATE TABLE employees (
 emp_id INT,
 emp_name varchar(50),
 dept_id int,
 salary INT
);

insert into employees values(1, "Rahul", 1, 45000);
insert into employees values(2, "Amit", 2, 55000);
insert into employees values(3, "Neha", 1, 75000);
insert into employees values(4, "Pooja", 3, 62000);
insert into employees values(5, "Karan", 2, 48000);
insert into employees values(6, "Meera", 4, 90000);
insert into employees values (7, "Ravi", 1, 52000);
insert into employees values (8, "Priya", 1, 68000);

CREATE TABLE departments (
 dept_id INT,
 dept_name varchar(50)
);

insert into departments values(1, "IT");
insert into departments values(2, "HR");
insert into departments values(3, "Finance");
insert into departments values(4, "Sales");

-- 1. Display employee name with department name

select e.emp_name, d.dept_name from employees e join departments d on e.dept_id = d.dept_id;

-- 2. Display employees earning more than 50,000

select * from employees where salary > 50000;

-- 3. Display department-wise total salary

select d.dept_name,sum(e.salary) as total_salary from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name;

-- 4. Display departments with more than 2 employees

select d.dept_name,count(e.emp_id) as total_employees from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name having count(e.emp_id)>2;

-- 5. Display employees without a department

select e.emp_name from employees e left join departments d on e.emp_id = d.dept_id where d.dept_id is null;