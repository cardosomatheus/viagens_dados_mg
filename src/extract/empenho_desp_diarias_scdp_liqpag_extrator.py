from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.empenho_desp_diarias_scdp_liqpag_schema import EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class EmpenhoDespDiariasScdpLiqpagExtrator(BaseExtrator):
    schema = EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_empenho_desp_diarias_scdp_liqpag.csv.gz')
        self.EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_empenho_desp_diarias_scdp_liqpag.parquet')

    def extrair_empenho_desp_diarias_scdp_liqpag(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_empenho_desp_diarias_scdp_liqpag(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.EMPENHO_DESP_DIARIAS_SCDP_LIQPAG_BRONZE
        )


if __name__ == '__main__':
    empenhodespdiariasscdpliqpag = EmpenhoDespDiariasScdpLiqpagExtrator()
    empenhodespdiariasscdpliqpag_df = empenhodespdiariasscdpliqpag.extrair_empenho_desp_diarias_scdp_liqpag()
    empenhodespdiariasscdpliqpag_df.show()
    empenhodespdiariasscdpliqpag.salvar_empenho_desp_diarias_scdp_liqpag(empenhodespdiariasscdpliqpag_df)
