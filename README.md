
## MLFLOW_Tutorial

PLease refer below sections and follow the step to run and learn.

<details><summary> <h2> Mlflow-Simple-ML-Project </h2> </summary>
<p>

#### Step1: Create a folder Mlflow_Project_Package and move inside the folder
```ruby
Mlflow_Simple_ML_Project
cd Mlflow_Simple_ML_Project
```
#### Step2: Create a train.py by copying code from here [train.py](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Simple_ML_Project/train.py)
```ruby
nano train.py
```  
#### Step3: Lets try to understand train.py/
```ruby
with mlflow.start_run():   # The parameters,metrics and artifacts under indentation of this line will be recorded.

mlflow.log_param("param_name",param_value)  # It will log the paramters

mlflow.log_metric("metric_name", metric_value)  # IT will log the metrics
  
mlflow.sklearn.log_model(model, "model_name")    # It will record model created by sklearn
```

#### Step4: Lets run train.py and wait till successful execution. Then you will notice that new folder under mlruns will be created.
  
```ruby
ls  # It will list the file and folder inside of Mlflow_Simple_ML_Project
```
  
#### Step5: Now its time to go to mlflow UI to see systematically presented parameters, metrics and artificats. Then it will generated URL for UI: http://127.0.0.1:5000.
```ruby
mlflow ui
```
  
#### Step6: On UI you will see all the metrics and logs we have recorded through our code. Explore this UI and enjoy it.
  
</p>
</details>





<details><summary> <h2> Mlflow_Project_Package </h2> </summary>
<p>

#### Step1: Create a folder Mlflow_Project_Package
```ruby
mkdir Mlflow_Project_Package
```
#### Step2: Create a new conda env
```ruby
conda create -n mlflow_env python=3.7 -y
```
#### Step3: Create a python file train.py and copy paste code from [train.py](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/train.py) or You can create train.ipynb file from [train.ipynb]
```ruby
nano train.py
```
#### Step4: Create requirements.txt and paste code from [requirements.txt](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/requirements.txt) and second command
```ruby
nano requirements.txt
pip install -r requirements.txt
```
#### Step5: Check if train.py is running
```ruby
python3 train.py  
```
#### Step6: run below command and check if results are logged into mlflow ui. If you have train.ipynb file in step3 then you can run this command in next cell of jupyter notebook as well.
```ruby
mlflow ui
```
#### Step7: Create [conda.yaml](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/conda.yaml) exporting depencies into it or you can go to mlflow ui and copy paste same conda.yaml file.
```ruby
conda env export > conda.yaml
```
#### Step8: Create file under name MLproject and copy paste from [MLproject](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/MLproject)
```ruby
nano MLproject
```
#### Step9: Run below command to check if package is running(second command will run it in local existing conda)
```ruby
mlflow run . -P intercept=False
mlflow run . -P intercept=False --no-conda
```
#### Step10: How to share your project??<br>
just share below four file and ask to run command <strong>mlflow run .</strong>
```ruby
  1. requirements.txt
  2. train.py
  3. conda.yaml 
  4. MLproject 
````
#### Step11: How to run project from github? <br> (make sure code on github is directly inside repo not under any folder of repo) Run below command.
```ruby
 # mlflow run git@github.com:Username/Repo_Name --version branch_name
   mlflow run git@github.com:ShubhPatil95/Mlflow_Project_Package --version main
```
 #### Step12: mlflow run using python API, just create file [mlflow_run_test.py](https://github.com/ShubhPatil95/Mlflow_Project_Package/blob/main/mlflow_run_test.py)
```ruby
 python3 mlflow_run_test.py
```
  
</p>
</details>



