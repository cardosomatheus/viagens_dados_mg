from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.cidade_schema import CIDADE_SCHEMA
import os

class CidadeExtrator(BaseExtrator):
    schema = CIDADE_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.CIDADE_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_cidade.csv.gz')
        self.CIDADE_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_cidade.parquet')

    def extrair_cidade(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.CIDADE_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_cidade(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.CIDADE_BRONZE
        )


if __name__ == '__main__':
    cidade = CidadeExtrator()
    cidadedf = cidade.extrair_cidade()
    cidadedf.show() 
    cidade.salvar_cidade(cidadedf)