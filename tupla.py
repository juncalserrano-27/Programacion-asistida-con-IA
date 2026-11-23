# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-24 16:02:12
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-24 16:22:03
def main() -> None:
    week_days = (
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes",
        "Sabado",
        "Domingo",
    )
    print(f"El tercer día de la semana es: {week_days[2]}")
    if "Saturday" in week_days:
        print("Saturday está en la tupla")
    else:
        print("Saturday no está en la tupla")

    number = 1
    for day in week_days:
        print(f"Día {number}: {day}")
        number += 1


main()
