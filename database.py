import json

#nome
#id
#status



#função para salvar a lista
def salvar_json(lista_dados):
    """função parasalvar o JSON"""
    with open(r"../data/dados.json","w", encoding="utf-8") as file:
        json.dump(lista_dados, file , indent=4)



#função para criar o arquivo
def criar_arquivo_vazio():
    """função para criar um arquivo vazio (com uma lista)"""
    with open(r"../data/dados.json","w", encoding="utf-8") as file:
        json.dump([],file)



#função para pegar o arquivo
"""função para pegar arquivo"""
def retornar_arquivo():
    if existe_arquivo():
        with open(r"../data/dados.json","r", encoding="utf-8") as file:
            return json.load(file)
    else:
        criar_arquivo_vazio()
        with open(r"../data/dados.json","r", encoding="utf-8") as file:
            return json.load(file)


#função para ver o arquivo existe
def existe_arquivo():
    """verifica se o arquivo existe e retornar true ou false"""
    try:
        with open(r"../data/dados.json","r", encoding="utf-8") as file:
            return True
    except:
        return False
    


#função para pegar maior id existente
def maior_id():
    """Pega o maior id"""
    if existe_arquivo():
        arquivo=retornar_arquivo()
        if arquivo:
            return max(item["id"] for item in arquivo)
    return 0







