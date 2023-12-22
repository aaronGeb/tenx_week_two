{{ config(materialized='view') }}

WITH top_speed AS (
    SELECT * FROM {{ ref('time_summary') }}
)

SELECT 
    *
FROM top_speed
ORDER BY "lat_acc" ASC
LIMIT 200
