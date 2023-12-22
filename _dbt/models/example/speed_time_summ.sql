
-- top_speed.sql

WITH top_speed as (
    SELECT * FROM {{ ref('time_summary') }}
)

SELECT *
FROM top_speed
ORDER BY "speed" ASC
LIMIT 100
