import json
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator


my_dag_id = 'dag_pg_connect1'

default_args = {
    'owner': 'xavier',
    'depends_on_past': False,
    'retries': 0,
    'concurrency': 1
}

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2024, 10, 1),
    schedule_interval=timedelta(minutes=60)
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

is_api_available = HttpSensor(
    task_id = 'is_api_available',
    http_conn_id = 'user_api',
    endpoint='api/',
    dag=dag
)  

extract_user = SimpleHttpOperator(
    task_id='extract_user',
    http_conn_id='user_api',
    endpoint='api/',
    method='GET',
    response_filter=lambda response: json.loads(response.text),
    log_response=True,
    dag=dag
)
