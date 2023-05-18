export PYSPARK_PYTHON=/bin/python3
export PYSPARK_DRIVER_PYTHON=python3
conf_path=$HOME/conf/dev/aws.conf
spark-submit \
--conf spark.driverEnv.PYSPARK_DRIVER_PYTHON=./environment/bin/python \
--conf spark.driverEnv.PYSPARK_PYTHON=./environment/bin/python \
--conf spark.executorEnv.PYSPARK_PYTHON=./environment/bin/python \
--archives $HOME/apcdl/rave_client/pyspark_venv_v3.tar.gz app_entrypoint_app.py --app_name $1 --conf_path $conf_path