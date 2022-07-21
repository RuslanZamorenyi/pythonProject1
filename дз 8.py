# Задание 1
# Создайте функцию, которая выводит приветствие для пользователя с заданным именем.
# Если имя не указано, она должна выводить приветствие для пользователя с Вашим именем

# def your_name():
#     a = input("ведіть ваше ім'я:")
#     if a:
#         print("привіт", a)
#     else:
#         print("привіт Руслан!")
# your_name()

# Задание 2
# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.

import numpy as np
def function_1(number1):
    if number1 > 0:
        return number1 * 4
    elif number1 < 0:
        return number1 * -1

def function_2():
    for x in np.arange(-5, 6, 0.5):
        y = function_1(x)
        print("function_1(", x, ") = ", y, sep = "")

function_2()




# def calculator():
#     c = input("Ведіть операцію(сложение, вычитание, умножение, деление=\n(для виведення результату напишить '('")
#
#     if c == "сложение":
#         sums = 0.0
#         s = float(input("напишіть число"))
#         while s != 00:
#             sums += s
#             s = float(input("напишіть число"))
#         print("сума=", sums)
#
#     elif c == "деление":
#         sums = float(input("ведіть перше число"))
#         s = float(input("напишіть число"))
#
#         while s != 00:
#             sums /= s
#             s = float(input("напишіть число"))
#             if s == 0:
#                 print("на 0 ділити не можна ")
#                 break
#         else:
#             print("сума", sums)
#
#     elif c == "вычитание":
#         sums = float(input("ведіть перше число"))
#         s = float(input("напишіть число"))
#         while s != 00:
#             sums -= s
#             s = float(input("напишіть число"))
#         print("сума", sums)
#
#     elif c == "умножение":
#         sums = float(input("ведіть перше число"))
#         s = float(input("напишіть число"))
#         while s != 00:
#             sums *= s
#             s = float(input("напишіть число"))
#         print("сума", sums)
#     else:
#         print("оберіть інший варіант")
#
# calculator()






