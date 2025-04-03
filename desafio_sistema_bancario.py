menu = """

[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair

"""

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor >= saldo
        excedeu_limite = valor >= limite_por_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Falha na operação! Saldo insuficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "e":
        # menu_extrato = "Extrato"
        print("Extrato".center(37, "-"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print("".center(37, "-"))

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")