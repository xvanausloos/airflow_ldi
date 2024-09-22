FROM apache/airflow:2.10.2-python3.9
RUN pip install apache-airflow-providers-microsoft-azure==1.2.0rc1