import csv
import requests

def import_moedas(path,deli=';'):
    '''
    path: caminho + nome do arquivo csv que contém a relação de moedas
    deli: delimitador do arquivo csv
    '''
    moedas={} #dicionário que terá como chave o código de 3 dígitos da moeda e o valor é o código da moeda para o banco central
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=deli)
        next(csv_reader,None)
        for row in csv_reader:
            moedas[row[2].strip()]=row[0]
        
    return moedas

def conversor_moedas(data,origem,destino,valor,url='https://www3.bcb.gov.br/bc_moeda/rest/converter/'):
    '''
    data: data da cotação (formato YYYY-MM-DD)
    origem: código da moeda de origem
    destino: código da moeda de destino
    valor: valor a ser convertido
    url: API rest que realiza a conversão
    '''
    #monta a url
    url_ = url+str(valor)+'/1/'+str(origem)+'/'+str(destino)+'/'+str(data)

    #pega o retorno
    response = requests.get(url_)

    #testa se o código obteve resposta de sucesso
    if response.status_code == 200:
        #pega o valor dentro da tag de valor convertido
        for item in str(response.content).split('</valor-convertido>'):
            if '<valor-convertido>' in item:
                return (item [ item.find("<valor-convertido>")+len("<valor-convertido>") : ])
    else:
        print('Ocorreu um erro ao acessar a API do Banco Central')
        raise Exception (response.status_code)

if __name__ == "__main__":
    #usa o arquivo presente no banco central para criar o dicionário (https://www.bcb.gov.br/acessoinformacao/legado?url=https:%2F%2Fwww4.bcb.gov.br%2Fpec%2Ftaxas%2Fbatch%2Ftabmoedas.asp%3Fid%3Dtabmoeda)
    dict_moedas = import_moedas('./M20191029.csv')

    try:
        #converter 10 BRL para EUR
        print('Valor de R$10 para EUR é: '+ conversor_moedas('2019-10-29',dict_moedas['BRL'],dict_moedas['EUR'],10))
        #converter 10 EUR para USD
        print('Valor de €10 para USD é: '+ conversor_moedas('2019-10-29',dict_moedas['EUR'],dict_moedas['USD'],10))
    except Exception as e:
        print(str(e))

