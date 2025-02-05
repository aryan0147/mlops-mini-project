import mlflow
import dagshub  # type: ignore

mlflow.set_tracking_uri("https://dagshub.com/aryan0147/mlops-mini-project.mlflow")
dagshub.init(repo_owner="aryan0147", repo_name="mlops-mini-project", mlflow=True)

with mlflow.start_run():
    mlflow.log_param("parameter name", "value")
    mlflow.log_metric("metric name", 1)
