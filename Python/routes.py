from flask import Flask , request
from imprimi import methodImpressao;


app = Flask("Impressao")

@app.route("/conexao", methods=["GET"])
def olaMundo():
    return geraResponse(200, "API Online.")

@app.route("/impressao", methods=["POST"])
def imprimeArquivos():
    body = request.get_json()
    if("descricaoImpressora" not in body):
        return geraResponse(400, "Erro, contatar o TI sem parâmetro de impressãoo.")

    if("idDocumento" not in body):
        return geraResponse(400, "Erro, contatar o TI sem parâmetro de nota Fiscal.")
    
    if("tipoArquivo" not in body):
        return geraResponse(400, "Erro, contatar o TI.")
        
   
    impressao = methodImpressao(body["descricaoImpressora"], body["idDocumento"],body["tipoArquivo"])
    
    if (impressao == 1):
        return geraResponse(200, "Impressão gerada.")
    elif impressao == 2:
        return geraResponse(400, "Impressora não encontrada.")
    elif impressao == 3:
        return geraResponse(400, "Arquivo não encontrado.")
    else:
        return geraResponse(400, "Caminho não encontrado.")

def geraResponse(status,mensagem):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem
    return response
    
app.run()