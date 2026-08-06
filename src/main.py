from src.extract.pais_extrator import PaisExtrator
from src.extract.estado_extrator import EstadoExtrator
from src.extract.cidade_extrator import CidadeExtrator
from src.extract.acao_extrator import AcaoExtrator
from src.extract.cargo_scdp_extrator import CargoScdpExtrator
from src.extract.documento_viagem_extrator import DocumentoViagemExtrator
from src.extract.empenho_desp_diarias_scdp_liqpag_extrator import EmpenhoDespDiariasScdpLiqpagExtrator
from src.extract.favorecido_scdp_extrator import FavorecidoScdpExtrator
from src.extract.fonte_extrator import FonteExtrator
from src.extract.funcao_desp_extrator import FuncaoDespExtrator
from src.extract.funcao_scdp_extrator import FuncaoScdpExtrator
from src.extract.item_desp_extrator import ItemDespExtrator
from src.extract.meio_transporte_extrator import MeioTransporteExtrator
from src.extract.motivo_viagem_extrator import MotivoViagemExtrator
from src.extract.orgao_scdp_extrator import OrgaoScdpExtrator
from src.extract.programa_extrator import ProgramaExtrator
from src.extract.tempo_diario_extrator import TempoDiarioExtrator
from src.extract.tipo_viagem_extrator import TipoViagemExtrator
from src.extract.tipo_viajante_extrator import TipoViajanteExtrator
from src.extract.diarias_scdp_extrator import DiariasScdpExtrator
from src.extract.diarias_scdp_liqpag_extrator import DiariasScdpLiqpagExtrator

from src.tranform.pais_transformador import PaisTransformador
from src.tranform.estado_transformador import EstadoTransformador
from src.tranform.cidade_transformador import CidadeTransformador
from src.tranform.acao_transformador import AcaoTransformador


if __name__ == '__main__':
    print("Iniciando a extração dos dados...")

    # Executar Extrator Países
    paisExtrator = PaisExtrator()
    paisdf = paisExtrator.extrair_pais()
    paisExtrator.salvar_pais(paisdf)

    # Executar Extrator Estados
    estadoExtrator = EstadoExtrator()
    estadodf = estadoExtrator.extrair_estado()
    estadoExtrator.salvar_estado(estadodf)

    # Executar Extrator Cidades
    cidadeExtrator = CidadeExtrator()
    cidadedf = cidadeExtrator.extrair_cidade()
    cidadeExtrator.salvar_cidade(cidadedf)

    # Executar Extrator Ações
    acaoExtrator = AcaoExtrator()
    acaodf = acaoExtrator.extrair_acao()
    acaoExtrator.salvar_acao(acaodf)

    # Executar Extrator Cargo SCDP
    cargoExtrator = CargoScdpExtrator()
    cargodf = cargoExtrator.extrair_cargo_scdp()
    cargoExtrator.salvar_cargo_scdp(cargodf)

    # Executar Extrator Documento Viagem
    docViagemExtrator = DocumentoViagemExtrator()
    docviagemdf = docViagemExtrator.extrair_documento_viagem()
    docViagemExtrator.salvar_documento_viagem(docviagemdf)

    # Executar Extrator Empenho Despesa Diárias SCDP LiqPag
    empenhoExtrator = EmpenhoDespDiariasScdpLiqpagExtrator()
    empenhodf = empenhoExtrator.extrair_empenho_desp_diarias_scdp_liqpag()
    empenhoExtrator.salvar_empenho_desp_diarias_scdp_liqpag(empenhodf)

    # Executar Extrator Favorecido SCDP
    favorecidoExtrator = FavorecidoScdpExtrator()
    favorecidodf = favorecidoExtrator.extrair_favorecido_scdp()
    favorecidoExtrator.salvar_favorecido_scdp(favorecidodf)

    # Executar Extrator Fonte
    fonteExtrator = FonteExtrator()
    fontedf = fonteExtrator.extrair_fonte()
    fonteExtrator.salvar_fonte(fontedf)

    # Executar Extrator Função Despesa
    funcaoDespExtrator = FuncaoDespExtrator()
    funcaodespdf = funcaoDespExtrator.extrair_funcao_desp()
    funcaoDespExtrator.salvar_funcao_desp(funcaodespdf)

    # Executar Extrator Função SCDP
    funcaoScdpExtrator = FuncaoScdpExtrator()
    funcaoscdpdf = funcaoScdpExtrator.extrair_funcao_scdp()
    funcaoScdpExtrator.salvar_funcao_scdp(funcaoscdpdf)

    # Executar Extrator Item Despesa
    itemDespExtrator = ItemDespExtrator()
    itemdespdf = itemDespExtrator.extrair_item_desp()
    itemDespExtrator.salvar_item_desp(itemdespdf)

    # Executar Extrator Meio Transporte
    meioTranspExtrator = MeioTransporteExtrator()
    meiotranspdf = meioTranspExtrator.extrair_meio_transporte()
    meioTranspExtrator.salvar_meio_transporte(meiotranspdf)

    # Executar Extrator Motivo Viagem
    motivoViagemExtrator = MotivoViagemExtrator()
    motivoviagemdf = motivoViagemExtrator.extrair_motivo_viagem()
    motivoViagemExtrator.salvar_motivo_viagem(motivoviagemdf)

    # Executar Extrator Órgão SCDP
    orgaoScdpExtrator = OrgaoScdpExtrator()
    orgaoscdpdf = orgaoScdpExtrator.extrair_orgao_scdp()
    orgaoScdpExtrator.salvar_orgao_scdp(orgaoscdpdf)

    # Executar Extrator Programa
    programaExtrator = ProgramaExtrator()
    programadf = programaExtrator.extrair_programa()
    programaExtrator.salvar_programa(programadf)

    # Executar Extrator Tempo Diário
    tempoDiarioExtrator = TempoDiarioExtrator()
    tempodiariodf = tempoDiarioExtrator.extrair_tempo_diario()
    tempoDiarioExtrator.salvar_tempo_diario(tempodiariodf)

    # Executar Extrator Tipo Viagem
    tipoViagemExtrator = TipoViagemExtrator()
    tipoviagemdf = tipoViagemExtrator.extrair_tipo_viagem()
    tipoViagemExtrator.salvar_tipo_viagem(tipoviagemdf)

    # Executar Extrator Tipo Viajante
    tipoViajanteExtrator = TipoViajanteExtrator()
    tipoviajantedf = tipoViajanteExtrator.extrair_tipo_viajante()
    tipoViajanteExtrator.salvar_tipo_viajante(tipoviajantedf)

    # Executar Extrator Fato Diárias SCDP
    diariasScdpExtrator = DiariasScdpExtrator()
    diariasscdpdf = diariasScdpExtrator.extrair_diarias_scdp()
    diariasScdpExtrator.salvar_diarias_scdp(diariasscdpdf)

    # Executar Extrator Fato Diárias SCDP LiqPag
    diariasLiqpagExtrator = DiariasScdpLiqpagExtrator()
    diariasliqpagdf = diariasLiqpagExtrator.extrair_diarias_scdp_liqpag()
    diariasLiqpagExtrator.salvar_diarias_scdp_liqpag(diariasliqpagdf)

    print("Iniciando a transformação dos dados...")

    # Transformação Países
    paisTransformador = PaisTransformador()    
    paisdf = paisTransformador.extrair_pais()
    paisdf = paisTransformador.tranformar_pais(df_dataframe=paisdf)
    paisTransformador.salvar_pais(paisdf)

    # Transformação Estados
    estadoTransformador = EstadoTransformador()
    estadodf = estadoTransformador.extrair_estado()
    estadodf = estadoTransformador.transformar_estado(df_dataframe=estadodf)
    estadoTransformador.salvar_estado(estadodf)

    # Transformação Cidades
    cidadeTransformador = CidadeTransformador()
    cidadedf = cidadeTransformador.extrair_cidade()
    cidadedf = cidadeTransformador.transformar_cidade(df_dataframe=cidadedf)
    cidadeTransformador.salvar_cidade(cidadedf)

    # Transformação Ações
    acaoTransformador = AcaoTransformador()
    acaodf = acaoTransformador.extrair_acao()
    acaodf = acaoTransformador.transformar_acao(df_dataframe=acaodf)
    acaoTransformador.salvar_acao(acaodf)

    print('FIM DA EXECUÇÃO DO PIPELINE ETL')