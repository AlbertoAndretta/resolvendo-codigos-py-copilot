def repetir_string():
    # Solicitar a string e o número inteiro como entrada
    string = input("Digite uma string: ")
    num_repeticoes = int(input("Digite o número de repetições: "))

    # Repetir a string o número de vezes informado
    resultado = string * num_repeticoes

    # Retornar o resultado
    return resultado

# Chamar a função e imprimir o resultado
resultado = repetir_string()
print(resultado)