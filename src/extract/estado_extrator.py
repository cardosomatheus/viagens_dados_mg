from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.estado_schema import ESTADO_SCHEMA
import os

class EstadoExtrator(BaseExtrator):
    schema = ESTADO_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.ESTADO_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_estado.csv.gz')
        self.ESTADO_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_estado.parquet')

    def extrair_estado(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.ESTADO_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_estado(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.ESTADO_BRONZE
        )


if __name__ == '__main__':
    estado = EstadoExtrator()
    estadodf = estado.extrair_estado()
    estadodf.show()
    estado.salvar_estado(estadodf)