from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

my_dag_id="dag_pythonop1"

def my_python_function():
    print("Hello, Airflow!")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_python_function,
    dag=my_dag_id,
)