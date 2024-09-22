#!/bin/bash
helm repo add apache-airflow https://airflow.apache.org

export RELEASE_NAME=airflow-example-release
export NAMESPACE=airflow-example-namespace

kubectl delete namespace $NAMESPACE
kubectl create namespace $NAMESPACE

helm install $RELEASE_NAME apache-airflow/airflow \
  --namespace $NAMESPACE \
  --set-string "env[0].name=AIRFLOW__CORE__LOAD_EXAMPLES" \
  --set-string "env[0].value=True"

kubectl port-forward svc/$RELEASE_NAME-webserver 8080:8080 --namespace $NAMESPACE

