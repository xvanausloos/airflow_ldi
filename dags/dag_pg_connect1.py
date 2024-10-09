from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator

my_dag_id = 'dag_pg_connect1'

default_args = {
    'owner': 'xavier',
    'depends_on_past': False,
    'retries': 10,
    'concurrency': 1
}

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(seconds=5)    
)
    
create_table_task = PostgresOperator(
    task_id='create_table_task',
    postgres_conn_id='postgres',
    sql='''
        CREATE TABLE IF NOT EXISTS users (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            country TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL);''' ,
    dag=dag
    )
