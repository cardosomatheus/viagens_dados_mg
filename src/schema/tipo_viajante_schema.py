from pyspark.sql.types import StructType, StructField, IntegerType, StringType


TIPO_VIAJANTE_SCHEMA = StructType([
    StructField('id_tipo_viajante', IntegerType(), True),
    StructField('nome', StringType(), True)
])
