from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

my_dag_id="dag_pythonop1"

default_args = {
    'owner': 'proton',
    'depends_on_past': False,
    'retries': 10,
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