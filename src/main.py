from src.extract.pais_extrator import PaisExtrator
from src.extract.estado_extrator import EstadoExtrator

from src.tranform.pais_transformador import PaisTransformador
from src.tranform.estado_transformador import EstadoTransformador


if __name__ == '__main__':
    # Executar ETL Países
    paisExtrator = PaisExtrator()
    paisdf = paisExtrator.extrair_pais()
    paisdf.show()
    paisExtrator.salvar_pais(paisdf)

    paisTransformador = PaisTransformador()    
    paisdf = paisTransformador.extrair_pais()
    paisdf = paisTransformador.tranformar_pais(df_dataframe=paisdf)
    paisTransformador.salvar_pais(paisdf)

    # Executar ETL Estados
    estadoExtrator = EstadoExtrator()
    estadodf = estadoExtrator.extrair_estado()    
    estadoExtrator.salvar_estado(estadodf) if hasattr(estadoExtrator, 'salvar_estado') else None

    estadoTransformador = EstadoTransformador()
    estadodf = estadoTransformador.extrair_estado()
    estadodf = estadoTransformador.transformar_estado(df_dataframe=estadodf)
    estadoTransformador.salvar_estado(estadodf)
    print('FIM')