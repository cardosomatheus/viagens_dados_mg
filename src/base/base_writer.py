from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession
import logging
from src.utils.logger import setup_logger


class BaseWriter:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)


    def salvar_parquet(self, df_dataframe:DataFrame, path_salvar:str) -> None:        
        self.logger.info(f"💾 Salvando DataFrame em:  {path_salvar}")
        spark = SparkSession.builder.getOrCreate()
        df_dataframe.write.mode('overwrite').parquet(path_salvar)
        self.logger.info(f"✅ DataFrame salvo com sucesso!!!.")

    

if __name__ == '__main__':
    bw = BaseWriter()
    bw.salvar_parquet(df_dataframe=None, path_salvar="data/trusted/teste.parquet")
