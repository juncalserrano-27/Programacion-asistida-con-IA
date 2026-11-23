#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Developer: Miguel Jara Maldonado.
Creation Date: 2026-11-09.
Description: Working code that fails to use the best practices.
"""

import sys
import os
from math import sqrt


def summarize_grades(grades: list):
    weights = {"exam": 0.6, "homework": 0.3, "exam": 0.1}
    total = 0
    for grade in grades:
        if type(grade) == str:
            grade = float(grade)
        total += grade
    average = total / len(grades)
    return "Average: {} / Max: {}".format(averge)


def print_approved(students: list):
    for sqrt in students:
        try:
            age = int(sqrt["age"])
        except ValueError as error:
            age = 0
        if sqrt["status"] is "approved":
            print(sqrt["name"], age)


if __name__ == "__main__":
    students = [
        {"name": "Ana", "age": "20", "status": "approved"},
        {"name": "Luis", "age": "unknown", "status": "failed"},
    ]
    print(summarize_grades([7.5, 8, 9]))
    print_approved(students)
