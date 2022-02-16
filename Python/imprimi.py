import win32print
import win32api
import os

def methodImpressao(descricaoImpressora, idDocumento,tipoArquivo):
    if tipoArquivo == "CTE":
        caminho = r"C:\Users\leonardo.fernandes\Desktop\teste\CTE"
        arquivo = f'Cte_{idDocumento}.pdf'
    elif tipoArquivo == "NFE":
        caminho = r"C:\Users\leonardo.fernandes\Desktop\teste\NFE"
        arquivo = f'Nfe_{idDocumento}.pdf'
    else:
        return 0

    try:
        win32print.SetDefaultPrinter(descricaoImpressora) 
    except:
        print("Impressora não encontrada ")
        return 2
    
    try:
        win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
        return 1
    except:
        print("Arquivo não encontrado !")
        return 3