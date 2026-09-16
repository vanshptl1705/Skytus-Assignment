-- students(student_id INT, name VARCHAR(50), department VARCHAR(30), year INT, marks INT)

CREATE DATABASE students;

USE  students;

CREATE TABLE students (
 id INT primary key,
 name varchar(50),
 department varchar(20),
 year INT,
 marks INT
);

insert into students values(1,"Shrey","IT",1,50);
insert into students values(2,"Krish","IT",2,40);
insert into students values(3,"Parth","Civil",3,80);
insert into students values(4,"Riddhesh","Computer",2,66);
insert into students values(5,"Pratham","Electical",4,71);

--1 Display all student records

select * from students;

--2 Display only name and department

select name, department from students;

--3 Find students with marks greater than 75

select name from students where marks > 75;

--4 Display students from CSE department

select * from students where department = "Computer";

--5 Sort students by marks (descending)

select * from students order by marks desc;

--6 Display top 3 scorers

select * from students order by marks desc limit 3;