-- 1. find employees earning more than average salary

select * from employees where salary > (select avg(salary) from employees);

-- 2. Find department with higest total salary

select d.dept_name , sum(e.salary) as Total_Salary from employees e join departments d on e.dept_id = d.dept_id group by d.dept_id,d.dept_name order by Total_Salary desc limit 1;

--  3. Display employee with second higest salary

select * from employees order by salary desc limit 1 offset 1;

-- 4. Display employee working in same department as "Amit"

select * from employees where dept_id = (select dept_id from employees where emp_name = 'Amit');