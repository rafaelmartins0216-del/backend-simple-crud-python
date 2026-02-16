#operações que podemos fazer com nosso JSON
import json
from database import salvar_json, existe_arquivo ,retornar_arquivo , maior_id



#função para criar usuários e colocar no banco (Json)
def criar_usuario(nome:str):
    """Função para criar um usuário"""

    arquivo=retornar_arquivo()
    
    for arq in arquivo:
        if arq["Nome"]==nome.title():
            return "nome ja presente em nosso banco"
    dic={
        "id":maior_id()+1,
        "Nome":nome.title(),
        "Status":False
    }
    
    arquivo.append(dic)

    salvar_json(arquivo)

    return "Usuário salvo com sucesso"



#listar todos os dados
def listar_dados():
    """função para exibir todos os dados"""
    if existe_arquivo():
            arquivo=retornar_arquivo()
            print(arquivo)

#buscar por nome
def filtrar_nome(nome:str):
    """Função para buscar por nome"""
    if existe_arquivo():
            arquivo=retornar_arquivo()
        
            nome=nome.title()

            for n in arquivo:
                if n["Nome"]==nome:
                    print(n)
                    return nome
                
            return None

#função para deletar um item
def deletar_item(id_item):
    arquivo = retornar_arquivo()

    for item in arquivo:
        if item["id"] == id_item:
            arquivo.remove(item)
            salvar_json(arquivo)
            return "Item removido com sucesso"

    return "ID não encontrado"


#função para atualizar nome
def atualiar_item_nome(id_item, nome_atualizado:str):
    if existe_arquivo():
        arquivo=retornar_arquivo()

        nome_atualizado=nome_atualizado.title()
        

        for ids in arquivo:
            if ids["id"]==id_item:

                ids["Nome"]=nome_atualizado

                salvar_json(arquivo)

                return "Nome atualizado com sucesso"

        return "ID não presente em nosso banco"


#função para mostrar status da pessoa
def verificar_pessoa_nome_existe(nome:str):
    if existe_arquivo():
        arquivo=retornar_arquivo()
        nome_filtro= filtrar_nome(nome)
        if nome_filtro:
            for arq in arquivo:
                if arq["Nome"]==nome_filtro:
                    return True
        return False

#função para mudar Status : Ativar
def ativar_status(nome:str):
    if existe_arquivo():
        nome=nome.title()
        arquivo=retornar_arquivo()
        if verificar_pessoa_nome_existe(nome):
            for arq in arquivo:
                if arq["Nome"]==nome:
                    arq["Status"]=True
        salvar_json(arquivo)


#função para desativar o Status:Desativar
def desativar_status(nome:str):
    if existe_arquivo():
        nome=nome.title()
        arquivo=retornar_arquivo()
        if verificar_pessoa_nome_existe(nome):
            for arq in arquivo:
                if arq["Nome"]==nome:
                    arq["Status"]=False
        salvar_json(arquivo)




