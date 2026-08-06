from pyspark.sql.dataframe import DataFrame
from src.base.base_extrator import BaseExtrator
from src.base.base_writer import BaseWriter
from src.schema.item_desp_schema import ITEM_DESP_SCHEMA
from dotenv import load_dotenv
import os

load_dotenv()

class ItemDespExtrator(BaseExtrator):
    schema = ITEM_DESP_SCHEMA

    def __init__(self):
        super().__init__()
        self.writer = BaseWriter()
        self.ITEM_DESP_RAW = os.path.join(os.getenv('PASTA_RAW'), 'dm_item_desp.csv.gz')
        self.ITEM_DESP_BRONZE = os.path.join(os.getenv('PASTA_BRONZE'), 'dm_item_desp.parquet')

    def extrair_item_desp(self) -> DataFrame:
        return self.ler_csv(
            arquivo_csv=self.ITEM_DESP_RAW,
            separador=';',
            schema=self.schema
        )

    def salvar_item_desp(self, df_dataframe) -> None:
        self.writer.salvar_parquet(
            df_dataframe=df_dataframe,
            path_salvar=self.ITEM_DESP_BRONZE
        )


if __name__ == '__main__':
    itemdesp = ItemDespExtrator()
    itemdesp_df = itemdesp.extrair_item_desp()
    itemdesp_df.show()
    itemdesp.salvar_item_desp(itemdesp_df)
