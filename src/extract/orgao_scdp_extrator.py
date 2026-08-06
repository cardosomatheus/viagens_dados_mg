from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.orgao_scdp_schema import ORGAO_SCDP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class OrgaoScdpExtrator(BaseExtrator):
    schema = ORGAO_SCDP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.ORGAO_SCDP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_orgao_scdp.csv.gz')
        self.ORGAO_SCDP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_orgao_scdp.parquet')

    def extrair_orgao_scdp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.ORGAO_SCDP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_orgao_scdp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.ORGAO_SCDP_BRONZE
        )


if __name__ == '__main__':
    orgaoscdp = OrgaoScdpExtrator()
    orgaoscdp_df = orgaoscdp.extrair_orgao_scdp()
    orgaoscdp_df.show()
    orgaoscdp.salvar_orgao_scdp(orgaoscdp_df)
