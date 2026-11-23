#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Developer: .
Creation Date: .
Description: .
"""
from fastmcp import FastMCP
from pprint import pprint
from courses_catalogue import CATALOGUE

mcp = FastMCP("PlanificadorServer")

student_schedule = []
MAX_CREDITS = 16

@mcp.tool()
def list_courses() -> str:
    """Lista el catálogo de cursos."""
    response_text = "Catalogo de Cursos:\n"
    for code, info in CATALOGUE.items():
        response_text += f"• [{code}] {info['nombre']} | Día: {info['dia']} ({info['hora_inicio']} - {info['hora_fin']}) | Cupos: {info['cupos']}\n"
    return response_text


@mcp.tool()
def get_course(course_query: str) -> str:
    """Da el detalle de una materia puntual."""
    query = course_query.upper().strip()
    if query in CATALOGUE:
        info = CATALOGUE[query]
        return f"📖 [{query}] {info['nombre']} | Créditos: {info['creditos']} | Día: {info['dia']} ({info['hora_inicio']} - {info['hora_fin']}) | Cupos: {info['cupos']}"
    return "No se encontró el curso."


@mcp.tool()
def add_course_to_schedule(course_query: str) -> str:
    """Agrega un curso al horario del alumno restando disponibilidad."""
    global student_schedule
    query = course_query.upper().strip()
    
    if query not in CATALOGUE:
        return "Error: El curso no existe."
        
    course = CATALOGUE[query]
    
    if course["cupos"] <= 0:
        return f"Error: '{course['nombre']}' no tiene cupos."
        
    for s in student_schedule:
        if s["code"] == query:
            return f"Error: Ya tienes inscrito '{course['nombre']}'."
            
    total_credits = sum(s["credits"] for s in student_schedule)
    if total_credits + course["creditos"] > MAX_CREDITS:
        return f"Error: Excede los {MAX_CREDITS} créditos."
        
    for s in student_schedule:
        if s["day"] == course["dia"]:
            if not (course["hora_fin"] <= s["start_time"] or course["hora_inicio"] >= s["end_time"]):
                return f"Error de solapamiento: Choca con '{s['name']}'."

    course["cupos"] -= 1
    student_schedule.append({
        "code": query,
        "name": course["nombre"],
        "day": course["dia"],
        "start_time": course["hora_inicio"],
        "end_time": course["hora_fin"],
        "credits": course["creditos"]
    })
    
    return f"¡Éxito! Curso '{course['nombre']}' agregado."


@mcp.tool()
def get_current_schedule() -> str:
    """Muestra el horario actual del alumno y total de créditos."""
    if not student_schedule:
        return "Tu horario actual está vacío."
        
    response_text = "📅 Horario Actual:\n"
    total_credits = 0
    for s in student_schedule:
        response_text += f"• [{s['code']}] {s['name']} | {s['day']} ({s['start_time']} - {s['end_time']}) | {s['credits']} cr.\n"
        total_credits += s['credits']
        
    response_text += f"\nTotal de créditos: {total_credits} / {MAX_CREDITS}"
    return response_text


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8080)