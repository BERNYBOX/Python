def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

texto = input("Ingresa una palabra o frase: ")

if es_palindromo(texto):
    print("¡Es un palíndromo! 🎉")
else:
    print("No es un palíndromo. ❌")
