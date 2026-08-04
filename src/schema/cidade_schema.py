from pyspark.sql.types import StructType, StringType, StructField, IntegerType


CIDADE_SCHEMA = StructType([
    StructField('id_cidade', IntegerType(), True),
    StructField('nome', StringType(), True)
])
