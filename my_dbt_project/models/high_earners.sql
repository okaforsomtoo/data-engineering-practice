{{ config(materialized='table') }}

with employees as (
    select * from {{ ref('people') }}
),
 
high_earners as (
    select
        name,
        salary,
        city
    from employees
    where salary > 50000
)

select * from high_earners