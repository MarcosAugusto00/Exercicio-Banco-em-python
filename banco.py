import os
import datetime
import getpass

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

class Usuario:
    
    usuarios_cadastrados = []
    
    def __init__(self):
        self.nome = None
        self.data_nascimento = None
        self.endereco = None
        self.cpf = None
        Usuario.usuarios_cadastrados.append(self)
     
    @staticmethod
    def tela_alterar_dados():
        print(f"""
        -----------------Bem vindo ao seu Banco-----------------
            
                        {(data_atual.strftime(formatador))}

        Por favor digite o numero do dado que deseja modificar:

        1 - Nome
        2 - Data de Nascimento
        3 - CPF
        4 - Endereço
        5 - Sair

        --------------------------------------------------------
        """)
            
    @staticmethod
    def teste_endereco():
        os.system('cls')
        while True:
            logradouro = input("Digite o nome da sua rua: \n")
            logradouro = logradouro.strip()
            logradouro = logradouro.split(" ")
            if len(logradouro) < 2:
                os.system('cls')
                print("Logradouro invalido, por favor digite nome completo do logradouro e seu tipo")
            else:
                os.system('cls')
                logradouro = " ".join(logradouro)
                break
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

    @staticmethod
    def teste_nome():
        os.system('cls')
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
            
    @staticmethod
    def teste_data_nascimento():
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
                if len(data_nascimento[0]) <= 2:
                    c += 1
                    data_nascimento[0] = str(data_nascimento[0]).zfill(2)
                else:
                    print("Erro dia")
                if len(data_nascimento[1]) <= 2:
                    c += 1
                    data_nascimento[1] = str(data_nascimento[1]).zfill(2)   
                if len(data_nascimento[2]) == 2:
                    if int(data_nascimento[2]) > 20:
                        data_nascimento[2] = "19" + data_nascimento[2]
                    else:
                        data_nascimento[2] = "20" + data_nascimento[2]
                    c += 1
                elif len(data_nascimento[2]) == 4:
                    data_nascimento[2] = data_nascimento[2]
                    c += 1
                if c == 3:
                    data_nascimento = "/".join(data_nascimento)
                    try:
                        datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
                        return data_nascimento
                    except ValueError:
                        os.system('cls')
                        print("Data de nascimento invalida, informe dia, mês e ano validos \n")
                else:
                    os.system('cls')
                    print("Data de nascimento invalida, informe dia, mês e ano a \n")
                    
    @staticmethod
    def teste_usuario_cpf():
        i = True
        while i:
            cpf = teste_cpf()
            i, cpf = Usuario.verificar_cpf_usuario(cpf)
        return cpf
            
    def sair(self):
        Usuario.usuarios_cadastrados.remove(self)
                
    @staticmethod
    def verificar_cpf_usuario(cpf):
        for usuario in Usuario.usuarios_cadastrados:
            if usuario.cpf == cpf:
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
                        return True, cpf
                    elif respf == 2:
                        return False, None
                    else:
                        os.system('cls')
                        print("       Opção invalida      ")
            else:
                return False, cpf 
        
    
    @staticmethod
    def mostrar_cadastro(nome, data_nascimento, cpf, endereco):
        while True:
            max_width = 40
            print(f"""
                    ----------------------- Dados Cadastrais -----------------------

                        Nome:              {nome.rjust(max_width)}

                        Data de Nascimento:{data_nascimento.rjust(max_width)} 

                        CPF:               {str(cpf).rjust(max_width)}

                        Endereço: {endereco.rjust(max_width)}

                    ----------------------------------------------------------------

                                Deseja realizar alguma alteração? [S/N]

                    """)
            resp = input()
            resp = testar_resp(resp)
            if resp == "N":
                return 1
            if resp == "S":
                while True:
                    Usuario.tela_alterar_dados()
                    operacao = teste_operacao()
                    if operacao == 1:
                        return 10
                    elif operacao == 2:
                        return 20
                    elif operacao == 3:
                        return 30
                    elif operacao == 4:
                        return 40
                    elif operacao == 5:
                        return None
                    else:
                        os.system('cls')
                        print("Operação invalida")
       
    def cadastro(self):
        c = 0
        while True:
            if c == 0 or c == 30:
                self.cpf = Usuario.teste_usuario_cpf()
                if self.cpf is None:
                    self.sair()
                    return
            if c == 0 or c == 10:
                self.nome = Usuario.teste_nome() 
            if c == 0 or c == 20:
                self.data_nascimento = Usuario.teste_data_nascimento() 
            if c == 0 or c == 40:
                self.endereco = Usuario.teste_endereco()
            c = Usuario.mostrar_cadastro(self.nome, self.data_nascimento, self.cpf, self.endereco)
            if c == 1:
                cpfs.append(self.cpf)
                global contador_usuarios
                contador_usuarios += 1
                return self
            if c is None:
                os.system('cls')
                telafinal()
                self.sair()
                return

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
                        
                        
                                Agência:         {nova_conta.agencia}
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
    
usuarios = []  
contas = []
contador_usuarios = 0
contador_contas = 0

while True:
    telainicial(data_atual)
    operacao = teste_operacao()
    if operacao == 1:
        while True:
            if len(usuarios) <= contador_usuarios:
                usuarios.append(None)
            else:
                break
        novo_usuario = Usuario()
        novo_usuario.cadastro()
        usuarios.insert(contador_usuarios, novo_usuario)
    elif operacao == 2:
        while True:
            if len(contas) <= contador_contas:
                contas.append(None)
            else:
                break
        nova_conta = Conta()
        nova_conta.cadastro_nova_conta()
        contas.insert(contador_contas, nova_conta)
    elif operacao == 3:
        conta_operacao = Conta.login()
        if conta_operacao is not None:
            conta_operacao.operacoes()
    elif operacao == 4:
        telafinal()
        break
    else:
        os.system('cls')
        print("Operação Invalida \n Por favor digite uma operação valida:")
