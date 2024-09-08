# Powered by brunoborges.eti.br
# 
import os
import subprocess
import sys


#2 funcao para criar o ambiente virtual
def criar_ambiente(diretorio_projeto):
    #Validar se o caminho é valido
    if not os.path.exists(diretorio_projeto):
        print("O diretorio informado não existes")
        return
    #Criar um caminho para o diretorio virtual
    venv_path = os.path.join(diretorio_projeto, 'venv')
    #Verificar se já existe o ambiente virtual com este nome
    if os.path.exists(venv_path):
        print("O Ambiente Virtual já existe")
        return
    # Criar o ambiente Virtual [VENV]
    try:
        subprocess.run(['virtualenv', venv_path], check=True)
        print("Ambiente criado com êxito")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar ambiente:{e}")
        

#3 funcao para 
def instalar_dependencias(diretorio_projeto, requirements_file):
    #Validar se existe o requirements no diretorio
    if not  os.path.exists(requirements_file):
        print("O Arquivo requirements.txt nao existe")
        return
    #Momento da ativacao do ambiente virtual
    venv_path = os.path.join(diretorio_projeto, 'venv', 'bin', 'activate')
    subprocess.run(['source', venv_path], shell=True)

    try:
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
        print("Dependencias instaladas com sucesso")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar as dependências: {e}")
        
    
    


#1 funcao para criar as dependencias do novo ambiente
def main():
    diretorio_projeto = sys.argv[1]
    requirements_file = os.path.join(diretorio_projeto, 'requirements_txt')
    criar_ambiente(diretorio_projeto)
    #Passa como parametro o diretorio do projeto e os requerimentos de instalacao [libs]
    instalar_dependencias(diretorio_projeto, requirements_file)

