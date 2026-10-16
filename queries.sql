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

SELECT name, department, salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary ASC) AS rank
FROM employees;

SELECT name, department, salary,
        RANK() OVER (ORDER BY salary DESC) AS overall_rank
FROM employees;
