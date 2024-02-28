import pandas as pd
import numpy as np

import pandas as pd
import psycopg2
from sqlalchemy import create_engine


def run_sql_query(connection_params: dict, query: str) -> None:
    connection = None
    cursor = None

    try:
        # Establish the database connection
        connection = psycopg2.connect(**connection_params)

        # Create a cursor
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Commit the transaction
        connection.commit()

        # Log success
        print("Log success")

    except Exception as e:
        # Log the error
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return None