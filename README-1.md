
## MLFLOW_Tutorial

PLease refer below sections and follow the step to run and learn.

<details><summary> <h3> Mlflow Installation Steps </h3> </summary>
<p>

#### Step1: Run a below command to install a mlflow(You can run this command in jupyter notebook cell as well)
```ruby
pip install mlflow
```
#### Step2: Check version of mlflow
```ruby
# for command line
mlflow --version

# For jupyter notebook
mlflow.__version__
```  
#### (Optional)Step3: It is recommend to create an new environment before installting mlflow
```ruby
conda create -n mlflow_env
conda activate mlflow_env
pip install mlflow
```    
</p>
</details>

There are 4 components of MLflow and they can be used independently.
* <strong> MLflow Tracking:</strong> It is used for logging metrics, parameters, code versions and output files
* <strong> MLflow Projects:</strong> It can package the code in a way in order to reproduce it on any plotform.
* <strong> MLflow Models:</strong> It is a standard format for packaging machine learning models that can be used in a variety of downstream tools—for example, real-time serving through a REST API or batch inference on Apache Spark. 
* <strong> MLflow Model Registry:</strong> It is a centralized model store, set of APIs, and web interface to manage the full ML lifecycle.

### MLflow Tracking: 
MLflow Tracking is probably the most used tool for a Da
