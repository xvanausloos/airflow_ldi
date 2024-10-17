from airflow import DAG, Dataset
from airflow.decorators import task
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

my_file = Dataset('/tmp/my_file.txt')

my_dag_id = 'dag_producer_dataset'

default_args = {
    'owner': 'xavier',
    'depends_on_past': False,
    'retries': 0,
    'concurrency': 1
}

# dag declaration
dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2019, 6, 17),
    schedule_interval=timedelta(seconds=5)
)

def my_python_function():
    print("Hello, Airflow!")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_python_function,
    dag=dag,
)