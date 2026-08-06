from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.funcao_desp_schema import FUNCAO_DESP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class FuncaoDespExtrator(BaseExtrator):
    schema = FUNCAO_DESP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.FUNCAO_DESP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_funcao_desp.csv.gz')
        self.FUNCAO_DESP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_funcao_desp.parquet')

    def extrair_funcao_desp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.FUNCAO_DESP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_funcao_desp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.FUNCAO_DESP_BRONZE
        )


if __name__ == '__main__':
    funcaodesp = FuncaoDespExtrator()
    funcaodesp_df = funcaodesp.extrair_funcao_desp()
    funcaodesp_df.show()
    funcaodesp.salvar_funcao_desp(funcaodesp_df)
