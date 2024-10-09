from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

my_dag_id = 'dag_pg_connect1'

dag = DAG(
    dag_id=my_dag_id,
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
)
    
create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres',
    sql='''
        CREATE TABLE IF NOT EXISTS users (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            country TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL);'''   
    )

create_table
