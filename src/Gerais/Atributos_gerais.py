import os
import datetime

formatador = ("%d/%m/%Y %H:%M:%S")

cpfs = []
conta = {}
data_atual = datetime.datetime.now()
numero_conta = 10000

def numero_contas():
    global numero_conta
    numero_conta += 1
    return numero_conta

def cancelar_numero_contas():
    global numero_conta
    numero_conta -= 1

def telafinal():
    print(f"""
          Obrigado por utilizar o nosso Banco
                   Volte Sempre!!!
          """)

def teste_operacao():
    operacao = input("Digite o numero da operação desejada: \n")
    if operacao.isdigit():
        operacao = int(operacao)
        return operacao 
    else:
        operacao = 9
        return operacao
    
def testar_resp(resp):
    if len(resp) > 0:
        resp = resp.strip().capitalize()
        return resp[0]
    else:
        return "f"
    
def telainicial(data):
    print(f"""
    --------------Bem vindo ao seu Banco--------------
          
                    {(data_atual.strftime(formatador))}

           Por favor digite a operação desejada:

      1 - Cadastrar novo usuario
      2 - Cadastrar nova conta
      3 - Operações
      4 - Sair

    --------------------------------------------------
      """)

def teste_cpf():
    while True:
        cpf = input("Digite o seu CPF: (Somente numeros) \n")
        cpf = cpf.replace(".", "").replace("-", "")
        if len(cpf) == 11:
            if cpf.isdigit():
                cpf = int(cpf)
                return cpf
            else:
                os.system('cls')
                print("CPF invalido, o CPF deve possuir apenas numeros")
        else:
            os.system('cls')
            print("CPF invalido, o CPF deve possuir 11 numeros")

usuarios = []  
contas = []
contador_usuarios = 0
contador_contas = 0
nova_conta = None