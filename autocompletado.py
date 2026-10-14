def is_palindrome():
    """imprime si una palabra es palíndromo o no
    """
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower().replace(" ", "")
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")

def count_vowels():
    """imprime cuántas vocales tiene una palabra
    """
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower().replace(" ", "")
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    print(f"{palabra} tiene {contador} vocal(es).")

def is_prime():
    """imprime si un número es primo
    """
    numero = int(input("Ingrese un número: "))
    if numero < 2:
        print(f"{numero} no es un número primo.")
    else:
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")

def invert_word_order():
    """imprime la palabra al revés
    """
    palabra = input("Ingrese una palabra: ")
    palabra = palabra.lower().replace(" ", "")
    print(f"La palabra al revés es: {palabra[::-1]}")

    