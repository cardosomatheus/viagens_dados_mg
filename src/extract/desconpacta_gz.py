import shutil
import gzip
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

class DescompactaPastas:
    def __init__(self) -> None:
        self.PASTA_RAW = os.getenv('PASTA_RAW')
        self.PASTA_BRONZE = os.getenv('PASTA_BRONZE')


    def desconpacta_gzip(self,  pasta_zipada) -> None:
        print(f'Descompactando a pasta: {pasta_zipada}')
        nome_arquivo = os.path.basename(pasta_zipada).replace('.gz', '')
        caminho_destino = os.path.join(self.PASTA_BRONZE, nome_arquivo)

        with gzip.open(pasta_zipada, 'rb') as arquivo_zipado:
            with open(caminho_destino, 'wb') as arquivo_descompactado:
                shutil.copyfileobj(arquivo_zipado, arquivo_descompactado)


    def desconpacta_varios_gzip(self) -> None:
        for pasta_zip in Path(self.PASTA_RAW).glob('*.gz'):
            self.desconpacta_gzip(pasta_zipada=pasta_zip)


if __name__ == '__main__':
    unzip_gz = DescompactaPastas()
    unzip_gz.desconpacta_varios_gzip()