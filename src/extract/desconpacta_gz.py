import shutil
import gzip
import os
from pathlib import Path


class DescompactaPastas:
    def __init__(self) -> None:
        pass


    def desconpacta_gzip(self,  pasta_zipada) -> None:
        nome_arquivo = os.path.basename(pasta_zipada).replace('.gz', '')
        caminho_destino = os.path.join('data/bronze', nome_arquivo)
        print(f'Descompactando a pasta: {pasta_zipada}...')

        with gzip.open(pasta_zipada, 'rb') as arquivo_zipado:
            with open(caminho_destino, 'wb') as arquivo_descompactado:
                shutil.copyfileobj(arquivo_zipado, arquivo_descompactado)


    def desconpacta_varios_gzip(self, pasta_com_gzips) -> None:
        for pasta_zip in Path(pasta_com_gzips).glob('*.gz'):
            self.desconpacta_gzip(pasta_zipada=pasta_zip)


if __name__ == '__main__':

    unzip_gz = DescompactaPastas()
    unzip_gz.desconpacta_varios_gzip('data/raw/')