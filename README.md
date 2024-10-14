Airflow LDI sandbox Sept 2024

Use for Udemy Airflow training: https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32289376?start=1#questions

## How to use in MacOs:
- Start Docker desktop 
- Enable venv : source venv/bin/activate
- Run `make deploy-infrastructure`. It will deploy the infrastructure for Airflow in Docker/K8S

Open your web browser and go to Airflow UI: `http://localhost:8080`

Default account/pwd: admin/admin

## Dev env
- Open repo in Visual Studio Code
- Enable venv `source venv/bin/activate`
- run `make install-requirements` 


## Run a Docker Postgres instance
The HELM chart already contains a Postgre instance for the Airflow metastore.

## Connecting Airflow to Postgres
Go in Airflow UI, create a new connection to Postgres.

