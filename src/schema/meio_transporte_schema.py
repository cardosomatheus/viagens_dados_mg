from pyspark.sql.types import StructType, StructField, IntegerType, StringType


MEIO_TRANSPORTE_SCHEMA = StructType([
    StructField('id_meio_transporte', IntegerType(), True),
    StructField('nome', StringType(), True)
])
