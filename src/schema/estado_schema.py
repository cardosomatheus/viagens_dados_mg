from pyspark.sql.types import StructType, StringType, StructField, IntegerType


ESTADO_SCHEMA = StructType([
    StructField('id_estado', IntegerType(), True),
    StructField('nome', StringType(), True)
])
