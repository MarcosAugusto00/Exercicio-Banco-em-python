import datetime
import os
formatador = ("%d/%m/%Y %H:%M:%S")
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

def telainicio(data):
    print(f"""
    --------------Bem vindo ao seu Banco--------------
          
                    {(data.strftime(formatador))}
      
           Por favor digite a operação desejada:

      1 - Saque
      2 - Deposito
      3 - Extrato

    --------------------------------------------------
      """)
    
extratos = {}
saldo = 0
n = 0
num_ope = 0
while True:
    data_atual = datetime.datetime.now()
    print(data_atual.strftime(formatador))
    telainicio(data_atual)
    operacao = int(input("Operação: "))
    os.system('cls')
    if num_ope <= 10:
        if operacao == 1:
            valor = float(input("Digite o valor que deseja sacar: R$"))
            extratos, saldo, n, num_ope = sacar(valor, extratos,saldo,n, data_atual, num_ope)
        elif operacao == 2:
            valor = float(input("Digite o valor que deseja depositar: R$"))
            extratos, saldo, num_ope = depositar(valor, extratos,saldo, data_atual, num_ope)
        elif operacao == 3:
            extrato(extratos,saldo, data_atual)
        else:
            print("Operação Invalida")
        print("")
        resp = input("Deseja realizar outra operação: [S/N] ")
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
        dataprimeiraope = datetime.date.today
    dataatual = datetime.date.today
    if dataprimeiraope != dataatual:
        num_ope = 0
    if resp.upper() == "S":
        continue
    elif resp.upper() == "N":
        print(f"""
              Obrigado por utilizar o nosso Banco
                       Volte Sempre!!!
              """)
        break
    else:
        print("     Opção invalida")
        print(f"""
              Obrigado por utilizar o nosso Banco
                       Volte Sempre!!!
              """)
        break