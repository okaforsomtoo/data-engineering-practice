{{ config(materialized='view') }}

    select 
        name,
        salary,
        city
    from {{ ref('high_earners') }}
    where city = 'London'