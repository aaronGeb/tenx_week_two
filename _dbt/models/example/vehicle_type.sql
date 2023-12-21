
{{ config(materialized='view') }}

WITH summary AS (
    SELECT 
        " car_type" AS "Vehicle type",
        COUNT(*) AS "Vehicle count",
        ROUND(Avg(" traveled_d"  ::Numeric),2) AS "Avg distance traveled",
        ROUND(AVG(" speed")::NUMERIC, 2) AS "Avg speed by vehicle"
    FROM trajectory
    GROUP BY type
    ORDER BY "Vehicle count" ASC
)

SELECT * FROM summary
