# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-24 15:41:50
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-24 16:22:25
def main() -> None:
    numbers=[12, 45, 7, 23, 56, 8, 34]

    print(f"La suma de los numeros es: {sum(numbers)}")
    print(f"El promedio de los numeros es: {sum(numbers)/len(numbers)}")
    print(f"El numero mayor es: {max(numbers)}")
    print(f"El numero menor es: {min(numbers)}")

    cont=0
    for number in numbers:
        if number>13:
            cont+=1
        
    print(f"El total de numeros mayores a 13 es: {cont}")

main()