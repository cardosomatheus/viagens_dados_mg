from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import StructType, StringType, StructField, IntegerType
from pyspark.sql import functions as f
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.utils.logger import setup_logger
from dotenv import load_dotenv
import os
import logging


load_dotenv()


class PaisTransformador(BaseExtrator):

    schema = StructType([
                StructField('id_pais', IntegerType(), True),
                StructField('nome', StringType(), True)
            ])
            
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__()
        self.writer = BaseWriter()
        self.PAIS_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_pais.parquet')
        self.PAIS_SILVER = os.path.join(os.getenv('PASTA_SILVER'), 'dm_pais.parquet')
    

    def extrair_pais(self) -> DataFrame:
        return self.ler_parquet(arquivo_parquet=self.PAIS_BRONZE,schema=self.schema)


    def __limar_nome_pais(self, df_dataframe :DataFrame) -> DataFrame:
        return df_dataframe.withColumn(
            "nome_limpo", 
            f.upper(f.trim(f.regexp_replace(f.col("nome"),"[^a-zA-Z0-9\\s]", "")))
        )

    def __definir_sigla_pais(self, df_dataframe :DataFrame) -> DataFrame:
        case_sigla_pais = """
            CASE id_pais
                WHEN 204 THEN 'BR'
                WHEN 205 THEN 'AG'
                WHEN 206 THEN 'AR'
                WHEN 207 THEN 'BO'
                WHEN 208 THEN 'CL'
                WHEN 209 THEN 'CO'
                WHEN 210 THEN 'EC'
                WHEN 211 THEN 'GF'
                WHEN 212 THEN 'GY'
                WHEN 213 THEN 'PY'
                WHEN 214 THEN 'PE'
                WHEN 215 THEN 'SR'
                WHEN 216 THEN 'UY'
                WHEN 217 THEN 'VE'
                WHEN 218 THEN 'CR'
                WHEN 219 THEN 'JM'
                WHEN 220 THEN 'BB'
                WHEN 221 THEN 'BS'
                WHEN 222 THEN 'CU'
                WHEN 223 THEN 'BZ'
                ELSE NULL 
            END
        """
        return df_dataframe.withColumn('sigla_pais',f.expr(case_sigla_pais))

    def tranformar_pais(self, df_dataframe :DataFrame) -> DataFrame:
        self.logger.info('🔄 Tranformando dados de PAISES.')
        df_dataframe = self.__definir_sigla_pais(df_dataframe=df_dataframe)
        df_dataframe = self.__limar_nome_pais(df_dataframe=df_dataframe)
        return df_dataframe
    
    def salvar_pais(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
                        df_dataframe=df_dataframe,
                        path_salvar=self.PAIS_SILVER
                    )





if __name__ == '__main__':
    pais = PaisTransformador()
    paisdf = pais.extrair_pais()
    paisdf = pais.tranformar_pais(df_dataframe=paisdf)
    pais.salvar_pais(paisdf)
    paisdf.show()

    