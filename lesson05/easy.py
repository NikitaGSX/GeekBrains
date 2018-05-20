#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
import shutil
import sys

''' Ещё плохо знаком с правилами оформления кода. Посторался соблюсти
рекомендации и мои функции ни чего не выводят, а только возвращают результат.
'''

def change_dir(dir): # Функция изменения директории
    try:
        os.chdir(dir)
#        os.system('cd ' + dir)
        return 'Директория изменена на {}'.format(dir)

    except FileNotFoundError:
        return 'Директории {} не существует'.format(dir)

def list_folder(dir): # Функция просмотра директории
    try:
        folder = []
        for i in os.listdir(dir):
            folder.append(i)
        return 'Содержимое директории {}:\n {}'.format(dir, folder)

    except FileNotFoundError:
        return 'Директории {} не существует'.format(dir)

def rm_folder(name): # Функция удаления директории
    try:
        os.rmdir(name)
        return 'Папка {} удаленна'.format(name)
    except FileNotFoundError:
        return 'Папка {} не существует'.format(name)

def create_folder(name): # Функция создания директории
    try:
        os.mkdir(name)
        return 'Папка {} созданна'.format(name)
    except FileExistsError:
        return 'Папка {} уже существует'.format(name)

# Задание-1
for i in range(9): # Создание директории
    print(create_folder('{}_{}'.format('dir', i+1)))

for i in range(9): # Удаление директории
    print(rm_folder('{}_{}'.format('dir', i+1)))

# Задание-2
# Тут не стал усложнять сделал прямолинейно
print(os.listdir(os.getcwd()))

# Задание-3
# Узнаём название текущего файла и указываем новое имя
f = sys.argv[0]
b = f + '.backup'

# Модуль os позволяет создать жёсткую ссылку, но для корректной работы данной
# процедуры, посмотрим какая система используется. В случае не posix производим
# копирование при помощи модуля shutil
if os.name != 'posix':
     shutil.copy(f, b)
else:
    try:
        os.link(f, b)
        print('Бэкап файла создан')
    except FileExistsError:
        print('Файл с таким именем уже существует')
