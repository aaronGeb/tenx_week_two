
{{ config(materialized='view') }}

WITH ranked_summary AS (
    SELECT
        "type" as "Vehicle type",
        COUNT("type") as "vehicle count",
        ROUND(AVG(CAST("traveled_d" AS NUMERIC)), 2) as "Avg distance traveled",
        ROUND(AVG(CAST("avg_speed" AS NUMERIC)), 2) as "Avg speed by vehicle",
        RANK() OVER (ORDER BY COUNT("type") ASC) as vehicle_count_rank
    FROM trajectory
    GROUP BY "type"
)

SELECT * FROM ranked_summary
WHERE vehicle_count_rank <= 100
