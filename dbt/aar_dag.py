from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook

# Define default_args dictionary to specify default parameters for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 19, 2),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

# Define the DAG with the default_args
dag = DAG(
    "data_loading_dag",
    default_args=default_args,
    description="A DAG to load data files into a database",
    schedule_interval=timedelta(days=1),  # Set the schedule interval as needed
)

# Define a function to load data into the database using PythonOperator
def load_data_to_db(**kwargs):
    # Use Airflow Variables to get the environment (Prod, Dev, Staging)
    environment = kwargs["task_instance"].xcom_pull(task_ids="check_environment")

    # Use the environment variable to determine the database connection
    if environment == "Prod":
        db_conn_id = "prod_database"
    elif environment == "Dev":
        db_conn_id = "dev_database"
    elif environment == "Staging":
        db_conn_id = "staging_database"
    else:
        raise ValueError(f"Invalid environment: {environment}")

    # Use a database hook to execute SQL or load data into the database
    db_hook = BaseHook.get_hook(conn_id=db_conn_id)
    # Implement your data loading logic here, for example:
    # db_hook.run("INSERT INTO your_table SELECT * FROM your_staging_table")


# Define a BashOperator to check the environment
check_environment = BashOperator(
    task_id="check_environment",
    bash_command="echo $AIRFLOW_ENVIRONMENT",
    dag=dag,
)

# Define PythonOperator to load data into the database
load_data_task = PythonOperator(
    task_id="load_data_to_db",
    python_callable=load_data_to_db,
    provide_context=True,  # Provide the context to the callable function
    dag=dag,
)

# Set the task dependencies
check_environment >> load_data_task
