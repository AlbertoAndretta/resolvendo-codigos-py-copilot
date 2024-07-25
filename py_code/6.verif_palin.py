def eh_palindromo(palavra):
    # Remover espaços e converter para minúsculas para comparar de forma case-insensitive
    palavra = palavra.replace(" ", "").lower()
    
    # Inverter a palavra
    palavra_invertida = palavra[::-1]
    
    # Comparar a palavra original com a invertida
    return palavra == palavra_invertida

# Testar a função
palavra = input("Digite uma palavra: ")
if eh_palindromo(palavra):
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo.")