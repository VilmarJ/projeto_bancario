menu = """
    Escolha uma opção:

    [d] => Depósito

    [s] => Saque

    [e] => Extrato

"""

LIMITE_SAQUES = 3
numero_saques = 0
limite = 500
extrato = ""
saldo = 0


while True:

    opcao = input(menu)
                  
    if opcao == "d":
            
        valor_deposito = float(input('Digite o valor do deposito em R$: '))

        if valor_deposito > 0:
            saldo += valor_deposito

            extrato += f'Entrada de R$:{valor_deposito:.2f} \n'

            print(f'Deposito de R$:{valor_deposito:.2f} feito com sucesso.')
            print(f'Saldo atual: R${saldo:.2f}')

        else: print("O valor depositado precisa ser maior que ZERO.")
    
    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: R$ "))

        if saldo < valor_saque:
            print(f"Não é possível sacar o valor de R${valor_saque:.2f} pois o seu saldo atual é R${saldo:.2f}")
            continue
            
        if valor_saque > 500:
            print("O limite máximo de saque é de R$500 reais!")
            continue

        saldo -= valor_saque
        extrato += f"Saída de R$:{valor_saque:.2f}"

        if numero_saques >= 3:
            print("A quantidade máxima de saques já foi realizada.")
            continue

        numero_saques += 1


        print(f"Saque de R$:{valor_saque:.2f}")
        print(f'Saldo atual: R${saldo:.2f}')
        
    elif opcao == "e":
        print(extrato)
        print(f'Saldo atual: R${saldo:.2f}')

    elif opcao == "sair":
        break

    else:
        print("Operação inválida, verifique as opções disponíveis no menu.")