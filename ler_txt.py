class ArquivoTexto(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self._extrair_conteudo()

        
  def _extrair_conteudo(self):
      conteudo = list()
      with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:  
       conteudo = arquivo.read().splitlines() 
       return conteudo

  def extrair_linha(self,numero_linha):  ##Função para extrair linha
      return self.conteudo[numero_linha-1] 


class ArquivoCSV(ArquivoTexto):  ##Criando a Classe que Herdará de ArquivoTXT

  def __init__(self, arquivo: str):  ##Funçao que iniciará a classe Pai
      super().__init__(arquivo=arquivo)  ##Iniciando a Classe Pai, onde arquivo recebe o arquivo da classe Pai

      self.colunas = self.extrair_colunas()  ##Atributo da Sub-Classe
   
  def extrair_colunas(self):  ##Função para extrair coluna da variável "conteudo" 
      return self.conteudo[0]

  def extrair_coluna_da_linha(self, numero_linha: int, numero_coluna: int):  ##Função para Extrair coluna da linha
    num_linha = self.conteudo[numero_linha]  ##1° Buscamos a linha de "conteudo"
    num_linha = num_linha.split(sep=',')[numero_coluna -1]  ##2° Fizemos Split separado por "," e atribuímos a chave -1.
    return num_linha  ##retornamos a "num_linha"



arquivo_csv = ArquivoCSV(arquivo='carros.csv')

numero_linha = 2
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

print('#'*30)
numero_linha = 3 
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))
