from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.funcao_scdp_schema import FUNCAO_SCDP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class FuncaoScdpExtrator(BaseExtrator):
    schema = FUNCAO_SCDP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.FUNCAO_SCDP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_funcao_scdp.csv.gz')
        self.FUNCAO_SCDP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_funcao_scdp.parquet')

    def extrair_funcao_scdp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.FUNCAO_SCDP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_funcao_scdp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.FUNCAO_SCDP_BRONZE
        )


if __name__ == '__main__':
    funcaoscdp = FuncaoScdpExtrator()
    funcaoscdp_df = funcaoscdp.extrair_funcao_scdp()
    funcaoscdp_df.show()
    funcaoscdp.salvar_funcao_scdp(funcaoscdp_df)
