from pyspark.sql.types import StructType, StructField, IntegerType, StringType


ITEM_DESP_SCHEMA = StructType([
    StructField('id_item', IntegerType(), True),
    StructField('cd_item', StringType(), True),
    StructField('nome', StringType(), True)
])
