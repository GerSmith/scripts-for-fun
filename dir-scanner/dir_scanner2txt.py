#! python
# -*- coding: utf-8 -*-

"""
Скрипт сканирует директорию MY_PATH и вложенные в неё каталоги
и возвращает имена всех файлов в ней если они оканчиваются на .pdf
Записывает всю информацию в текстовый файл
"""
import os


MY_PATH = 'L:\\Подразделения\\Электротехнический цех\\АСУ\\!Общая\\Акты дефектации 2017-2020(скан)\\'

# Создаём дерево (объект-генератор) функции walk()
tree = os.walk(MY_PATH)

# Удаляем старый файл если он существует
if os.path.isfile('dir_scanner_files.txt'):
    print('Удаляем старый файл...')
    os.remove('dir_scanner_files.txt')

# записываем вывод скрипта в файл
with open('dir_scanner_files.txt', 'w', encoding='utf-8') as target_file:

    for root, dirs, files in tree:
        for filename in files:
            if filename[-4:] == '.pdf':
                year, name = root[-4:], filename[:-4]
                print(year + '\t' + name + '\n')
                target_file.write(str(year + '\t' + name + '\n'))
