from pyspark.sql.types import StructType, StringType, StructField, IntegerType


ACAO_SCHEMA = StructType([
    StructField('id_acao', IntegerType(), True),
    StructField('nome', StringType(), True)
])
