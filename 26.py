"""Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии."""

def power(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    elif exponent < 0:
        return power(1/base, -exponent)
    else:
        return base * power(base, exponent - 1)

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

result = power(A, B)
print(f"Результат: {A} в степени {B} = {result}")