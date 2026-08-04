from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.pais_schema import PAIS_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class PaisExtrator(BaseExtrator):
    schema = PAIS_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter() 
        self.PAIS_RAW = os.path.join(os.getenv('PASTA_RAW'), "dm_pais.csv.gz")
        self.PAIS_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), "dm_pais.parquet")


    def extrair_pais(self) -> DataFrame:
        return self.ler_csv(
                    arquivo_csv=self.PAIS_RAW,
                    separador=';',
                    schema=self.schema
                )
    
    def salvar_pais(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
                        df_dataframe=df_dataframe,
                        path_salvar=self.PAIS_BRONZE
                    )


if __name__ == '__main__':
    pais = PaisExtrator()
    paisdf = pais.extrair_pais()
    paisdf.show()
    pais.salvar_pais(paisdf)