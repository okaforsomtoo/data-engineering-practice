/* SELECT  department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 40000; */

SELECT COUNT(*) FROM employees;

/* SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department;
*/

/* SELECT AVG(salary) AS average_salary
FROM employees;
*/

/* SELECT department, 
        COUNT(*) AS total_employees,
        AVG(salary) AS average_salary
FROM employees
GROUP BY department; 

SELECT department, 
        SUM(salary) AS total_salary,
        MAX(salary) AS highest_salary,
        MIN(salary) AS lowest_salary
FROM employees
GROUP BY department; */

/* CREATE TABLE departments (
    department TEXT,
    manager TEXT,
    budget REAL
);

INSERT INTO departments VALUES ('Engineering', 'David', 120000);
INSERT INTO departments VALUES ('Marketing', 'Sandra', 85000);
INSERT INTO departments VALUES ('HR', 'Patricia', 60000);
INSERT INTO departments VALUES ('Finance', 'Robert', 95000); */

-- SELECT * FROM departments;

/* SELECT employees.name, employees.salary, departments.manager, departments.budget
FROM employees
INNER JOIN departments ON employees.department = departments.department; */

/*SELECT employees.name, employees.salary, departments.manager, departments.budget
FROM employees
LEFT JOIN departments ON employees.department = departments.department; */

/*SELECT name, department, salary,
        -- AVG(salary) OVER (PARTITION BY department) AS dept_abg_salary
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees; */

/* SELECT name, department, salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary ASC) AS rank
FROM employees;

SELECT name, department, salary,
        RANK() OVER (ORDER BY salary DESC) AS overall_rank
FROM employees; */

-- Challenge 1: Write a query that returns all employees who live in London, showing only their name, department and salary.
SELECT name, department, salary
FROM employees
    WHERE city = "London";


-- Challenge 2: Write a query that shows the total salary bill per department, ordered from highest to lowest.
/*SELECT department, 
    SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC; */

/* SELECT name
FROM pragma_table_info('employees'); */ 

-- Challenge 3: Write a query that returns only departments where the minimum salary is above £30,000.

/* SELECT department, MIN(salary) AS min_salary 
FROM employees
GROUP BY department
HAVING MIN(salary) > 30000; */


-- Challenge 4: Write a query that shows each employee’s name, salary and the highest salary in their department side by side — without collapsing the rows.
/* 
SELECT name, salary, department,
MAX(salary) OVER (PARTITION BY department) AS max_salary_in_dept
FROM employees; 
*/

-- Challenge 5: Write a query using a JOIN that shows each employee’s name, their manager’s name and their department budget — but only for employees earning above £40,000
SELECT employees.name, departments.manager, departments.budget 
FROM employees 
INNER JOIN departments ON employees.department = departments.department
WHERE employees.name = 'Tom';