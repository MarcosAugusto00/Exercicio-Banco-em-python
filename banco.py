import datetime
import os

formatador = ("%d/%m/%Y %H:%M:%S")

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

def teste_operacao():
    operacao = input("Digite o numero da operação desejada: \n")
    if operacao.isdigit():
        operacao = int(operacao)
        return operacao 
    else:
        operacao = 9
        return operacao
    
def teste_nome():
    while True:    
        nome = input("Digite o seu nome completo: \n")
        os.system('cls')
        nome = nome.strip()
        nome = nome.split(" ")
        if len(nome) < 2:
            os.system('cls')
            print("Nome invalido, por favor digite seu nome completo, não apenas o primeiro nome")
        else:
            os.system('cls')
            nome = " ".join(nome)
            return nome
    
def teste_nascimento():
    while True:
        data_nascimento = input("Digite a sua data de nascimento: [xx/yy/zz] \n")
        os.system('cls')
        if "/" not in data_nascimento:
            dia = data_nascimento[:2]
            mes = data_nascimento[2:4]
            ano = data_nascimento[4:]
            data_nascimento = "/".join([dia, mes, ano])
        data_nascimento = data_nascimento.split("/")
        c = 0
        if len(data_nascimento) == 3: 
            if int(data_nascimento[0]) <= 31 and int(data_nascimento[0]) > 0:
                if len(data_nascimento[0]) <= 2:
                    c += 1
                    data_nascimento[0] = str(data_nascimento[0]).zfill(2)
                else:
                    print("Erro dia")
            if int(data_nascimento[1]) > 0 and int(data_nascimento[1]) <= 12:
                if len(data_nascimento[1]) <= 2:
                    c += 1
                    data_nascimento[1] = str(data_nascimento[1]).zfill(2)   
            if len(data_nascimento[2]) == 2:
                c += 1
            elif len(data_nascimento[2]) == 4:
                data_nascimento[2] = data_nascimento[2][2:]
                c += 1
            if c == 3:
                data_nascimento = "/".join(data_nascimento)
                return data_nascimento
            else:
                os.system('cls')
                print("Data de nascimento invalida, informe dia, mês e ano \n")

def verificar_cpf(cpf):
    contador = 0
    if contas:  # Checa se 'contas' não está vazio
        for conta_info in contas.values():  # Itera sobre cada lista de contas
            for item in conta_info:  # Itera sobre cada lista dentro de conta_info
                if len(item) > 1:  # Verifica se existe mais de um dicionário na lista
                    dados = item[1]  # Acessa o dicionário com os dados do usuário
                    if dados['CPF'] == cpf:  # Verifica se o CPF é o mesmo
                        contador += 1
    return contador

def f_endereco():
    logradouro = input("Digite o nome da sua rua: \n")
    numero_casa = input("Digite o numero da sua casa: \n")
    bairro = input("Digite o nome do seu bairro: \n")
    cidade = input("Digite o nome da sua cidade: \n")
    while True:
        estado = input("Digite a sigla do seu estado: \n")
        if len(estado) != 2:
            os.system('cls')
            print("Estado Invalido, por favor digite a sigla do seu estado \n")
        else:
            break
    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}"
    return endereco

def cadastrousuario(numero_usuario, cpfs, usuario, dicionario_usu, data):
    os.system('cls')
    c = 1
    while True:
        if c == 1 or c == 10:
            nome = teste_nome()
            c += 1
        if c == 2 or c == 20:
            data_nascimento = teste_nascimento()
            c += 1
        if c == 3 or c == 30:
            while True:
                cpf = teste_cpf()
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
                            return numero_usuario, cpfs, usuario, dicionario_usu
                        else:
                            print("       Opção invalida      ")
                else:
                    c += 1  
                    break
        if c == 4 or c == 40:
            endereco = f_endereco()
            dicionario_usu.append({
                "Nome": nome,
                "Data de Nascimento": data_nascimento,
                "CPF": cpf,
                "Endereço": endereco
            })
            c += 1
        teste = True
        while teste:
            cadastro = dicionario_usu[numero_usuario]
            max_width = 40
            print(f"""
                  ----------------------- Dados Cadastrais -----------------------

                    Nome:              {cadastro["Nome"].rjust(max_width)}

                    Data de Nascimento:{cadastro["Data de Nascimento"].rjust(max_width)} 

                    CPF:               {str(cadastro["CPF"]).rjust(max_width)}

                    Endereço: {cadastro["Endereço"].rjust(max_width)}

                  ----------------------------------------------------------------

                             Deseja realizar alguma alteração? [S/N]

                """)
            resp = input()
            resp = testar_resp(resp)
            if resp == "N":
                loop = False
                break
            if resp == "S":
                loop = True
                while True:
                    tela_alterar_dados(data)
                    operacao = teste_operacao()
                    if operacao == 1:
                        c = 10
                        teste = False
                        break
                    elif operacao == 2:
                        c = 20
                        teste = False
                        break
                    elif operacao == 3:
                        c = 30
                        teste = False
                        break
                    elif operacao == 4:
                        c = 40
                        teste = False
                        break
                    elif operacao == 5:
                        teste = False
                        break
                    else:
                        os.system('cls')
                        print("Operação invalida")
            else:
                os.system('cls')
                print("Resposta invalida")
        os.system('cls')
        if loop == False:
            break
    usuario.insert(numero_usuario, dicionario_usu[numero_usuario])  # Adiciona o dicionário no index numero_usuario
    numero_usuario += 1
    cpfs.append(cpf)
    return numero_usuario, cpfs, usuario, dicionario_usu

def achar_index(usuario, cpf):
    indices = [i for i, dicionario in enumerate(usuario) if 'CPF' in dicionario and dicionario['CPF'] == cpf]
    return indices[0] if indices else None

def testar_resp(resp):
    if len(resp) > 0:
        resp = resp.strip().capitalize()
        return resp[0]
    else:
        return "f"

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
    cpf = teste_cpf()
    if cpf in cpfs:
        indice_usu = achar_index(usuario, cpf)
        if indice_usu is not None:
            nome = usuario[indice_usu]['Nome'].split()[0]
            nome_completo = usuario[indice_usu]['Nome']
            contador = 0
            contador = verificar_cpf(cpf)
            while True:
                print(f"""
                                            Olá {nome}!!!
                             Você possui {contador} contas cadastradas em seu CPF
                                   Deseja cadastrar outra nova? [S/N] 
                      """)
                resp = input(" ")
                resp = testar_resp(resp)
                os.system('cls')
                if resp == "S":
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
                elif resp == "N":
                    return contas, numero_conta
                else:
                    os.system('cls')
                    print("Resposta invalida \n\n")
        else:
            print("CPF não cadastrado")
            if not contas:
                contas = {}
            return contas, numero_conta
    else:
        print("CPF não cadastrado")
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

def tela_alterar_dados(data):
    print(f"""
    -----------------Bem vindo ao seu Banco-----------------
          
                      {(data.strftime(formatador))}

    Por favor digite o numero do dado que deseja modificar:

      1 - Nome
      2 - Data de Nascimento
      3 - CPF
      4 - Endereço
      5 - Sair

    --------------------------------------------------------
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
dicionario_usu = []
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
dicionario_usu.append({"CPF" : 0})
while True:
    data_atual = datetime.datetime.now()
    telainicial(data_atual)
    operacao = teste_operacao()
    if operacao == 1:
        data_atual = datetime.datetime.now()
        numero_usuario, cpfs, usuario, dicionario_usu = cadastrousuario(numero_usuario, cpfs, usuario, dicionario_usu, data_atual)
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
                operacao = teste_operacao()
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
                    resp = testar_resp(resp)
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
        else:
            os.system('cls')
            print("Conta inexistente")
    elif operacao == 4:
        telafinal()
        break
    else:
        os.system('cls')
        print("                    Operação invalida\n")
 