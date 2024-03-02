# Data warehouse with MySQL, DBT, Airflow
![](image/Screenshot%202024-03-02%20at%2019.52.12.png)

In collaboration with a municipal traffic department, I am actively involved in the collection of traffic data through the deployment of swarm UAVs (drones) across diverse locations within the city.

 The primary objective is to leverage the gathered data for enhancing overall traffic management and supporting various undisclosed projects. Assigned with this crucial task, my company is undertaking the development of a scalable data warehouse. This warehouse will serve as the repository for vehicle trajectory data, meticulously derived from the analysis of footage captured by swarm drones and stationary roadside cameras.

#### The objective of this project is to execute the essential tasks outlined below:

- A data warehouse (PostgresQL)
- An orchestration service (Airflow)
- An ELT tool (dbt)
- Visualization on Redash
  


## Getting Started
1. **Clone the Repository:**
  ```
   $ git clone https://github.com/Xmuluneh/tenx_week_two
   $ cd tenx_week_two
   ```
2.**Build and Run Airflow**
  ```
  $ docker-compose up --build
  ```
3.**Stop Airflow Services:**
  ```
  $ docker-compose down
  ```
# License

This project is licensed under the [MIT LICENSE](LICENSE).

Please feel welcome to contribute, offer feedback, or utilize the code as required!
