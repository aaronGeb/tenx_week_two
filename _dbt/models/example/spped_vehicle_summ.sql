
{{ config(materialized='view') }}

WITH fast_v AS (
    SELECT * FROM {{ ref('speed_vehicles') }}
)

SELECT 
    type as "Vehicle type",
    count(type) as "vehicle count"
FROM fast_v 
GROUP BY type
ORDER BY "vehicle count" ASC
