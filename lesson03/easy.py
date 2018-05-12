#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import random

number = random.uniform(0, 100)
answer = (input("Хотите огруглить случайное число? (Y/N/q):")).upper()


def my_round(ndigits):
    return round(number, ndigits)

def my_format(number):
    return "{:.2f}".format(number)

def my_round1(ndigits, number=number):
    number = number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)

def lucky_ticket(t):
    num = str(t)
    first = int(num[0]) + int(num[1])
    last = int(num[-1]) + int(num[-2])
    return first - last

if answer == "Y":
    ndigits = int(input("До какого знака нужно округлить?: "))
    print(my_round(ndigits), "Округлиние случайного числа \
при помощи функции round")

elif answer == "N":
    number = float(input("Введите число, которое нужно огруглить:\n"))
    print(my_format(number), "Огругление до второго знака \
используя функцию format")

elif answer == "Q":
    ndigits = int(input("До какого знака нужно округлить?: "))
    print(my_round1(ndigits), "Округлиние случайного числа \
при помощи математики")

else:
    print("Ответ {} не ясен".format(answer))

while True:
    try:
        t = int(input("Введите номер вашего билета:\n"))
    except ValueError:
        print("Номер может содержать только цифры! Будь внимательнее.")
    else:
        if lucky_ticket(t) == 0:
            print("Удивительно! У вас счастливый билет!")
            break
        elif lucky_ticket(t) !=0:
            print("Неудача приследует тебя в этой жизни повсюду.")
            break
