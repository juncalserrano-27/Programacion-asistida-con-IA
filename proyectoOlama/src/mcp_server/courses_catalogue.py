#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Developer: Miguel Jara Maldonado.
Creation Date: 2026-09-23.
Description: Courses catalogue for the MCP server lab.

Course structure:
- nombre: str
- creditos: int
- dia: str            -> "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"
- hora_inicio: str     -> formato "HH:MM" (24h)
- hora_fin: str        -> formato "HH:MM" (24h)
- cupos: int           -> available seats (0 = full)

"""

CATALOGUE = {
    "CALC1": {
        "nombre": "Cálculo I",
        "creditos": 4,
        "dia": "Lunes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00",
        "cupos": 12,
    },
    "CALC2": {
        "nombre": "Cálculo II",
        "creditos": 4,
        "dia": "Lunes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00",
        "cupos": 10,
    },
    "PROG1": {
        "nombre": "Programación I",
        "creditos": 5,
        "dia": "Lunes",
        "hora_inicio": "10:00",
        "hora_fin": "12:30",
        "cupos": 20,
    },
    "PROG2": {
        "nombre": "Programación II",
        "creditos": 5,
        "dia": "Martes",
        "hora_inicio": "10:00",
        "hora_fin": "12:30",
        "cupos": 15,
    },
    "BD1": {
        "nombre": "Bases de Datos",
        "creditos": 4,
        "dia": "Lunes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00",
        "cupos": 8,
    },
    "ESTR_DATOS": {
        "nombre": "Estructuras de Datos",
        "creditos": 5,
        "dia": "Miércoles",
        "hora_inicio": "08:00",
        "hora_fin": "10:30",
        "cupos": 14,
    },
    "SIST_OP": {
        "nombre": "Sistemas Operativos",
        "creditos": 4,
        "dia": "Jueves",
        "hora_inicio": "10:00",
        "hora_fin": "12:00",
        "cupos": 0,
    },
    "REDES1": {
        "nombre": "Redes de Computadores",
        "creditos": 4,
        "dia": "Viernes",
        "hora_inicio": "08:00",
        "hora_fin": "10:00",
        "cupos": 10,
    },
    "HIST1": {
        "nombre": "Historia I",
        "creditos": 3,
        "dia": "Miércoles",
        "hora_inicio": "14:00",
        "hora_fin": "16:00",
        "cupos": 25,
    },
    "HIST2": {
        "nombre": "Historia II",
        "creditos": 3,
        "dia": "Jueves",
        "hora_inicio": "14:00",
        "hora_fin": "16:00",
        "cupos": 25,
    },
    "FIS1": {
        "nombre": "Física I",
        "creditos": 4,
        "dia": "Miércoles",
        "hora_inicio": "14:00",
        "hora_fin": "16:00",
        "cupos": 16,
    },
    "FIS2": {
        "nombre": "Física II",
        "creditos": 4,
        "dia": "Martes",
        "hora_inicio": "14:00",
        "hora_fin": "16:00",
        "cupos": 12,
    },
    "ING1": {
        "nombre": "Inglés I",
        "creditos": 2,
        "dia": "Martes",
        "hora_inicio": "08:00",
        "hora_fin": "09:30",
        "cupos": 30,
    },
    "ING2": {
        "nombre": "Inglés II",
        "creditos": 2,
        "dia": "Jueves",
        "hora_inicio": "08:00",
        "hora_fin": "09:30",
        "cupos": 30,
    },
    "ESTAD1": {
        "nombre": "Estadística",
        "creditos": 4,
        "dia": "Martes",
        "hora_inicio": "10:00",
        "hora_fin": "12:00",
        "cupos": 18,
    },
    "ETICA1": {
        "nombre": "Ética Profesional",
        "creditos": 2,
        "dia": "Viernes",
        "hora_inicio": "10:00",
        "hora_fin": "11:30",
        "cupos": 20,
    },
    "ELEC_ARTE": {
        "nombre": "Electiva: Historia del Arte",
        "creditos": 2,
        "dia": "Viernes",
        "hora_inicio": "12:00",
        "hora_fin": "13:30",
        "cupos": 15,
    },
    "ELEC_MUS": {
        "nombre": "Electiva: Apreciación Musical",
        "creditos": 2,
        "dia": "Jueves",
        "hora_inicio": "16:00",
        "hora_fin": "17:30",
        "cupos": 0,
    },
}
