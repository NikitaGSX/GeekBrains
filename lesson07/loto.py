#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержи 3 строки по 9 клеток.
В каждой строке по 5 случайных цифр,расположенных по возрастанию.
Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random
import sys
 
bag = list(range(1, 91))
 
 
class Card():
    def __init__(self):
        self.count = 0
        self.rows = [[], [], []]
        numbers = list(range(1, 91))
        for i in range(3):
            self.rows[i] = [' '] * 9
            row_length = list(range(0, 9))
            rand_numbers = []
            rand_positions = []
            for j in range(5):
                rand_numbers.append(numbers.pop(random.randint(0, len(numbers) - 1)))
                rand_positions.append(row_length.pop(random.randint(0, len(row_length) - 1)))
            rand_numbers.sort()
            rand_positions.sort()
            for j in range(5):
                self.rows[i][rand_positions[j]] = rand_numbers[j]
 
    def print_card(self):
        for row in self.rows:
            print(row)
 
    def mark_number(self, number):
        check = 0
        for row in self.rows:
            if number in row:
                row[row.index(number)] = 'X'
                self.count += 1
            else:
                check += 1
        if check == 3:
            print('Вы зачеркнули неверный номер. Вы проиграли')
            sys.exit()
 
    def check_number(self, number):
        for row in self.rows:
            if number in row:
                print('Вы не зачеркнули нужный номер. Вы проиграли')
                sys.exit()
 
player_card = Card()
enemy_card = Card()
 
while True:
    print('Ваша карточка')
    player_card.print_card()
    print('Карточка противника')
    enemy_card.print_card()
 
    number = bag.pop(random.randint(0, len(bag) - 1))
    print('Номер ' + str(number) + '!')

    while True:
        choice = input('=== Вы зачеркнете номер? (y/n):')
        if choice == 'y':
            player_card.mark_number(number)
            break
        elif choice == 'n':
            player_card.check_number(number)
            break
        else:
            print('непонятно')
    for row in enemy_card.rows:
        if number in row:
            enemy_card.mark_number(number)
    if player_card.count == 15:
        print('Вы зачеркнули все номера. Вы выиграли')
        sys.exit()
    elif enemy_card.count == 15:
        print('Противник зачеркнул все номера. Вы проиграли')
        sys.exit()
 
