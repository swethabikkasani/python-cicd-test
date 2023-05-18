from src_spark_app.spark_builder.spark_session_builder import SparkInitializer
from src_spark_app.config_read.read_conf_file import read_config_file


def start_app(name_app: str, config_path):
    spark = SparkInitializer().create_spark_session()
    columns = ["language", "users_count"]
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
    rdd = spark.sparkContext.parallelize(data)
    dfFromRDD1 = rdd.toDF()
    dfFromRDD1.printSchema()
    key, arn = read_config_file(config_path)
    print("App Name: - " + name_app)
    print("KEY: - " + key)
    print("ARN: - " + arn)
