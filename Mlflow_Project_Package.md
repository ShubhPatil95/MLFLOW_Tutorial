PLease refer below sections and follow the step to run and learn.

<details><summary> <h2> Mlflow_Project_Package </h2> </summary>
<p>

* Create a folder Mlflow_Project_Package
```ruby
mkdir Mlflow_Project_Package
```
* Create a new conda env
```ruby
conda create -n mlflow_env python=3.7 -y
```
* Create a python file train.py and copy paste code from [train.py](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/train.py)
```ruby
nano train.py
```
* Create requirements.txt and paste code from [requirements.txt](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/requirements.txt) and second command
```ruby
nano requirements.txt
pip install -r requirements.txt
```
* Check if train.py is running
```ruby
python3 train.py  
```
* run below command and check if results are logged into mlflow ui
```ruby
mlflow ui
```
* Create [conda.yaml](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/conda.yaml) exporting depencies into it or you can go to mlflow ui and copy paste same conda.yaml file.
```ruby
conda env export > conda.yaml
```
* Create file under name MLproject and copy paste from [MLproject](https://github.com/ShubhPatil95/MLFLOW_Tutorial/blob/main/Mlflow_Project_Package/MLproject)
```ruby
nano MLproject
```
* Run below command to check if package is running(second command will run it in local existing conda)
```ruby
mlflow run . -P intercept=False
mlflow run . -P intercept=False --no-conda
```
* How to share your project??<br>
just share below four file and ask to run command <strong>mlflow run .</strong>
```ruby
  1. requirements.txt
  2. train.py
  3. conda.yaml 
  4. MLproject 
````
* How to run project from github? <br> (make sure code on github is directly inside repo not under any folder of repo) Run below command.
```ruby
 # mlflow run git@github.com:Username/Repo_Name --version branch_name
   mlflow run git@github.com:ShubhPatil95/Mlflow_Project_Package --version main
```
 * mlflow run using python API, just create file [mlflow_run_test.py](https://github.com/ShubhPatil95/Mlflow_Project_Package/blob/main/mlflow_run_test.py)
```ruby
 python3 mlflow_run_test.py
```
  
</p>
</details>
