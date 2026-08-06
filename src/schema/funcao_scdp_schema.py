from pyspark.sql.types import StructType, StructField, IntegerType, StringType


FUNCAO_SCDP_SCHEMA = StructType([
    StructField('id_funcao', IntegerType(), True),
    StructField('nome', StringType(), True)
])
