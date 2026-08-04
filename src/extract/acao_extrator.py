from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.acao_schema import ACAO_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class AcaoExtrator(BaseExtrator):
    schema = ACAO_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter() 
        self.ACAO_RAW = os.path.join(os.getenv('PASTA_RAW'), "dm_acao.csv.gz")
        self.ACAO_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), "dm_acao.parquet")


    def extrair_acao(self) -> DataFrame:
        return self.ler_csv(
                    arquivo_csv=self.ACAO_RAW,
                    separador=';',
                    schema=ACAO_SCHEMA
                )
    
    def salvar_acao(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
                        df_dataframe=df_dataframe,
                        path_salvar=self.ACAO_BRONZE
                    )


if __name__ == '__main__':
    acao = AcaoExtrator()
    acao_df = acao.extrair_acao()
    acao_df.show()
    acao.salvar_acao(acao_df)