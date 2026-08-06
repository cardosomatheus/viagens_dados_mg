from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.fonte_schema import FONTE_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class FonteExtrator(BaseExtrator):
    schema = FONTE_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.FONTE_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_fonte.csv.gz')
        self.FONTE_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_fonte.parquet')

    def extrair_fonte(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.FONTE_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_fonte(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.FONTE_BRONZE
        )


if __name__ == '__main__':
    fonte = FonteExtrator()
    fonte_df = fonte.extrair_fonte()
    fonte_df.show()
    fonte.salvar_fonte(fonte_df)
