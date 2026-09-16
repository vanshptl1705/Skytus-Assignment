-- 1. Count total number of students

select count(*) as Number_of_students from students;

-- 2. Find average marks of students

select avg(marks) as Average_marks from students;

-- 3. Find highest and lowest marks

select max(marks) as Highest_marks , min(marks) as Lowest_marks from students;

-- 4. Find department-wise average marks

select department , avg(marks) from students group by department;

-- 5. Display departments where average marks > 70

select department, avg(marks) from students group by department having avg(marks) > 70;