def sacar(valor, extratos, saldo, n):
    if saldo>=valor:
        n += 1
        if n <= 3:
            saldo -= valor
            print(f"O seu {n}º saque diario de {valor} foi feito")
            extratos.update({"Saque        R$" : valor})
        else:
            print("Você ultrapassou o limite de saques diarios")
    else:
        print("Saldo insuficiente")
    return extratos, saldo, n

def depositar(valor, extratos, saldo):
    saldo += valor
    print("Deposito no valor de {} realizado".format(valor))
    extratos.update({"Deposito     R$" : valor})
    return extratos, saldo

def extrato(extratos, saldo):
    print("----Extrato----")
    for chave, valor in extratos.items():
        print(f'{chave:>10}: {valor:>8.2f}')
    print(f"Saldo total  R$:  {saldo:.2f}")

def telainicio():
    print(f"""
    --------------Bem vindo ao seu Banco--------------
      
           Por favor digite a operação desejada:
      1 - Saque
      2 - Deposito
      3 - Extrato

    --------------------------------------------------
      """)
    
extratos = {}
saldo = 0
n = 0
while True:
    telainicio()
    operacao = int(input("Operação: "))
    if operacao == 1:
        valor = float(input("Digite o valor que deseja sacar: R$"))
        extratos, saldo, n = sacar(valor, extratos,saldo,n)
    elif operacao == 2:
        valor = float(input("Digite o valor que deseja depositar: R$"))
        extratos, saldo = depositar(valor, extratos,saldo)
    elif operacao == 3:
        extrato(extratos,saldo)
    else:
        print("Operação Invalida")
    resp = input("Deseja realizar outra operação: [S/N]")
    if resp.upper() == "S":
        continue
    else:
        print(f"""
              Obrigado por utilizar o nosso Banco
                       Volte Sempre!!!
              """)
        break