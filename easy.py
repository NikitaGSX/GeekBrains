#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

from datetime import date

def age():
    born = input("Введите вашу дату рождения:\n")
    if born.isdigit():
        today = date.today()
        return today.year - int(born)
    else:
        print("Нужно ввести число!")

def number():
    a = input("Введите ваше счастливое число:\n")
    if a.isdigit():
        return int(a)
    else:
        print("И всё же нужно ввести любимое число!")

__author__ = 'Дриманович Никита Витальевич'

age = age()
num = number()
ran = list(str(num))
out = len(ran)

while 0 < out:
    print('\n'.join(ran))
    out -= out

#print("Ваше число {}, и вы родились {} года назад".format(num, age))
c = age - num
b = num + c
a = num - c

print('A = {0}; B = {1}'.format(a, b))

if  age < 18:
      print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешён")
