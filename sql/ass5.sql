-- Create users table with:

create table users (
	-- Primary key
    user_id int primary key,
    name varchar(50),
    
	-- Unique email
    email varchar(100) unique,
    
    -- Not null password
    password varchar(100) not null
);

-- Add foreign key between orders and users

create table orders (
    order_id int primary key,
    user_id int,
    product varchar(100),
    amount int,
    foreign key (user_id) references users(user_id)
);

-- Create index on email column

create index idx_email on users(email);

-- Create view to display user order summary

create view user_order_summary as select u.user_id, u.name, u.email, count(o.order_id) as total_orders, sum(o.amount) as total_amount from users u left join orders o on u.user_id = o.user_id group by u.user_id, u.name , u.email; 

select * from user_order_summary;