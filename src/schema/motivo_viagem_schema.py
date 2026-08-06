from pyspark.sql.types import StructType, StructField, IntegerType, StringType


MOTIVO_VIAGEM_SCHEMA = StructType([
    StructField('id_motivo', IntegerType(), True),
    StructField('nome', StringType(), True)
])
