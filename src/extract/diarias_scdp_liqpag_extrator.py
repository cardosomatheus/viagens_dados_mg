from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.diarias_scdp_liqpag_schema import DIARIAS_SCDP_LIQPAG_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class DiariasScdpLiqpagExtrator(BaseExtrator):
    schema = DIARIAS_SCDP_LIQPAG_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.DIARIAS_SCDP_LIQPAG_RAW = os.path.join(os.getenv('PASTA_RAW'), 'ft_diarias_scdp_liqpag.csv.gz')
        self.DIARIAS_SCDP_LIQPAG_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'ft_diarias_scdp_liqpag.parquet')

    def extrair_diarias_scdp_liqpag(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.DIARIAS_SCDP_LIQPAG_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_diarias_scdp_liqpag(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.DIARIAS_SCDP_LIQPAG_BRONZE
        )


if __name__ == '__main__':
    diariasscdpliqpag = DiariasScdpLiqpagExtrator()
    diariasscdpliqpag_df = diariasscdpliqpag.extrair_diarias_scdp_liqpag()
    diariasscdpliqpag_df.show()
    diariasscdpliqpag.salvar_diarias_scdp_liqpag(diariasscdpliqpag_df)
