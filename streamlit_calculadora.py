# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-31 15:15:32
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-08-31 15:40:02
import streamlit as st

def main():
    st.title("CALCULADORA")
    num1=st.number_input("Ingrese un número")
    num2=st.number_input("Ingrese otro número")

    if st.button("Suma"):
        addition=num1 + num2
        st.write(f"La suma de los números es: {addition}")
    if st.button("Resta"):  
        substraction=num1 - num2
        st.write(f"La resta de los números es: {substraction}")
    if st.button("Multiplicación"):
        multiplication=num1 * num2
        st.write(f"La multiplicación de los números es: {multiplication}")
    if st.button("División"):
        if num2 != 0:
            division=num1 / num2
            st.write(f"La división de los números es: {division}")
        else:
            st.write("No se puede dividir entre cero")




if __name__ == "__main__":
    main()