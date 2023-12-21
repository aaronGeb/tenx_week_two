
{{ config(materialized='view') }}

with fast_vehicles as (
    SELECT " car_type"
    from trajectory t 
    ORDER BY " avg_speed" DESC
)


SELECT * FROM fast_vehicles