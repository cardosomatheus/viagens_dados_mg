from pyspark.sql.types import StructType, StringType, StructField, IntegerType
from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from dotenv import load_dotenv
import os

load_dotenv()

class PaisExtrator(BaseExtrator):

    schema = StructType([
                StructField('id_pais', IntegerType(), True),
                StructField('nome', StringType(), True)
            ])
            
    def __init__(self):
        super().__init__()
        self.writer = BaseWriter() 
        self.ARQUIVO_PAIS = os.path.join(os.getenv('PASTA_RAW'), "dm_pais.csv.gz")
        self.ARQUIVO_PAIS_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), "dm_pais.parquet")


    def extrair_pais(self) -> DataFrame:
        return self.ler_csv(
                    arquivo_csv=self.ARQUIVO_PAIS,
                    separador=';',
                    schema=self.schema
                )
    
    def salvar_pais(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
                        df_dataframe=df_dataframe,
                        path_salvar=self.ARQUIVO_PAIS_BRONZE
                    )


if __name__ == '__main__':
    pais = PaisExtrator()
    paisdf = pais.extrair_pais()
    paisdf.show()
    pais.salvar_pais(paisdf)