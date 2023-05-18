#!/bin/bash

export PYSPARK_PYTHON=/bin/python3
spark-submit \
--conf spark.archives=$HOME/apcdl/test_app/pyspark_venv.tar.gz \
--conf spark.driverEnv.PYSPARK_DRIVER_PYTHON=./environment/bin/python \
--conf spark.driverEnv.PYSPARK_PYTHON=./environment/bin/python \
--conf spark.executorEnv.PYSPARK_PYTHON=./environment/bin/python \
--conf spark.submit.pyFiles=$HOME/apcdl/test_app/src_app.zip $HOME/apcdl/test_app/app_entrypoint_spark.py --app_name $1