from dataclasses import dataclass
from pyspark.sql import SparkSession



@dataclass
class SparkInitializer:

    def create_spark_session(self, flow_name) -> SparkSession:

        spark = SparkSession \
            .builder \
            .appName(f"Test_app") \
            .getOrCreate()

        return spark
