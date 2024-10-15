import os
import datetime
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Gerais import *

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