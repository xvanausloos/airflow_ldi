#!/bin/bash
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace

kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow

