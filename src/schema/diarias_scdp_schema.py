from pyspark.sql.types import StructType, StructField, DoubleType, IntegerType, StringType


DIARIAS_SCDP_SCHEMA = StructType([
    StructField('id_tempo', IntegerType(), True),
    StructField('id_favorecido', IntegerType(), True),
    StructField('id_cargo', IntegerType(), True),
    StructField('id_funcao_scdp', IntegerType(), True),
    StructField('id_orgao', IntegerType(), True),
    StructField('id_pais_origem', IntegerType(), True),
    StructField('id_estado_origem', IntegerType(), True),
    StructField('id_cidade_origem', IntegerType(), True),
    StructField('id_pais_destino', IntegerType(), True),
    StructField('id_estado_destino', IntegerType(), True),
    StructField('id_cidade_destino', IntegerType(), True),
    StructField('id_documento_viagem', IntegerType(), True),
    StructField('id_tipo_viagem', IntegerType(), True),
    StructField('id_tipo_viajante', IntegerType(), True),
    StructField('id_meio_transporte', IntegerType(), True),
    StructField('id_motivo', IntegerType(), True),
    StructField('ordem_trecho', IntegerType(), True),
    StructField('ano_particao', IntegerType(), True),
    StructField('dt_inicio_trecho', StringType(), True),
    StructField('dt_fim_trecho', StringType(), True),
    StructField('qt_diaria', DoubleType(), True),
    StructField('vr_diaria', DoubleType(), True),
    StructField('vr_passagem', DoubleType(), True)
])
