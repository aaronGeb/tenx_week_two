{{ config(materialized='view') }}

WITH ranked_timely_summary AS (
    SELECT
        "time",
        ROUND(AVG(CAST("speed" AS NUMERIC)), 2) as "speed",
        ROUND(AVG(CAST("lat_acc" AS NUMERIC)), 2) as "lat_acc",
        ROUND(AVG(CAST("lon_acc" AS NUMERIC)), 2) as "lon_acc",
        RANK() OVER (ORDER BY "time") as time_rank
    FROM vehicle
    GROUP BY "time"
)

SELECT * FROM ranked_timely_summary