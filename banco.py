import datetime
import os
formatador = ("%d/%m/%Y %H:%M:%S")

def cadastrousuario(numero_usuario, cpfs):
    nome = input("Digite o seu nome completo: \n")
    data_nascimento = input("Digite a sua data de nascimento: [xx/yy/zz] \n")
    while True:
        cpf = int(input("Digite o numero de seu cpf: (Somente numeros)\n"))
        if cpf in cpfs:
            print("  Numero CPF já cadastrado ")
            while True:
                print("""
                      
                      ------------------------------
                        Digite a operação desejada:
                  
                       1 - Utilizar outro CPF
                       2 - Sair

                      ------------------------------

                    """)
                respf = int(input(" "))
                if respf == 1:
                    break
                elif respf == 2:
                    return None, None, None
                else:
                    print("       Opção invalida      ")
        else:  
            break
    logradouro = input("Digite o nome da sua rua: \n")
    numero_casa = input("Digite o numero da sua casa: \n")
    bairro = input("Digite o nome do seu bairro: \n")
    cidade = input("Digite o nome da sua cidade: \n")
    estado = input("Digite a sigla do seu estado: \n")
    endereço = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}"
    dicionario_usu = {"Nome" : nome, "Data de Nascimento:" : data_nascimento, 
                                "CPF:" : cpf, "Endereço: " : endereço 
                                }
    usuario.insert(numero_usuario, dicionario_usu)
    numero_usuario += 1
    cpfs.append(cpf)
    os.system('cls')
    return numero_usuario, cpfs, usuario

def achar_index(usuario, cpf):
    indices = [i for i, dicionario in enumerate(usuario) if dicionario['CPF:'] == cpf]
    return indices[0] if indices else None


def nova_conta(agencia, numero_conta, contas, cpfs, data_atual, usuario):
    os.system('cls')
    print(f"""
              --------------------------------------------
          
                   Cadastros de nova conta corrente
          
              --------------------------------------------
          
          """)
    cpf = int(input("Digite o seu CPF: (Somente numeros) \n"))
    contador = 0
    if cpf in cpfs:
        indice = achar_index(usuario, cpf)
        if indice is not None:
            nome = usuario[indice]['Nome'].split()[0]
        for conta in contas.values():
            if conta['CPF:'] == cpf:
                contador += 1
        while True:
            print(f"""
              
                                        Olá {nome}!!!

                         Você possui {contador} contas cadastradas em seu CPF

                               Deseja cadastrar outra nova? [S/N] 

                  """)
            resp_conta = input(" ")
            os.system('cls')
            if resp_conta.upper() == "S":
                numero_conta += 1
                contas.update({numero_conta : usuario})
                print(f"""
                            -----------------------------------------------
                      
                                 Parabens você acaba de criar sua nova
                                            conta corrente
                          
                               Agência:         {agencia}
                               Conta corrente: {numero_conta} 
                               Nome:  {nome}

                                      {(data_atual.strftime(formatador))}

                            -----------------------------------------------
                          """)
                break
            elif resp_conta.upper() == "N":
                os.system('cls')
                return None, None
            else:
                print("                Opção invalida   ")
                continue
        return contas, numero_conta
    else:
        print("CPF não cadastrado")
    return None, None

def sacar(valor, extratos, saldo, n, data, num_ope):
    if saldo>=valor:
        n += 1
        if n <= 3:
            num_ope += 1
            saldo -= valor
            print(f"Operação diaria {num_ope}")
            print(f"O seu {n}º saque diario de {valor:.2f} foi feito")
            extratos.update({f"Operação {num_ope}  Saque    " : f"- R${valor:.2f} em {data.strftime(formatador)}"})
        else:
            print("Você ultrapassou o limite de saques diarios")
    else:
        print("Saldo insuficiente")
    return extratos, saldo, n, num_ope

def depositar(valor, extratos, saldo, data, num_ope):
    num_ope += 1
    saldo += valor
    print(f"Operação diaria {num_ope}")
    print(f"Deposito no valor de {valor:.2f} realizado")
    extratos.update({f"Operação {num_ope}  Deposito " : f"  R${valor} em {data.strftime(formatador)}"})
    return extratos, saldo, num_ope

def extrato(extratos, saldo, data):
    largura = 35
    print("-------------------------Extrato-------------------------")
    print("")
    print(f"                   {(data.strftime(formatador))}")
    print("")
    for chave, valor in extratos.items():
        print(f'{chave:<{largura -15}}: {valor:10}')
    tela = "Saldo total"
    saldos = f"   R${saldo:.2f}"
    print("")
    print("")
    print(f'{tela:<{largura -14}}:{saldos:10}')
    print("")
    print("-------------------------------------------------------")

def telainicial(data):
    print(f"""
    --------------Bem vindo ao seu Banco--------------
          
                    {(data.strftime(formatador))}
      
           Por favor digite a operação desejada:

      1 - Cadastrar novo usuario
      2 - Cadastrar nova conta
      3 - Operações
      4 - Sair

    --------------------------------------------------
      """)

def telainicio(data):

    print(f"""
    --------------Bem vindo ao seu Banco--------------
          
                    {(data.strftime(formatador))}
      
           Por favor digite a operação desejada:

      1 - Saque
      2 - Deposito
      3 - Extrato
      4 - Sair

    --------------------------------------------------
      """)

def telafinal():
    print(f"""
          Obrigado por utilizar o nosso Banco
                   Volte Sempre!!!
          """)
    
extratos = {}
usuario = []
cpfs = []
contas = {}
n = 0
num_ope = 0  
saldo = 0
numero_usuario = 1
agencia = "0001"
dataprimeiraope = datetime.date.today()
numero_conta = 10000
data_atual = datetime.datetime.now()
while True:
    telainicial(data_atual)
    operacao = int(input("Operação: \n"))
    if operacao == 1:
        numero_usuario, cpfs, usuario = cadastrousuario(numero_usuario, cpfs)
    elif operacao == 2:
        contas, numero_conta = nova_conta(agencia, numero_conta, contas, cpfs, data_atual, usuario)
    elif operacao == 3:
        conta_usu = int(input("Digite o numero de sua conta: \n"))
        if contas.get(conta_usu):    
            while True:
                telainicio(data_atual)
                operacao = int(input("Operação: \n"))
                os.system('cls')
                if num_ope <= 10:
                    if operacao == 1:
                        valor = float(input("Digite o valor que deseja sacar: \nR$"))
                        extratos, saldo, n, num_ope = sacar(valor, extratos,saldo,n, data_atual, num_ope)
                    elif operacao == 2:
                        valor = float(input("Digite o valor que deseja depositar: \nR$"))
                        extratos, saldo, num_ope = depositar(valor, extratos,saldo, data_atual, num_ope)
                    elif operacao == 3:
                        extrato(extratos,saldo, data_atual)
                    elif operacao == 4:
                        break
                    else:
                        print("Operação Invalida")
                    print("")
                    resp = input("Deseja realizar outra operação: [S/N] \n")
                    os.system('cls')
                else:
                    if operacao == 3:
                        extrato(extratos,saldo, data_atual)
                    else:
                        print("""
                               ---------------------------------------
                                                         
                               Limite de operações diarias atingido: 
                                     Por favor volte outro dia       
                                                         
                               ---------------------------------------
                              """)
                    resp = "N"
                if num_ope == 1:
                    dataprimeiraope = datetime.date.today()
                dataatual = datetime.date.today()
                if dataprimeiraope != dataatual:
                    num_ope = 0
                if resp.upper() == "S":
                    continue
                elif resp.upper() == "N":
                    telafinal()
                    break
                else:
                    print("     Opção invalida")
                    telafinal()
                    break
        else:
            print("Conta inexistente")
            exit()
    elif operacao == 4:
        telafinal()
        break
    else:
        print("Operação invalida")
        telafinal()
        break