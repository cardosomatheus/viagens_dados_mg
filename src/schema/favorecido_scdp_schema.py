from pyspark.sql.types import StructType, StructField, IntegerType, StringType


FAVORECIDO_SCDP_SCHEMA = StructType([
    StructField('id_favorecido', IntegerType(), True),
    StructField('nr_cpf_anonimizado', StringType(), True),
    StructField('masp', StringType(), True),
    StructField('nome_anonimizado', StringType(), True)
])
