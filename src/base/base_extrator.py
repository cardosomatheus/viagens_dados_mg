import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from src.utils.logger import setup_logger
import logging

load_dotenv()
setup_logger()

class BaseExtrator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)


    def ler_csv(self, arquivo_csv, separador: str = ';', schema = None) -> DataFrame:
        spark = SparkSession.builder.getOrCreate()

        self.logger.info(f"📖 Iniciando a leitura do CSV: {arquivo_csv}")
        df = spark.read.csv(
                    arquivo_csv,
                    header=True, 
                    sep=separador, 
                    schema=schema, 
                    inferSchema = True
            )
        self.logger.info(f"✅ Leitura do CSV concluída: {arquivo_csv}")
        return df

    def ler_parquet(self, arquivo_parquet, schema) -> DataFrame:
        self.logger.info(f"📖 Iniciando a leitura do PARQUET: {arquivo_parquet}")
        spark = SparkSession.builder.getOrCreate()
        df = spark.read.schema(schema).parquet(arquivo_parquet)
        self.logger.info(f"✅ Leitura do PARQUET concluída: {arquivo_parquet}")
        return df

if __name__ == '__main__':
    bs = BaseExtrator()
    data = bs.ler_csv(arquivo_csv='data/raw/dm_pais.csv.gz',separador=';').show(10)

