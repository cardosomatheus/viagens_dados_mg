from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.documento_viagem_schema import DOCUMENTO_VIAGEM_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class DocumentoViagemExtrator(BaseExtrator):
    schema = DOCUMENTO_VIAGEM_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.DOCUMENTO_VIAGEM_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_documento_viagem.csv.gz')
        self.DOCUMENTO_VIAGEM_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_documento_viagem.parquet')

    def extrair_documento_viagem(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.DOCUMENTO_VIAGEM_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_documento_viagem(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.DOCUMENTO_VIAGEM_BRONZE
        )


if __name__ == '__main__':
    documentoviagem = DocumentoViagemExtrator()
    documentoviagem_df = documentoviagem.extrair_documento_viagem()
    documentoviagem_df.show()
    documentoviagem.salvar_documento_viagem(documentoviagem_df)
