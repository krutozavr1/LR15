#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает
эту строку в список чисел и возвращает их сумму. Определите декоратор для этой функции,
который имеет один параметр start – начальное значение суммы. Примените декоратор
со значением start=5 к функции и вызовите декорированную функцию. Результат
отобразите на экране.
"""



def modified_sum(func):
    """counts sum of ints in str withh start number"""
    new_sum = 0
    def add_start_to_sum(str, start):
        print(f"start is {start}")
        new_sum = func(str) + start
        print(new_sum)

    return add_start_to_sum


@modified_sum
def sum_in_str(str, start = 0):
    """counts sum of ints in str """
    lst = list(str.split(" "))
    sum = 0
    for i in lst:
        sum += int(i)

    return sum


if __name__ == "__main__":
    str = input()

    sum_in_str(str, 5)
