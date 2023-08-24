"""
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""

import math
import random
import csv
import json


def solve_quadratic_equation(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Equation: {a}x^2 + {b}x + {c}")
                print("Roots:", result)
                print()

    return wrapper


def save_to_json(func):
    def wrapper(*args):
        results = func(*args)
        with open('function_results.json', 'a') as json_file:
            json.dump({
                'arguments': args,
                'results': results
            }, json_file)
            json_file.write('\n')
        return results

    return wrapper


@solve_quadratic_equation
@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return None


def generate_csv_file(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


generate_csv_file("file_number", 10)
find_roots("file_number")
