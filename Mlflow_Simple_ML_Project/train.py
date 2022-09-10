from sklearn.linear_model import ElasticNet
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import mlflow
import mlflow.sklearn

x=np.array([1,2,3,4,5,6]).reshape(-1,1)
y=np.array([11,22,33,55,44,66])

alphas=[0.5,1,1.5]
l1_ratios=[0.5,1]

for alpha in alphas:
    for l1_ratio in l1_ratios:
        with mlflow.start_run():
            model=ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
            model.fit(x, y)
            y_pred = model.predict(x)

            # Metrics
            r2=r2_score(y,y_pred)
            MSE=mean_squared_error(y,y_pred)
            MAE=mean_absolute_error(y,y_pred)

            #logging params
            mlflow.log_param("alpha", alpha)
            mlflow.log_param("l1_ratio", l1_ratio)

            # logging metrics
            mlflow.log_metric("MSE", MSE)
            mlflow.log_metric("MAE", MAE)
            mlflow.log_metric("r2", r2)

            # mlflow model logging 
            mlflow.sklearn.log_model(model, "model")




