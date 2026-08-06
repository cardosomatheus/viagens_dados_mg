from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.motivo_viagem_schema import MOTIVO_VIAGEM_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class MotivoViagemExtrator(BaseExtrator):
    schema = MOTIVO_VIAGEM_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.MOTIVO_VIAGEM_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_motivo_viagem.csv.gz')
        self.MOTIVO_VIAGEM_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_motivo_viagem.parquet')

    def extrair_motivo_viagem(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.MOTIVO_VIAGEM_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_motivo_viagem(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.MOTIVO_VIAGEM_BRONZE
        )


if __name__ == '__main__':
    motivoviagem = MotivoViagemExtrator()
    motivoviagem_df = motivoviagem.extrair_motivo_viagem()
    motivoviagem_df.show()
    motivoviagem.salvar_motivo_viagem(motivoviagem_df)
