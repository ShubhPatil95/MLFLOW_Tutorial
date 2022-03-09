# MLFLOW_Tutorial

<details><summary> <h2> Mlflow Project Package </h2> </summary>
<p>

* Create a folder Mlflow_Project_Package
```ruby
mkdir Mlflow_Project_Package
```
* Create a new conda env
```ruby
conda create -n mlflow_env python=3.7 -y
```
* Create a python file train.py and copy paste code from 
```ruby
nano train.py
```
* Create requirements.txt and paste code from and second command
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
* Create conda.yaml exporting depencies into it or you can go to mlflow ui and copy paste same conda.yaml file.
```ruby
conda env export > conda.yaml
```
* Create file under name MLproject and copy paste from
```ruby
nano MLproject
```
* Run below command to check if package is running(second command will run it in local existing conda)
```ruby
mlflow run . -P intercept=False
mlflow run . -P intercept=False --no-conda
```
* How to share you experiment??
```bash
just share below four file and ask to run command **mlflow run .**
  1. requirements.txt
  2. train.py
  3. conda.yaml 
  4. MLproject 
````
</p>
</details>
