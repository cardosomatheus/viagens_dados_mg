from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.tipo_viagem_schema import TIPO_VIAGEM_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class TipoViagemExtrator(BaseExtrator):
    schema = TIPO_VIAGEM_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.TIPO_VIAGEM_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_tipo_viagem.csv.gz')
        self.TIPO_VIAGEM_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_tipo_viagem.parquet')

    def extrair_tipo_viagem(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.TIPO_VIAGEM_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_tipo_viagem(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.TIPO_VIAGEM_BRONZE
        )


if __name__ == '__main__':
    tipoviagem = TipoViagemExtrator()
    tipoviagem_df = tipoviagem.extrair_tipo_viagem()
    tipoviagem_df.show()
    tipoviagem.salvar_tipo_viagem(tipoviagem_df)
