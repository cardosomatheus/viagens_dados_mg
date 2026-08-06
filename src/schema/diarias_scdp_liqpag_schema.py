from pyspark.sql.types import StructType, StructField, DoubleType, IntegerType, StringType


DIARIAS_SCDP_LIQPAG_SCHEMA = StructType([
    StructField('id_documento_viagem', IntegerType(), True),
    StructField('id_empenho', IntegerType(), True),
    StructField('id_programa', IntegerType(), True),
    StructField('id_funcao', IntegerType(), True),
    StructField('id_fonte', IntegerType(), True),
    StructField('id_item', IntegerType(), True),
    StructField('id_acao', IntegerType(), True),
    StructField('fl_passagem', IntegerType(), True),
    StructField('nr_liquidacao', IntegerType(), True),
    StructField('nr_pagamento', IntegerType(), True),
    StructField('dt_liquidacao', StringType(), True),
    StructField('dt_pagamento', StringType(), True),
    StructField('vr_devolvido', DoubleType(), True),
    StructField('vr_liqpag', DoubleType(), True)
])
