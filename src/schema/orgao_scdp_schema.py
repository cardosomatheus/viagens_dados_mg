from pyspark.sql.types import StructType, StructField, IntegerType, StringType


ORGAO_SCDP_SCHEMA = StructType([
    StructField('id_orgao', IntegerType(), True),
    StructField('cd_orgao', StringType(), True),
    StructField('nome', StringType(), True)
])
