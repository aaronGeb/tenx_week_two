{{ config(materialized='view') }}

WITH timely_summary AS (
    SELECT 
        " time",
        ROUND(AVG( " speed"::NUMERIC), 2) AS avg_speed,
        ROUND(AVG(" lat_acc"::NUMERIC), 2) AS avg_lat_acc,
        ROUND(AVG(" lon_acc"::NUMERIC), 2) AS avg_lon_acc
    FROM vehicle
    GROUP BY  " time"
)

SELECT * FROM timely_summary

