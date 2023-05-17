from spark_builder.spark_session_builder import SparkInitializer

if __name__ == '__main__':

    spark = SparkInitializer().create_spark_session(flow_name="csv-format-clinical-views")
    columns = ["language", "users_count"]
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
    rdd = spark.sparkContext.parallelize(data)
    dfFromRDD1 = rdd.toDF()
    dfFromRDD1.printSchema()
