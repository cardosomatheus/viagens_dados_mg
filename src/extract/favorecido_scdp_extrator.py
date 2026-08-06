from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.favorecido_scdp_schema import FAVORECIDO_SCDP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class FavorecidoScdpExtrator(BaseExtrator):
    schema = FAVORECIDO_SCDP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.FAVORECIDO_SCDP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_favorecido_scdp.csv.gz')
        self.FAVORECIDO_SCDP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_favorecido_scdp.parquet')

    def extrair_favorecido_scdp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.FAVORECIDO_SCDP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_favorecido_scdp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.FAVORECIDO_SCDP_BRONZE
        )


if __name__ == '__main__':
    favorecidoscdp = FavorecidoScdpExtrator()
    favorecidoscdp_df = favorecidoscdp.extrair_favorecido_scdp()
    favorecidoscdp_df.show()
    favorecidoscdp.salvar_favorecido_scdp(favorecidoscdp_df)
