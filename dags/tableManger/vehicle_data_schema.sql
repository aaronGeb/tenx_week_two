
CREATE TABLE IF NOT EXISTS vehicles
(
    "id" SERIAL NOT NULL,
    "track_id" TEXT NOT NULL,
    lat      double precision,
    lon      double precision,
    speed    double precision,
    lon_acc  double precision,
    lat_acc  double precision,
    time     double precision,
    PRIMARY KEY ("id"),
    CONSTRAINT fk_trajectory
        FOREIGN KEY("track_id") 
            REFERENCES trajectories(track_id)
            ON DELETE CASCADE
    
);
