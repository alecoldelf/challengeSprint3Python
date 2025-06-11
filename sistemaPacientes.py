import os
from datetime import datetime
import pandas as pd

os.system("cls")

pacientes = []
ult_id = 0

# Função genérica para validar entradas
def entrada(msg):
    while True:
        valor = input(msg)
        if valor.strip() == "0":
            print("Valor '0' não é permitido. Digite novamente.")
        else:
            return valor

def add_pac():
    """Adiciona um novo paciente à lista"""
    global ult_id
    try:
        p = {}
        p["Nome"] = entrada("Nome: ")
        p["Idade"] = entrada("Idade: ")
        p["Nascimento"] = entrada("Data de nascimento (DD/MM/AAAA): ")
        p["Sexo"] = entrada("Sexo: ")
        p["CPF"] = entrada("CPF: ")
        ult_id += 1
        p["ID"] = ult_id
        pacientes.append(p)
        print(f"Paciente adicionado com ID {ult_id}.\n")
    except Exception as e:
        print(f"Erro ao adicionar paciente: {e}\n")

def alt_pac():
    """Altera os dados de um paciente existente"""
    try:
        pid = int(entrada("ID do paciente a alterar: "))
        for p in pacientes:
            if p["ID"] == pid:
                print(f"Paciente encontrado: {p}")
                campo = entrada("Campo a alterar (Nome, Idade, Nascimento, Sexo, CPF): ")
                if campo in p:
                    novo = entrada(f"Novo valor para {campo}: ")
                    p[campo] = novo
                    print("Paciente alterado com sucesso.\n")
                else:
                    print("Campo inválido.\n")
                return
        print("Paciente não encontrado.\n")
    except ValueError:
        print("ID inválido. Digite um número inteiro.\n")
    except Exception as e:
        print(f"Erro ao alterar paciente: {e}\n")

def exc_pac():
    """Exclui um paciente da lista"""
    try:
        pid = int(entrada("ID do paciente a excluir: "))
        for p in pacientes:
            if p["ID"] == pid:
                pacientes.remove(p)
                print("Paciente excluído com sucesso.\n")
                return
        print("Paciente não encontrado.\n")
    except ValueError:
        print("ID inválido. Digite um número inteiro.\n")
    except Exception as e:
        print(f"Erro ao excluir paciente: {e}\n")

def ver_pac():
    """Exibe todos os pacientes cadastrados"""
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return
    print("\n=== Lista de Pacientes ===")
    for p in pacientes:
        print(f"ID: {p['ID']}")
        print(f"Nome: {p['Nome']}")
        print(f"Idade: {p['Idade']}")
        print(f"Nascimento: {p['Nascimento']}")
        print(f"Sexo: {p['Sexo']}")
        print(f"CPF: {p['CPF']}\n")

def salvar_excel(pacientes) -> None:
    """Exporta os dados para uma planilha Excel"""
    try:
        nome = entrada("Pressione [Enter] para nome automático ou digite o nome do arquivo: ")
        if nome.strip() == "":
            agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nome = f"pacientes_{agora}.xlsx"
        elif not nome.lower().endswith(".xlsx"):
            nome += ".xlsx"

        df = pd.DataFrame(pacientes)
        df.to_excel(f"./{nome}", index=False)
        print(f"Planilha '{nome}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar planilha: {e}\n")

def ler_excel() -> None:
    """Importa dados de uma planilha Excel"""
    try:
        nome = entrada("Nome do arquivo (sem .xlsx): ")
        caminho = f'./{nome}.xlsx'
        df = pd.read_excel(caminho)
        print("Dados lidos do Excel:")
        print(df)
    except FileNotFoundError:
        print("Arquivo não encontrado.\n")
    except Exception as e:
        print(f"Erro ao ler planilha: {e}\n")

def priorizar():
    """Move um paciente para uma posição prioritária na lista"""
    try:
        pid = int(entrada("ID do paciente a priorizar: "))
        for p in pacientes:
            if p["ID"] == pid:
                pacientes.remove(p)
                pos = int(entrada(f"Nova posição (0 até {len(pacientes)}): "))
                if pos < 0:
                    pos = 0
                elif pos > len(pacientes):
                    pos = len(pacientes)
                pacientes.insert(pos, p)
                print(f"Paciente com ID {pid} movido para posição {pos} com sucesso!\n")
                return
        print("Paciente não encontrado.\n")
    except ValueError:
        print("Entrada inválida. Use apenas números inteiros.\n")
    except Exception as e:
        print(f"Erro ao priorizar paciente: {e}\n")

def menu():
    """Menu principal do sistema"""
    while True:
        print("=== MENU ===")
        print("1 - Adicionar paciente")
        print("2 - Alterar dado de paciente")
        print("3 - Excluir paciente")
        print("4 - Mostrar pacientes")
        print("5 - Transferir para planilha")
        print("6 - Importar planilha")
        print("7 - Priorizar paciente")
        print("0 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            add_pac()
        elif opc == "2":
            alt_pac()
        elif opc == "3":
            exc_pac()
        elif opc == "4":
            ver_pac()
        elif opc == "5":
            salvar_excel(pacientes)
        elif opc == "6":
            ler_excel()
        elif opc == "7":
            priorizar()
        elif opc == "0":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
