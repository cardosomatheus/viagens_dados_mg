from pyspark.sql.types import StructType, StructField, IntegerType, StringType


TIPO_VIAGEM_SCHEMA = StructType([
    StructField('id_tipo_viagem', IntegerType(), True),
    StructField('nome', StringType(), True)
])
