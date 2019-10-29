Case 1:
Construa um serviço de conversão de moedas. Este serviço deve obter os dados de cotação do site do Banco Central do Brasil. Deve ser possível realizar uma chamada a um método da API do serviço com parâmetros de data da cotação (ex: 10/09/2019), moeda de origem (ex: EUR), moeda final (ex: USD) e valor desejado (ex: 150). O resultado desta chamada é o valor convertido para a moeda final.
<br>
Arquivo conversor_moedas.py<br>
	bibliotecas usadas:<br>
    csv - leitura do arquivo csv com informações das moedas<br>
    requests - recebe retorno da API<br>
    datetime - conversão da data<br>
  funções:<br>
    import_moedas - lê arquivo csv que contém de-para de código da moeda (texto) para código da API (alfanumerico)<br>
    conversor_moedas - recebe os parâmetros de data, moeda de origem, moeda de destino e valor e retorna valor convertido<br>
<br>
Arquivo servico_conversor.py<br>
  bibliotecas usadas:<br>
    Flask - criação de um serviço REST/API<br>
    conversor_moedas - funções relatadas acima<br>
  funções:<br>
    conversor - recebe os argumentos da requisição e retorna o valor convertido.<br>
<br>    
Para iniciar o programa, use o comando 'env FLASK_APP=servico_conversor.py flask run'
