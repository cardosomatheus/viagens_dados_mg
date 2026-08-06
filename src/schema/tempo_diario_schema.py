from pyspark.sql.types import StructType, StructField, IntegerType, StringType


TEMPO_DIARIO_SCHEMA = StructType([
    StructField('id_tempo', IntegerType(), True),
    StructField('data_iso', IntegerType(), True),
    StructField('dia', IntegerType(), True),
    StructField('mes', IntegerType(), True),
    StructField('ano', IntegerType(), True),
    StructField('data_formatada', StringType(), True)
])
