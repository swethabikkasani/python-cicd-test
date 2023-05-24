# apcdl-ci-cd
This is the test repository to develop strategies around CII/CD for APCDL

# Option 1

## Step 1 Build archive for the environemnt 
- python3 -m venv pyspark_venvsource
- source pyspark_venvsource/bin/activate
- pip3 install -r requirements.txt
- pip3 install venv-pack
- venv-pack -f -o pyspark_venv.tar.gz

## Step 2 zip archive the application code 
zip src/ src.zip

## Step 3 Copy the env tar archive and zip source code to a destination

# Option 2

## Step 1: Build a pypi repo in Jfrog
## Step 2: create a local config with an access key (PASSWORD) generated in Jfrog

```
[distutils]
index-servers = local
[local]
repository: https://repo.jfrogrepo.com/artifactory/api/pypi/python-staging
username: <USERNAME>
password: <PASSWORD>
```
## Step 3: run inside CI-CD the following commands

```
python3 -m pip install --upgrade setuptools
pipenv lock
python3 setup.py bdist_wheel
```
## Step 4: publish the whl file to Jfrog repo

## Step 5: create virtual env environment with installation of requirements from txt and jfrog

```
python3 -m venv pyspark_venvsource
source pyspark_venvsource/bin/activate
pip3 install -r requirements.txt
pip install --no-cache-dir ${library-developed}==0.0.x
pip3 install venv-pack
venv-pack -f -o pyspark_venv.tar.gz
```

- pip install --no-cache-dir dataplatform==0.0.6
- remove dist/ and the .egg info

### spark submit example
```
export PYSPARK_PYTHON=/bin/python3
export PYSPARK_DRIVER_PYTHON=python3
conf_path=$HOME/conf/dev/aws.conf
spark-submit \
--conf spark.driverEnv.PYSPARK_DRIVER_PYTHON=./environment/bin/python \
--conf spark.driverEnv.PYSPARK_PYTHON=./environment/bin/python \
--conf spark.executorEnv.PYSPARK_PYTHON=./environment/bin/python \
--archives $HOME/apcdl/rave_client/pyspark_venv_v3.tar.gz app_entrypoint_app.py --app_name $1 --conf_path $conf_path
```

entry point script should be in the same location with spark-submit bash script
