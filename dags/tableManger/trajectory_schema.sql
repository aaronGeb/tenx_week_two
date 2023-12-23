CREATE TABLE IF NOT EXISTS trajectories 
(
    "track_id" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    traveled_d double precision,
    avg_speed double precision,
    
    PRIMARY KEY ("track_id")
);