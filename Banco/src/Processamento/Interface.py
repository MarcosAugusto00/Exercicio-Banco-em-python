import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Gerais import*
from Cadastro import*
from Conta_usuario import *

def run_interface():
    global nova_conta
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