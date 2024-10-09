export RELEASE_NAME=airflow-example-release
export NAMESPACE=airflow-example-namespace
kubectl delete namespace $NAMESPACE
kubectl create namespace $NAMESPACE
helm install $RELEASE_NAME apache-airflow/airflow \
  -f override-values.yaml \
  --namespace $NAMESPACE 
  
kubectl port-forward svc/$RELEASE_NAME-webserver 8080:8080 --namespace $NAMESPACE
