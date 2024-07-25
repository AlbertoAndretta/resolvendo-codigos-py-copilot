def operacao_simples():
    # Solicitar os dois números como entrada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Solicitar a operação a ser realizada
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = int(input("Digite o número da operação: "))

    # Realizar a operação
    if opcao == 1:
        resultado = num1 + num2
    elif opcao == 2:
        resultado = num1 - num2
    elif opcao == 3:
        resultado = num1 * num2
    elif opcao == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: não é possível dividir por zero!")
            return
    else:
        print("Erro: opção inválida!")
        return

    # Imprimir o resultado
    print(f"O resultado da operação é: {resultado}")

# Chamar a função
operacao_simples()