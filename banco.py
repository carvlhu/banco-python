menu = """

    Bem vindo ao Banco
    
    Opções:
    [1] - Depositar
    [2] - Sacar
    [3] - Ver Extrato
    [4] - Sair

"""

saldo = 3000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    option = input(menu)

    if option == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\n Depósito no valor de R${valor_deposito:.2f}"
        
        else:
            print("Valor informado inválido.")
    
    elif option == "2":

        valor_saque = float(input("Digite o valor do Saque: "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        if excedeu_limite:
            print("Operação falhou! Valor de saque maior que seu limite")

        elif excedeu_saldo:
            print("Operação falhou! Valor de saque maior que valor da conta")

        elif excedeu_saques:
            print("Operação falhou! Número de saques diários atingidos")

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"\n Saque no valor de R${valor_saque:.2f}"

        else: 
            print("Valor informado inválido.")

    elif option == "3":
        print("\n $$$$$$$$$$$ Histórico de transações:")
        print("Não foram realizadas transações na sua conta." if not extrato else extrato)
        print(f"\nSeu saldo atual é de R${saldo:.2f} \n")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    elif option == "4":
        break

    else:
        print("Nenhuma opção selecionada, Escolha novamente")