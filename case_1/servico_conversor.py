from flask import Flask, escape, request
import conversor_moedas as cm

app = Flask(__name__)

@app.route('/conversor')
def hello():
    data = request.args.get("data")
    origem=request.args.get("origem")
    destino=request.args.get("destino")
    valor=request.args.get("valor")
    
    #usa o arquivo presente no banco central para criar o dicionário (https://www.bcb.gov.br/acessoinformacao/legado?url=https:%2F%2Fwww4.bcb.gov.br%2Fpec%2Ftaxas%2Fbatch%2Ftabmoedas.asp%3Fid%3Dtabmoeda)
    dict_moedas = cm.import_moedas('./M20191029.csv')
    
    return cm.conversor_moedas(data,dict_moedas[str(origem)],dict_moedas[str(destino)],valor)

if __name__ == '__main__':
    app.run()