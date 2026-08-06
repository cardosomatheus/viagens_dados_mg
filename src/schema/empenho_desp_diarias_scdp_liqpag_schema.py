from pyspark.sql.types import StructType, StructField, DoubleType, IntegerType, StringType


EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_SCHEMA = StructType([
    StructField('id_empenho', IntegerType(), True),
    StructField('ano_exercicio', IntegerType(), True),
    StructField('nr_empenho', StringType(), True),
    StructField('dt_empenho', StringType(), True),
    StructField('unidade_executora', StringType(), True),
    StructField('tipo_empenho', StringType(), True),
    StructField('vr_empenho', DoubleType(), True),
    StructField('cd_uni_prog_gasto', IntegerType(), True),
    StructField('uni_prog_gasto', StringType(), True)
])
