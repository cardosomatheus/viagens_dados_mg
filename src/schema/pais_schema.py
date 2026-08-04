from pyspark.sql.types import StructType, StringType, StructField, IntegerType


PAIS_SCHEMA = StructType([
        StructField('id_pais', IntegerType(), True),
        StructField('nome', StringType(), True)
    ])

