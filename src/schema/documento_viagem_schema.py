from pyspark.sql.types import StructType, StructField, IntegerType, StringType


DOCUMENTO_VIAGEM_SCHEMA = StructType([
    StructField('id_documento_viagem', IntegerType(), True),
    StructField('nr_documento', StringType(), True),
    StructField('dt_viagem_inicio', StringType(), True),
    StructField('dt_viagem_fim', StringType(), True),
    StructField('motivo', StringType(), True)
])
