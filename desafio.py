menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print(f"O valor de R${valor} foi depositado na sua conta!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        mensagem = ""
        valor = float(input("Informe o valor do depósito: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE
        excedeu_saques = numero_saques > LIMITE_SAQUES
        if excedeu_saldo:
           mensagem = f"Você não tem saldo o suficinete para retirar! Seu saldo: R${saldo} | Valor que desejava sacar: R${valor}\n ------------"
        elif excedeu_limite:
            mensagem = f"Você já excedeu o limite do valor de saque! Valor desejado para sacar R${valor} | Limite é R$500\n ------------"
        elif excedeu_saques:
            mensagem = "Você já alcançou o número de saques do dia que são 3, volte amanhã para sacar\n ------------"
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: {valor:.2f}\n"
            numero_saques += 1
            mensagem = f"O saque com o valor de R${valor} foi realizado com sucesso!"
        else:
            mensagem = "A operação falhou! O valor de saque é inválido\n ------------"
        print(mensagem)
    elif opcao == "e":
        print("------------Extrato------------")
        print(f"{extrato}\nSaldo: {saldo} \n--------------------")
    elif opcao == "q":
        print("O sistema foi encerrado, tenha um ótimo dia!")
        break;
    else:
        print("O valor dado está incorreto!")