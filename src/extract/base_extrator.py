import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


load_dotenv()

class BaseExtrator:
    def __init__(self) -> None:
        self.PASTA_RAW = os.getenv('PASTA_RAW')
        self.PASTA_BRONZE = os.getenv('PASTA_BRONZE')

    def ler_csv(self, arquivo_csv, separador: str = ';') -> DataFrame:
        spark = SparkSession.builder.getOrCreate()
        caminho = os.path.join(self.PASTA_BRONZE, arquivo_csv)
        return spark.read.csv(caminho, header=True, sep=separador, inferSchema=True)


if __name__ == '__main__':
    bs = BaseExtrator()
    data = bs.ler_csv(arquivo_csv='dm_pais.csv',separador=';').show(10)

