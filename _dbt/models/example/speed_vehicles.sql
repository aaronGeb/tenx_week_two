
{{ config(materialized='view') }}

SELECT "type"
FROM (
    SELECT "type",
    RANK() OVER (ORDER BY avg_speed DESC) as speed_rank
    FROM trajectory
) ranked_trajectories
WHERE speed_rank <= 100