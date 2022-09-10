
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

## MLflow Tracking: 
MLflow Tracking is probably the most used tool in industry by ML engineers and data scientists. Lets quickly see how to use mlflow tracking to track the metrics and parameters. <br>

You can copy and paste below code in jupyter notebook named train.ipynb
<img src="https://github.com/ShubhPatil95/MLFLOW_Tutorial/tree/main/images/train-ipynb.jpg" alt="train.ipynb">

```ruby
import mlflow

if __name__ == "__main__":
    mlflow.log_param("Param-1", "Apple")
    mlflow.log_param("Param-2", 11)
    mlflow.log_metric("Metrics-1",12)
    mlflow.log_metric("Metrics-2",20.5)

    with open("test.txt", "w") as f:
        f.write("hello world!")
    mlflow.log_artifact("test.txt")
```
Now run below line in next cell of train.ipynb and you will get URL UI like http://127.0.0.1:5000. Go to URL and you will see output as below.
```ruby
mlflow ui
```
<img src="https://github.com/ShubhPatil95/MLFLOW_Tutorial/tree/main/images/UI-outputs-1.jpg" alt="UI output-1">

You can click on run and you will see below page showing all detail with test.txt file.

<img src="https://github.com/ShubhPatil95/MLFLOW_Tutorial/tree/main/images/UI-outputs-1-Inside.jpg" alt="UI-outputs-1-Inside">




<details><summary> <h3> Simple ML Project </h3> </summary>
<p>

#### Step1: Create a train.py file copying code from [here]()
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



