# Script para extrair as informações de uma fonte de dados
# Constantes definidas para a aplicação
DATA_INICIAL = "07-01-2023"
DATA_FINAL = "08-31-2023"
SOURCE_URL = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{DATA_INICIAL}'&@dataFinalCotacao='{DATA_FINAL}'&$format=text/csv&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
# Importações utilizadas
import requests
from datetime import datetime

def buscar_dados():
    """
    Busca os dados de uma fonte de dados
    """
    # Faz a requisição dos dados
    resposta = requests.get(SOURCE_URL)

    # Verifica se a requisição foi bem sucedida
    if resposta.status_code != 200:
        raise Exception("Erro ao buscar dados da fonte de dados")

    # Retorna os dados
    return resposta.text

def salvar_dados(dados, file_path):
    """
    Salva os dados em um arquivo
    """
    # Abre o arquivo para escrita
    with open(file_path, "w") as arquivo:
        # Escreve os dados no arquivo
        arquivo.write(dados)


# Função principal da extração.
def main():
    print(f"[EXTRAÇÃO] Iniciando extração de dados")
    print(f"[EXTRAÇÃO] Buscando os dados de {DATA_INICIAL} até {DATA_FINAL}")
    print(f"[EXTRAÇÃO] Fonte de dados: {SOURCE_URL}")
    dados = buscar_dados()
    print(f"[EXTRAÇÃO] Dados aquisitados com sucesso")
    file_path = "dados.csv"
    print(f"[EXTRAÇÃO] Salvando dados no arquivo {file_path}")
    salvar_dados(dados, file_path)




if __name__ == "__main__":
    # Executa a função de busca de dados
    main()