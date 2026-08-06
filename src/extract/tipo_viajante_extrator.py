from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.tipo_viajante_schema import TIPO_VIAJANTE_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class TipoViajanteExtrator(BaseExtrator):
    schema = TIPO_VIAJANTE_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.TIPO_VIAJANTE_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_tipo_viajante.csv.gz')
        self.TIPO_VIAJANTE_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_tipo_viajante.parquet')

    def extrair_tipo_viajante(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.TIPO_VIAJANTE_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_tipo_viajante(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.TIPO_VIAJANTE_BRONZE
        )


if __name__ == '__main__':
    tipoviajante = TipoViajanteExtrator()
    tipoviajante_df = tipoviajante.extrair_tipo_viajante()
    tipoviajante_df.show()
    tipoviajante.salvar_tipo_viajante(tipoviajante_df)
