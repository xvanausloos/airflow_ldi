import json
import pandas as pd
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


my_dag_id = 'dag_pg_connect1'

default_args = {
    'owner': 'xavier',
    'depends_on_past': False,
    'retries': 0,
    'concurrency': 1
}

def _process_user(ti):
    user = ti.xcom_pull(task_ids="extract_user")
    user = user['results'][0]
    print(user)
    processed_user = pd.json_normalize({
        'firstname': user['name']['first'],
        'lastname': user['name']['last'],
        'country': user['location']['country'],
        'username': user['login']['username'],
        'password': user['login']['password'],
        'email': user['email']
    })
    processed_user.to_csv('/tmp/processed_user.csv', index=None, header=False)

def _store_user():
    hook = PostgresHook(postgres_conn_id='postgres')
    hook.copy_expert(
        sql="COPY users FROM stdin WITH DELIMITER as ','",
        filename='/tmp/processed_user.csv'
    )

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2024, 10, 1),
    schedule_interval=timedelta(minutes=60)
)
    
create_table = PostgresOperator(
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

process_user = PythonOperator(
    task_id='process_user',
    python_callable=_process_user, 
    dag=dag
)


store_user = PythonOperator(
    task_id='store_user',
    python_callable=_store_user,
    dag=dag
)


create_table >> is_api_available >> extract_user >> process_user >> store_user
