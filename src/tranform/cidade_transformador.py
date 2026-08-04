from pyspark.sql.dataframe import DataFrame
from pyspark.sql import functions as f
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.cidade_schema import CIDADE_SCHEMA
from src.utils.logger import setup_logger
from dotenv import load_dotenv
import os
import logging


load_dotenv()


class CidadeTransformador(BaseExtrator):

    schema = CIDADE_SCHEMA
            
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__()
        self.writer = BaseWriter()
        self.CIDADE_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_cidade.parquet')
        self.CIDADE_SILVER = os.path.join(os.getenv('PASTA_SILVER'), 'dm_cidade.parquet')
    

    def extrair_cidade(self) -> DataFrame:
        return self.ler_parquet(arquivo_parquet=self.CIDADE_BRONZE, schema=self.schema)


    def __limpar_nome_cidade(self, df_dataframe: DataFrame) -> DataFrame:
        sem_acento = f.translate(
            f.col("nome"),
            "ÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇáàãâäéèêëíìîïóòõôöúùûüç",
            "AAAAAEEEEIIIIOOOOOUUUUCaaaaaeeeeiiiiooooouuuuc"
        )
        return df_dataframe.withColumn(
            "nome_limpo", 
            f.upper(f.trim(f.regexp_replace(sem_acento, "[^a-zA-Z0-9\\s]", "")))
        )

    def transformar_cidade(self, df_dataframe: DataFrame) -> DataFrame:
        self.logger.info('🔄 Transformando dados de CIDADES.')
        df_dataframe = self.__limpar_nome_cidade(df_dataframe=df_dataframe)
        self.logger.info('🔄 Transformações em CIDADES concluídas com sucesso!!!')
        return df_dataframe
    
    def salvar_cidade(self, df_dataframe: DataFrame) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.CIDADE_SILVER
        )


if __name__ == '__main__':
    cidade = CidadeTransformador()
    cidadedf = cidade.extrair_cidade()
    cidadedf = cidade.transformar_cidade(df_dataframe=cidadedf)
    cidade.salvar_cidade(cidadedf)
    cidadedf.show(30)