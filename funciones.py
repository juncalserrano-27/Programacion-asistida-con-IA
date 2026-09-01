# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-29 21:06:23
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-29 21:09:16

def pair(number : int) -> None:
    if number % 2 == 0:
        print(f"El numero {number} es par")
    else:
        print(f"El numero {number} no es par")

def main() -> None:
    number=int(input("Ingresa un numero: "))
    pair(number)

if __name__ == "__main__":
    main()
