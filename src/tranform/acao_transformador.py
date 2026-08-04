from pyspark.sql.dataframe import DataFrame
from pyspark.sql import functions as f
from pyspark.sql.types import StringType
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.acao_schema import ACAO_SCHEMA

from src.utils.logger import setup_logger
from dotenv import load_dotenv
import os
import logging
from num2words import num2words

load_dotenv()


class AcaoTransformador(BaseExtrator):

    schema = ACAO_SCHEMA
            
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__()
        self.writer = BaseWriter()
        self.ACAO_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_acao.parquet')
        self.ACAO_SILVER = os.path.join(os.getenv('PASTA_SILVER'), 'dm_acao.parquet')
    

    def extrair_acao(self) -> DataFrame:
        return self.ler_parquet(arquivo_parquet=self.ACAO_BRONZE, schema=self.schema)

    def __ano_por_extenso(self, df_dataframe):
        numero_para_palavra_udf = f.udf(
            lambda x: num2words(int(x), lang='pt_BR') if x is not None and str(x).isdigit() else None,
            StringType()
        )

        return df_dataframe.withColumn(
            "ano_extenso", 
            numero_para_palavra_udf(f.col('nome'))
        )

    def transformar_acao(self, df_dataframe: DataFrame) -> DataFrame:
        self.logger.info('🔄 Transformando dados de AÇÕES.')
        df_dataframe = self.__ano_por_extenso(df_dataframe=df_dataframe)
        self.logger.info('🔄 Transformações em AÇÕES concluídas com sucesso!!!')
        return df_dataframe
    
    def salvar_acao(self, df_dataframe: DataFrame) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.ACAO_SILVER
        )


if __name__ == '__main__':
    acao = AcaoTransformador()
    acao_df = acao.extrair_acao()
    acao_df = acao.transformar_acao(df_dataframe=acao_df)
    acao.salvar_acao(acao_df)
    acao_df.show(30)