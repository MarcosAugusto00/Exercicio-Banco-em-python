import datetime
import os

formatador = ("%d/%m/%Y %H:%M:%S")

def cadastrousuario(numero_usuario, cpfs):
    nome = input("Digite o seu nome completo: \n")
    data_nascimento = input("Digite a sua data de nascimento: [xx/yy/zz] \n")
    while True:
        cpf = int(input("Digite o numero de seu CPF: (Somente numeros)\n"))
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
    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}"
    dicionario_usu = {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "CPF": cpf,
        "Endereço": endereco
    }
    usuario.insert(numero_usuario, dicionario_usu)  # Adiciona o dicionário no index numero_usuario
    numero_usuario += 1
    cpfs.append(cpf)
    os.system('cls')
    return numero_usuario, cpfs, usuario, dicionario_usu

def achar_index(usuario, cpf):
    indices = [i for i, dicionario in enumerate(usuario) if dicionario['CPF'] == cpf]
    return indices[0] if indices else None

def indiceg(conta):
    return conta - 10000

def nova_conta(agencia, numero_conta, contas, cpfs, data_atual, usuario, dicionario_usu):

    "Esta função serve para criar uma nova conta para um usuario, o mesmo usuario, pode ter varias contas"

    os.system('cls')
    print(f"""
              --------------------------------------------
                   Cadastros de nova conta corrente
              --------------------------------------------
          """)
    cpf = int(input("Digite o seu CPF: (Somente numeros) \n"))
    if cpf in cpfs:
        indice_usu = achar_index(usuario, cpf)
        if indice_usu is not None:
            nome = usuario[indice_usu]['Nome'].split()[0]
            nome_completo = usuario[indice_usu]['Nome']
            contador = 0
            if contas:  # Checa se 'contas' não está vazio
                for conta_info in contas.values():  # Itera sobre cada lista de contas
                    for conta in conta_info:  # Itera sobre cada dicionário (cada conta)
                        if conta['CPF'] == cpf:  # Verifica se o CPF é o mesmo
                            contador += 1 

            print(f"""
                                        Olá {nome}!!!
                         Você possui {contador} contas cadastradas em seu CPF
                               Deseja cadastrar outra nova? [S/N] 
                  """)
            resp_conta = input(" ")
            os.system('cls')
            if resp_conta.upper() == "S":
                numero_conta += 1
                if numero_conta not in contas:
                    contas[numero_conta] = []  # Inicializa a lista se não existir
                contas[numero_conta].append(dicionario_usu)  # Adiciona a nova conta à lista
                
                print(f"""
                            -----------------------------------------------
                      
                                 Parabéns, você acaba de criar sua nova
                                            conta corrente
                      
                      
                               Agência:         {agencia}
                               Conta corrente: {numero_conta} 
                               Nome:  {nome_completo}


                                      {(data_atual.strftime(formatador))}

                            -----------------------------------------------
                          """)
                indice = indiceg(numero_conta)
                extratos.insert(indice, {})
                num_ope.insert(indice, 0)
                dataprimeiraope.insert(indice, data_atual)
                saldo.insert(indice, 0)
                n.insert(indice, 0)   
                return contas, numero_conta
            else:
                return None, None
        else:
            print("CPF não cadastrado")
            if not contas:
                contas = {}
                os.system('cls')
            return contas, numero_conta
    else:
        print("CPF não cadastrado")
        os.system('cls')
    if not contas:
        contas = {}
    return contas, numero_conta

def sacar(valor, extratos, saldo, n, data, num_ope, dataprimeiraope):
    if saldo >= valor:
        n += 1
        if n <= 3:
            num_ope += 1
            if num_ope == 1:
                dataprimeiraope = datetime.date.today()
            saldo -= valor
            print(f"Operação diária {num_ope}")
            print(f"O seu {n}º saque diário de {valor:.2f} foi feito")
            extratos.update({f"Operação {num_ope}  Saque    ": f"- R${valor:.2f} em {data.strftime(formatador)}"})
        else:
            print("Você ultrapassou o limite de saques diários")
    else:
        print("Saldo insuficiente")
    return extratos, saldo, n, num_ope, dataprimeiraope

def depositar(valor, extratos, saldo, data, num_ope, dataprimeiraope):
    num_ope += 1
    if num_ope == 1:
        dataprimeiraope = datetime.date.today()
    saldo += valor
    print(f"Operação diária {num_ope}")
    print(f"Depósito no valor de {valor:.2f} realizado")
    extratos.update({f"Operação {num_ope}  Deposito ": f"  R${valor} em {data.strftime(formatador)}"})
    return extratos, saldo, num_ope, dataprimeiraope

def extrato(extratos, saldo, data):
    largura = 35
    print("-------------------------Extrato-------------------------")
    print("")
    print(f"                   {(data.strftime(formatador))}")
    print("")
    for chave, valor in extratos.items():
        print(f'{chave:<{largura - 15}}: {valor:10}')
    tela = "Saldo total"
    saldos = f"   R${saldo:.2f}"
    print("")
    print("")
    print(f'{tela:<{largura - 14}}:{saldos:10}')
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

# Variáveis globais
extratos = []
dicionario_usu = {}
usuario = []
cpfs = []
n = []
contas = {}
num_ope = []  
saldo = []
numero_usuario = 1
agencia = "0001"
dataprimeiraope = []
numero_conta = 9999

while True:
    data_atual = datetime.datetime.now()
    telainicial(data_atual)
    operacao = int(input("Operação: \n"))
    if operacao == 1:
        data_atual = datetime.datetime.now()
        numero_usuario, cpfs, usuario, dicionario_usu = cadastrousuario(numero_usuario, cpfs)
    elif operacao == 2:
        data_atual = datetime.datetime.now()
        contas, numero_conta = nova_conta(agencia, numero_conta, contas, cpfs, data_atual, usuario, dicionario_usu)
    elif operacao == 3:
        conta_usu = int(input("Digite o numero de sua conta: \n"))
        if conta_usu in contas: 
            indice = indiceg(conta_usu)
            dataatual = datetime.date.today()
            if num_ope[indice] >= 1:
                if dataprimeiraope[indice] != dataatual:
                    num_ope[indice] = 0
                    n[indice] = 0   
            while True:
                data_atual = datetime.datetime.now()
                telainicio(data_atual)
                operacao = int(input("Operação: \n"))
                os.system('cls')
                if num_ope[indice] < 10:  # Verifica se o número de operações é menor que 10
                    if operacao == 1:
                        data_atual = datetime.datetime.now()
                        valor = float(input("Digite o valor que deseja sacar: \nR$"))
                        extratos[indice], saldo[indice], n[indice], num_ope[indice], dataprimeiraope[indice] = sacar(valor, extratos[indice], saldo[indice], n[indice], data_atual, num_ope[indice], dataprimeiraope[indice])
                    elif operacao == 2:
                        data_atual = datetime.datetime.now()
                        valor = float(input("Digite o valor que deseja depositar: \nR$"))
                        extratos[indice], saldo[indice], num_ope[indice], dataprimeiraope[indice] = depositar(valor, extratos[indice], saldo[indice], data_atual, num_ope[indice], dataprimeiraope[indice])
                    elif operacao == 3:
                        data_atual = datetime.datetime.now()
                        extrato(extratos[indice], saldo[indice], data_atual)
                    elif operacao == 4:
                        break
                    else:
                        print("Operação inválida")
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
            os.system('cls')
    elif operacao == 4:
        telafinal()
        break
    else:
        print("Operação invalida")