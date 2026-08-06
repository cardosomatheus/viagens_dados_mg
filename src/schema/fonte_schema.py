from pyspark.sql.types import StructType, StructField, IntegerType, StringType


FONTE_SCHEMA = StructType([
    StructField('id_fonte', IntegerType(), True),
    StructField('cd_fonte', StringType(), True),
    StructField('nome', StringType(), True)
])
