from pyspark.sql.types import StructType, StructField, IntegerType, StringType


CARGO_SCDP_SCHEMA = StructType([
    StructField('id_cargo', IntegerType(), True),
    StructField('nome', StringType(), True)
])
