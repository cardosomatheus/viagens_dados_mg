from pyspark.sql.dataframe import DataFrame
from pyspark.sql import functions as f
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.estado_schema import ESTADO_SCHEMA
from src.utils.logger import setup_logger
from dotenv import load_dotenv
import os
import logging


load_dotenv()


class EstadoTransformador(BaseExtrator):

    schema = ESTADO_SCHEMA
            
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__()
        self.writer = BaseWriter()
        self.ESTADO_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_estado.parquet')
        self.ESTADO_SILVER = os.path.join(os.getenv('PASTA_SILVER'), 'dm_estado.parquet')
    

    def extrair_estado(self) -> DataFrame:
        return self.ler_parquet(arquivo_parquet=self.ESTADO_BRONZE, schema=self.schema)


    def __limpar_nome_estado(self, df_dataframe: DataFrame) -> DataFrame:
        sem_acento = f.translate(
            f.col("nome"),
            "ÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇáàãâäéèêëíìîïóòõôöúùûüç",
            "AAAAAEEEEIIIIOOOOOUUUUCaaaaaeeeeiiiiooooouuuuc"
        )
        return df_dataframe.withColumn(
            "nome_limpo", 
            f.upper(f.trim(f.regexp_replace(sem_acento, "[^a-zA-Z0-9\\s]", "")))
        )

    def __definir_sigla_estado(self, df_dataframe: DataFrame) -> DataFrame:
        case_sigla_estado = """
            CASE id_estado
                WHEN 58 THEN 'AC'
                WHEN 59 THEN 'AL'
                WHEN 60 THEN 'AM'
                WHEN 61 THEN 'AP'
                WHEN 62 THEN 'BA'
                WHEN 63 THEN 'CE'
                WHEN 64 THEN 'DF'
                WHEN 65 THEN 'ES'
                WHEN 66 THEN 'GO'
                WHEN 67 THEN 'MA'
                WHEN 68 THEN 'MG'
                WHEN 69 THEN 'MS'
                WHEN 70 THEN 'MT'
                WHEN 71 THEN 'PA'
                WHEN 72 THEN 'PB'
                WHEN 73 THEN 'PE'
                WHEN 74 THEN 'PI'
                WHEN 75 THEN 'PR'
                WHEN 76 THEN 'RJ'
                WHEN 77 THEN 'RN'
                WHEN 78 THEN 'RO'
                WHEN 79 THEN 'RR'
                WHEN 80 THEN 'RS'
                WHEN 81 THEN 'SC'
                WHEN 82 THEN 'SE'
                WHEN 83 THEN 'SP'
                WHEN 84 THEN 'TO'
            END
        """
        return df_dataframe.withColumn('sigla_estado', f.expr(case_sigla_estado))

    def transformar_estado(self, df_dataframe: DataFrame) -> DataFrame:
        self.logger.info('🔄 Transformando dados de ESTADOS.')
        df_dataframe = self.__definir_sigla_estado(df_dataframe=df_dataframe)
        df_dataframe = self.__limpar_nome_estado(df_dataframe=df_dataframe)
        self.logger.info('🔄 Transformações em ESTADOS concluídas com sucesso!!!')
        return df_dataframe
    
    def salvar_estado(self, df_dataframe: DataFrame) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.ESTADO_SILVER
        )


if __name__ == '__main__':
    estado = EstadoTransformador()
    estadodf = estado.extrair_estado()
    estadodf = estado.transformar_estado(df_dataframe=estadodf)
    estado.salvar_estado(estadodf)
    estadodf.show(30)
