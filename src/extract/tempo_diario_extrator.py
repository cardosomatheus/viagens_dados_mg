from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.tempo_diario_schema import TEMPO_DIARIO_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class TempoDiarioExtrator(BaseExtrator):
    schema = TEMPO_DIARIO_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.TEMPO_DIARIO_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_tempo_diario.csv.gz')
        self.TEMPO_DIARIO_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_tempo_diario.parquet')

    def extrair_tempo_diario(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.TEMPO_DIARIO_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_tempo_diario(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.TEMPO_DIARIO_BRONZE
        )


if __name__ == '__main__':
    tempodiario = TempoDiarioExtrator()
    tempodiario_df = tempodiario.extrair_tempo_diario()
    tempodiario_df.show()
    tempodiario.salvar_tempo_diario(tempodiario_df)
