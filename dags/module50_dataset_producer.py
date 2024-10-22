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
    schedule="@daily",
    catchup=False
)

@task(outlets=[my_file])
def update_dataset():
   with open(my_file.uri, "+a") as f:
      f.write("producer update")
   

python_task = PythonOperator(
    task_id='update_ds_task',
    python_callable=update_dataset(),
    dag=dag,
)