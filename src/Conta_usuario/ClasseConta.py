import os
import datetime
import getpass
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Gerais import *
from Cadastro import *

class Conta:
    
    def __init__(self):
        self.numero_conta = None
        self.agencia = "0001"
        self.usuario = None
        self.senha = None
        self.n_tentativa_senha = 3
        self.data_primeira_operacao = datetime.date.today()
        self.n_saque_diario = 0
        self.n_operacoes_diario = 0
        self.extratos = {}
        self.saque = 0
        self.deposito = 0
        self.saldo = 0
    
    def testar_data(self):
        if self.data_primeira_operacao != datetime.date.today():
            self.n_saque_diario = 0
            self.n_operacoes_diario = 0
            self.data_primeira_operacao = datetime.date.today()
            return self
       
    @staticmethod
    def tela_cadastro_conta():
         print(f"""
              --------------------------------------------
                   Cadastros de nova conta corrente
              --------------------------------------------
          """)
         
    @staticmethod
    def adicionar_conta(cpf, numero_conta):
        if cpf in conta:
            conta[cpf].append(numero_conta)  # Adiciona o novo CPF à lista
        else:
            conta.update({cpf : [numero_conta]}) # Adiciona um novo dicionario em contas, com o CPF como chave, e uma lista de contas daquele CPF como valor
            
    @staticmethod
    def contas_cpf(cpf):
        if cpf in conta:
            contador = len(conta[cpf])
            return contador
        else:
            return 0
        
    @staticmethod
    def achar_nome(cpf):
        for usuario in usuarios:
            if usuario is not None and usuario.cpf == cpf:
                nome = usuario.nome.split()[0]
                return nome
            
    @staticmethod
    def achar_nome_completo(cpf):
        for usuario in usuarios:
            if usuario is not None and usuario.cpf == cpf:
                nome = usuario.nome
                return nome
       
    @staticmethod
    def achar_usuarios(cpf):
        for usuario in usuarios:
            if usuario is not None and usuario.cpf == cpf:
                return usuario   
       
    @staticmethod
    def nova_conta():
        os.system('cls')
        Conta.tela_cadastro_conta()
        cpf = teste_cpf()
        if cpf in cpfs:
            nome = Conta.achar_nome(cpf)
            nome_completo = Conta.achar_nome_completo(cpf)
            contador = Conta.contas_cpf(cpf)
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
                    numero_conta = numero_contas()
                    Conta.adicionar_conta(cpf, numero_conta)
                    print(f"""
                                -----------------------------------------------

                                    Parabéns, você acaba de criar sua nova
                                                conta corrente
                        
                        
                                Agência:          0001
                                Conta corrente: {numero_conta} 
                                Nome:  {nome_completo}


                                        {(data_atual.strftime(formatador))}

                                -----------------------------------------------
                            """)   
                    return numero_conta, cpf
                elif resp == "N":
                    return None, None
                else:
                    os.system('cls')
                    print("Resposta invalida \n\n")
        else:
            print("CPF não cadastrado")
            return None, None           
         
    @staticmethod
    def telainicio():
        print(f"""
        --------------Bem vindo ao seu Banco--------------
            
                        {(data_atual.strftime(formatador))}

            Por favor digite a operação desejada:

        1 - Saque
        2 - Deposito
        3 - Extrato
        4 - Sair

        --------------------------------------------------
        """)     
    
    @staticmethod
    def criar_senha():
        while True:
            print("""
                            ---------------------------------------------------
                
                            Agora precisamos criar umas senha para a sua conta
                
                            ---------------------------------------------------
                """)
            senha = Conta.teste_senha()
            senha = Conta.validar_senha(senha)
            if senha is not None:
                return senha
    
    def validar_senha(senha):
        validar_senha = getpass.getpass("Confirme a sua senha: (Apenas 6 numeros) \n")
        if len(validar_senha) == 6:
            if validar_senha.isdigit():
                validar_senha = int(validar_senha)
                if senha == validar_senha:
                    return validar_senha
            else:
                print("As senhas nao conhecidem")
                return None
        else:
            print("As senhas nao conhecidem")
            return None
                    
    def cadastro_nova_conta(self):
        self.numero_conta, cpf = Conta.nova_conta()
        if self.numero_conta is None:
            cancelar_numero_contas()
            return
        self.senha = Conta.criar_senha()
        self.usuario = Conta.achar_usuarios(cpf)
        global contador_contas
        contador_contas += 1
        return self
        
    def sacar(self):
        valor = float(input("Digite o valor que deseja sacar: \nR$"))
        if self.saldo >= valor:
            self.testar_data()
            self.n_saque_diario += 1
            if self.n_saque_diario <= 3:
                self.n_operacoes_diario += 1
                self.saldo -= valor
                print(f"Operação diária {self.n_operacoes_diario}")
                print(f"O seu {self.n_saque_diario}º saque diário de R${valor:.2f} foi feito")
                data = datetime.datetime.now()
                self.extratos.update({f"Operação {self.n_operacoes_diario}  Saque    ": f"- R${valor:.2f} em {data.strftime(formatador)}"})
            else:
                print("Você ultrapassou o limite de saques diários")
        else:
            print("Saldo insuficiente")
            
    def depositar(self):
        self.testar_data()
        valor = float(input("Digite o valor que deseja depositar: \nR$"))
        self.n_operacoes_diario += 1
        self.saldo += valor
        print(f"Operação diária {self.n_operacoes_diario}")
        print(f"Depósito no valor de R${valor:.2f} realizado")
        data = datetime.datetime.now()
        self.extratos.update({f"Operação {self.n_operacoes_diario}  Deposito ": f"  R${valor:.2f} em {data.strftime(formatador)}"})
        
    def extrato(self):
        largura = 35
        data = datetime.datetime.now()
        print("-------------------------Extrato-------------------------")
        print("")
        print(f"                   {(data.strftime(formatador))}")
        print("")
        for chave, valor in self.extratos.items():
            print(f'{chave:<{largura - 15}}: {valor:10}')
        tela = "Saldo total"
        saldos = f"   R${self.saldo:.2f}"
        print("")
        print("")
        print(f'{tela:<{largura - 14}}:{saldos:10}')
        print("")
        print("---------------------------------------------------------")
        
    def operacoes(self):
        while True:
            Conta.telainicio()
            operacao = teste_operacao()
            os.system('cls')
            if operacao != 4:
                if self.n_operacoes_diario <= 10 or operacao == 3 or operacao == 4:
                    if operacao == 1:
                        self.sacar()
                    elif operacao == 2:
                        self.depositar()
                    elif operacao == 3:
                        self.extrato()
                    elif operacao == 4:
                        return
                    else:
                        print("Operação inválida \n")
                        resp = input("Deseja realizar outra operação: [S/N] \n")
                        resp = testar_resp(resp)
                        os.system('cls')

                else:
                    print("""
                        ---------------------------------------
                                                        
                        Limite de operações diarias atingido: 
                                Por favor volte outro dia       
                                                            
                        ---------------------------------------
                        """)
                    resp = input("\n Deseja realizar outra operação: [S/N] \n")
                    if resp.upper() == "S":
                        continue
                    elif resp.upper() == "N":
                        telafinal()
                        return
                    else:
                        print("Opção invalida")
            else:
                telafinal()
                return
            
    @staticmethod
    def login():
        while True:
            try:
                numero_conta = int(input("Digite o numero da conta que deseja acessar: \n"))
                break
            except ValueError:
                os.system('cls')
                print("Numero de conta invalido, por favor digite um numero valido")
        for conta_usu in contas:
            if conta_usu is not None and conta_usu.numero_conta == numero_conta:
                while True:
                    senha = conta_usu.teste_senha()
                    if conta_usu.n_tentativa_senha > 0:
                        if conta_usu.senha == senha:
                            os.system('cls')
                            conta_usu.n_tentativa_senha = 3
                            return conta_usu
                        else:
                            os.system('cls')
                            conta_usu.n_tentativa_senha -= 1
                            print("Senha invalida \n")
                            print(f"Restam {conta_usu.n_tentativa_senha} tentativas")
                    else:
                        print("""
                            -------------------------------
                                
                            Limite de tentativa atingidos
                                
                            Por favor consulte seu gerente
                                
                            -------------------------------
                            """)
                        return None
        os.system('cls')    
        print("Numero de conta nao encontrado!")
        return None
    
    @staticmethod
    def teste_senha():
        while True:
            senha = getpass.getpass("Digite a sua senha: (Apenas 6 numeros)\n")
            if len(senha) == 6:
                if senha.isdigit():
                    senha = int(senha)
                    return senha
                else:
                    os.system('cls')
                    print("Senha invalida, a sua senha deve possuir apenas numeros")
            else:
                os.system('cls')
                print("Senha invalida, a sua senha deve possuir 6 numeros")
                