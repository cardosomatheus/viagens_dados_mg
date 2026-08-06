from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.cargo_scdp_schema import CARGO_SCDP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class CargoScdpExtrator(BaseExtrator):
    schema = CARGO_SCDP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.CARGO_SCDP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_cargo_scdp.csv.gz')
        self.CARGO_SCDP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_cargo_scdp.parquet')

    def extrair_cargo_scdp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.CARGO_SCDP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_cargo_scdp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.CARGO_SCDP_BRONZE
        )


if __name__ == '__main__':
    cargoscdp = CargoScdpExtrator()
    cargoscdp_df = cargoscdp.extrair_cargo_scdp()
    cargoscdp_df.show()
    cargoscdp.salvar_cargo_scdp(cargoscdp_df)
