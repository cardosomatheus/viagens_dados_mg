from pyspark.sql.types import StructType, StructField, IntegerType, StringType


FUNCAO_DESP_SCHEMA = StructType([
    StructField('id_funcao', IntegerType(), True),
    StructField('ano_exercicio', IntegerType(), True),
    StructField('cd_funcao', StringType(), True),
    StructField('nome', StringType(), True)
])
