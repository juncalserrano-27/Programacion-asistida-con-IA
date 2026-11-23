# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-24 15:24:55
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-24 16:22:15

def main() -> None:
    number=int(input("Ingresa el numero del que desea realizar la tabla de multiplicar: "))
    count=1
    mul=0
    while count <= number:
        mul=count*number
        print(f"{mul} ")
        count+=1
main()
    