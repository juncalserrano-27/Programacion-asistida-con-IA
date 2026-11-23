# -*- coding: utf-8 -*-
# @Author: Lilia Juncal Serrano Duran
# @Date:   2026-08-31 16:04:53
# @Last Modified by:   Lilia Juncal Serrano Duran
# @Last Modified time: 2026-09-01 13:20:29

import streamlit as st

def main():
    st.title("LISTA DE TAREAS")

    if "homework_number" not in st.session_state:
        st.session_state["homework_number"] = 0

    homework = st.text_input("Ingrese la tarea:")

    if st.button("Agregar tarea"):
        if homework != "":
            st.session_state["homework_number"] += 1

            numero = st.session_state["homework_number"]

            st.session_state[f"homework{numero}"] = homework

    st.write("Tareas ingresadas:")

    for i in range(1, st.session_state["homework_number"] + 1):
        st.write(f"Tarea {i}: {st.session_state[f'homework{i}']}")


if __name__ == "__main__":
    main()
