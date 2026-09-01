# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-24 16:36:56
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-24 16:45:28
def main()->None:
    inventory = {"borrador": 15, "cuaderno": 8,"regla": 12}

    print(f"Los productos que hay en el inventario son: {list(inventory.keys())}")
    print(f"El total  de unidades en inventario es: {sum(inventory.values())}")
    inventory["lapiz"] = 50
    inventory["cuaderno"] = 20
    print(f"El diccionario final es: {list(inventory.items())}")

main()