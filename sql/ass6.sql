-- Start a transaction

create database bank_db;
use bank_db;

create table accounts (account_id int primary key,name varchar(50),balance int);

insert into accounts values(1,'Rahul',10000),(2,'Amit',5000),(3,'Krish',15000),(4,'Freya',7000);

start transaction;

-- Insert record into accounts

insert into accounts (account_id, name, balance) values (5, 'Hit', 3000);

-- Rollback changes

Rollback;
select * from accounts;

-- Commit valid transactions

insert into accounts values (6, 'Neha', 7000);
commit;

-- Demonstrate transfer of money using transaction

update accounts set balance = balance - 1000 where account_id = 1;
update accounts set balance = balance + 1000 where account_id = 2;
update accounts set balance = balance - 1000 where account_id = 3;
update accounts set balance = balance + 1000 where account_id = 4;
commit;