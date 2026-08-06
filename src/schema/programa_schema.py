from pyspark.sql.types import StructType, StructField, IntegerType, StringType


PROGRAMA_SCHEMA = StructType([
    StructField('id_programa', IntegerType(), True),
    StructField('ano_exercicio', IntegerType(), True),
    StructField('cd_programa', StringType(), True),
    StructField('nome', StringType(), True)
])
