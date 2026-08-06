from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.diarias_scdp_schema import DIARIAS_SCDP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class DiariasScdpExtrator(BaseExtrator):
    schema = DIARIAS_SCDP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.DIARIAS_SCDP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'ft_diarias_scdp.csv.gz')
        self.DIARIAS_SCDP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'ft_diarias_scdp.parquet')

    def extrair_diarias_scdp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.DIARIAS_SCDP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_diarias_scdp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.DIARIAS_SCDP_BRONZE
        )


if __name__ == '__main__':
    diariasscdp = DiariasScdpExtrator()
    diariasscdp_df = diariasscdp.extrair_diarias_scdp()
    diariasscdp_df.show()
    diariasscdp.salvar_diarias_scdp(diariasscdp_df)
