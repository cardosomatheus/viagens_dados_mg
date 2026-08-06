from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.programa_schema import PROGRAMA_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class ProgramaExtrator(BaseExtrator):
    schema = PROGRAMA_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.PROGRAMA_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_programa.csv.gz')
        self.PROGRAMA_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_programa.parquet')

    def extrair_programa(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.PROGRAMA_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_programa(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.PROGRAMA_BRONZE
        )


if __name__ == '__main__':
    programa = ProgramaExtrator()
    programa_df = programa.extrair_programa()
    programa_df.show()
    programa.salvar_programa(programa_df)
