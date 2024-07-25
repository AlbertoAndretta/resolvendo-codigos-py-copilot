def verificar_paridade(numero):
    """
    Verifica se um número é par ou ímpar.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        str: "Par" se o número for par, "Ímpar" caso contrário.
    """
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Exemplo de uso:
numero = int(input("Digite um número: "))
print(verificar_paridade(numero))