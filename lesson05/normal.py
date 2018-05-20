#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
import easy

answer = input('Выберите нужное:\n \
               1 - Перейти в папку\n \
               2 - Просмотр текущей папки\n \
               3 - Удалить папку\n \
               4 - Создать папку\n\r')

if answer == '1':
    dir = input('Укажите директорию:\n ')
    print(easy.change_dir(dir))

elif answer == '2':
    dir = input('Укажите директорию и/или нажмите Enter: ')
    if dir == '':
        dir = os.getcwd()
    print(easy.list_folder(dir))

elif answer == '3':
    dir = input('Укажите папку для удаления: ')
    try:
        print(easy.rm_folder(dir))
    except:
        pass

elif answer == '4':
    name = input('Введите имя для новой папки:\n ')
    print(easy.create_folder(name))

else:
    print('Извини, в ответах я ограничен - правильно задавай вопросы')
