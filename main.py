
import os
from time import sleep

print("====================  Seja bem vindo ao RodriguesBank!! ==================")
print("'Transformando seu dia, um passo de cada vez, com nossa tecnologia em missão.'")

saldo = 0
limite = 500
extrato = []
quant_saques = 0

while True:
    print("\nComo podemos lhe ajudar?. Selecione um numero para continuarmos!")

    print("\n[1] Depositar\n[2] Sacar\n[3] Visualizar Extrato\n[4] Sair")
    menu = int(input("\nInsira um numero das opções: "))

    def Deposito(valor):
        print("\n\n***------------------ DEPOSITO ---------------------***")
        global saldo 
        saldo += valor
        print(f"Deposito realizado com sucesso\nSALDO: {saldo}")
        extrato.append(f"+ DEPOSITO: R${valor}")
        print("-----------------------------------------------------------")

    def Saque(valor):
        print("\n\n***------------------ SAQUE ------------------------***")
        global saldo
        saldo -= valor;
        print(f"Saque realizado com sucesso\n SALDO: {saldo}")
        extrato.append(f"- SAQUE: R${valor}")
        print("-----------------------------------------------------------")

    def Extrato():
        print("\n\n***------------------ EXTRATO ----------------------***")
        for i in range(len(extrato)):
            print(extrato[i])
        print("-----------------------------------------------------------")
       
    match menu:       
        case 1:
            #Deposita
            print("Qual o valor que deseja depositar? ")
            valorDeposito = float(input("R$"))
            Deposito(valorDeposito)
        case 2:
            #Saca
            print("Qual o valor que deseja sacar? ")
            valorSaque = float(input("R$"))
            if quant_saques < 3 and valorSaque <= 500:
                if saldo >= valorSaque:
                    Saque(valorSaque)
                    quant_saques += 1
                else:
                    print("\n------------------------------------------------------")
                    print("***Saldo insuficiente para realizar essa operação!!***")
                    print("\n------------------------------------------------------")
            else:
                print("\n------------------------------------------------------------------------")
                print("""Não sera possivel realizar operação por motivos de execer a quantidade 
                      de saques disponiveis por dia ou valor acima do limite permido para saque""")
                print("-------------------------------------------------------------------------")

        case 3:
            #Verifica o extratp 
            Extrato()
            print(f"SALDO: {saldo}")

        case 4:
            #Sair
            print("Até logo, estaremos esperando por voce !")
    sleep(2)
    os.system("cls")


        

        







