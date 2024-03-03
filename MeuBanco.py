NUMERO_SAQUES = 3
LIMITE_POR_SAQUE = 500
saldoConta = 0.00
valorSaque = 0.00
valorDeposito = 0.00
qtdeSaque = 0
extrato =""

MENU = """
=============MENU============
DIGITE SUA OPÇÃO DE OPERAÇÃO

SALDO    [1]
SAQUE    [2]
DEPOSITO [3]
EXTRATO  [4]
SAIR     [q]
=============================
"""
user=input("USUÁRIO: ")
paswd=input("SENHA: ")

if user=="leto" and paswd=="123":
    print("Acesso liberado com sucesso!")

    while True:
        print(MENU)
        opcao = input("")

        if opcao == "1":
            print(f"Seu saldo atual é: {saldoConta:.2f}")

        if opcao == "2":
            valorSaque = float(input("Digite o valor do saque: "))

            if qtdeSaque > NUMERO_SAQUES:
                print(f"Quantidades diárias de saques excedidas >:{NUMERO_SAQUES}")
            else:
                if valorSaque > saldoConta:
                    print("\n" * 130)
                    print("Não é possível o saque, valor maior do que o saldo!")
                    continue
                else:
                    saldoConta -= valorSaque
                    qtdeSaque +=1
                    print(f"Saque concluído, saldo atualizado no valor de:{saldoConta:.2f}")
                    extrato += f"|Saque   |---Valor R$ {valorSaque:.2f} \n"

        if opcao == "3":
            valorDeposito = float(input("Digite o valor do deposito: "))
            saldoConta += valorDeposito
            print(f"Seu saldo atual é: {saldoConta}")
            extrato += f"|Depósito|---Valor R$ {valorDeposito:.2f} \n"

        if opcao == "4":
            
            if extrato == "":
                print("\n" * 130)
                print("Não há informação para mostrar no extrato")
            else:
                print("=======VALORES EXTRATO=======")
                print (extrato)

        if opcao == "q":
            print("Sistema será encerrado!")
            break


else:
    print("Acesso negado!")    