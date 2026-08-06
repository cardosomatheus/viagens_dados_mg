from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.meio_transporte_schema import MEIO_TRANSPORTE_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class MeioTransporteExtrator(BaseExtrator):
    schema = MEIO_TRANSPORTE_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.MEIO_TRANSPORTE_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_meio_transporte.csv.gz')
        self.MEIO_TRANSPORTE_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_meio_transporte.parquet')

    def extrair_meio_transporte(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.MEIO_TRANSPORTE_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_meio_transporte(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.MEIO_TRANSPORTE_BRONZE
        )


if __name__ == '__main__':
    meiotransporte = MeioTransporteExtrator()
    meiotransporte_df = meiotransporte.extrair_meio_transporte()
    meiotransporte_df.show()
    meiotransporte.salvar_meio_transporte(meiotransporte_df)
