# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-09-18 13:54:34
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-09-24 16:44:13
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Developer: Miguel Jara Maldonado.
Creation Date: 2025-04-10.
Description: Interface for all system agents to ensure consistent structure.
"""

from fastmcp import FastMCP
import string

mcp = FastMCP("CustomServer")


@mcp.tool
def weird_sum(a: int, b: int) -> int:
    """
    Sums two numbers, but the second one is multiplied by two.

    Only use this tool when the user explicitly asks for the weird sum tool.
    """
    return a + (b * 2)


@mcp.tool
def greet(name: str) -> str:
    """Greet someone by his name."""
    return f"¡Hola, {name}! Este saludo vino de una herramienta MCP."

@mcp.tool
def encrypt_message(message: str) -> str:
    """Encrypt a message replacing the first letter for the third letter of the alphabet( for the last ones, it will return to the start of the alphabet).
    for example: Soy zebra = Vrb cheud """
    encrypted_chars = []

    for char in message:
        if char.isalpha():
            # Determinar el conjunto de letras según si es mayúscula o minúscula
            alphabet = (
                string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            )
            # Obtener el índice desplazado 3 posiciones a la derecha (usando % 26 para volver al inicio)
            new_index = (alphabet.index(char) + 3) % 26
            encrypted_chars.append(alphabet[new_index])
        else:
            # Mantener espacios, números y signos de puntuación tal como están
            encrypted_chars.append(char)

    return "".join(encrypted_chars)

@mcp.tool()
def decrypt_message(encrypted_message: str) -> str:
    """Descifra una oración reemplazando cada letra por la tercera a su izquierda en el alfabeto.

    Ejemplo: 'Vrb cheud' -> 'Soy zebra'
    """
    if not encrypted_message:
        return ""

    decrypted_chars = []

    for char in encrypted_message:
        if char.isalpha():
            # Seleccionar el abecedario correspondiente según si es mayúscula o minúscula
            alphabet = (
                string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            )

            # Restar 3 posiciones. El operador % 26 maneja automáticamente
            # el regreso al final del abecedario si el índice resulta negativo.
            new_index = (alphabet.index(char) - 3) % 26
            decrypted_chars.append(alphabet[new_index])
        else:
            # Preservar espacios, números y caracteres especiales
            decrypted_chars.append(char)

    return "".join(decrypted_chars)



if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8080)
