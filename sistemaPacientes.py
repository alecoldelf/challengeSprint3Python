import os
from datetime import datetime
import pandas as pd 
os.system("cls")

lista_pacientes = []
ultimo_id = 0

def adicionar_paciente():
    global ultimo_id
    paciente = {}
    paciente["Nome"] = input("Digite o nome do paciente: ")
    paciente["Idade"] = input("Digite a idade do paciente: ")
    paciente["Data de Nascimento"] = input("Digite a data de nascimento do paciente (DD/MM/AAAA): ")
    paciente["Sexo"] = input("Digite o sexo do paciente: ")
    paciente["CPF"] = input("Digite o CPF do paciente: ")
    ultimo_id += 1
    paciente["ID"] = ultimo_id
    lista_pacientes.append(paciente)
    print(f"Paciente adicionado com ID {ultimo_id}.\n")

def alterar_paciente():
    id_paciente = int(input("Digite o ID do paciente que deseja alterar: "))
    for paciente in lista_pacientes:
        if paciente["ID"] == id_paciente:
            print(f"Paciente encontrado: {paciente}")
            campo = input("Qual campo deseja alterar (Nome, Idade, Data de Nascimento, Sexo, CPF)? ")
            if campo in paciente:
                novo_valor = input(f"Digite o novo valor para {campo}: ")
                paciente[campo] = novo_valor
                print("Paciente alterado com sucesso.\n")
            else:
                print("Campo inválido.\n")
            return
    print("Paciente não encontrado.\n")

def excluir_paciente():
    id_paciente = int(input("Digite o ID do paciente que deseja excluir: "))
    for paciente in lista_pacientes:
        if paciente["ID"] == id_paciente:
            lista_pacientes.remove(paciente)
            print("Paciente excluído com sucesso.\n")
            return
    print("Paciente não encontrado.\n")

def mostrar_pacientes():
    if not lista_pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    print("\n=== Lista de Pacientes ===")
    for paciente in lista_pacientes:
        print(f"ID: {paciente['ID']}")
        print(f"Nome: {paciente['Nome']}")
        print(f"Idade: {paciente['Idade']}")
        print(f"Data de Nascimento: {paciente['Data de Nascimento']}")
        print(f"Sexo: {paciente['Sexo']}")
        print(f"CPF: {paciente['CPF']}\n")

def transferirParaExcel(lista_pacientes) -> None:
    nome_arquivo = input("Pressione [Enter] para gerar um arquivo com a data-hora atual ou digite o nome do arquivo desejado: ")

    if nome_arquivo.strip() == "":
        agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"arquivo_{agora}.xlsx"
    else:
        if not nome_arquivo.lower().endswith(".xlsx"):
            nome_arquivo += ".xlsx"

    df = pd.DataFrame(lista_pacientes)
    df.to_excel(f"./{nome_arquivo}", index=False)

    print(f"Planilha '{nome_arquivo}' criada com sucesso!")

def transferirParaPython() -> None:
    arquivo = input("Digite o nome do arquivo que deseja ler: ")

    caminho_arquivo = f'./{arquivo}.xlsx'
    df = pd.read_excel(caminho_arquivo)
    print("Dados lidos do Excel:")
    print(df)

def priorizar_paciente():
    id_paciente = int(input("Digite o ID do paciente que deseja priorizar: "))
    for paciente in lista_pacientes:
        if paciente["ID"] == id_paciente:
            lista_pacientes.remove(paciente)
            posicao = int(input(f"Digite a nova posição para o paciente (0 até {len(lista_pacientes)}): "))
            if posicao < 0:
                posicao = 0
            elif posicao > len(lista_pacientes):
                posicao = len(lista_pacientes)
            lista_pacientes.insert(posicao, paciente)
            print(f"Paciente com ID {id_paciente} movido para a posição {posicao} com sucesso!\n")
            return
    print("Paciente não encontrado.\n")

def menu():
    while True:
        print("=== MENU ===")
        print("1 - Adicionar paciente")
        print("2 - Alterar dado de paciente")
        print("3 - Excluir paciente")
        print("4 - Mostrar pacientes")
        print("5 - Transferir para planilha")
        print("5 - Importar planilha")
        print("7 - Priorizar paciente")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_paciente()
        elif opcao == "2":
            alterar_paciente()
        elif opcao == "3":
            excluir_paciente()
        elif opcao == "4":
            mostrar_pacientes()
        elif opcao == "5":
            transferirParaExcel(lista_pacientes)
        elif opcao == "6":
            transferirParaPython()
        elif opcao == "7":
            priorizar_paciente()
        elif opcao == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
