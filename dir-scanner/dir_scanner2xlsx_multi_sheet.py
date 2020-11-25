#! python
# -*- coding: utf-8 -*-

"""
Скрипт сканирует директорию MY_PATH и вложенные в неё каталоги
и возвращает имена всех файлов в ней если они оканчиваются на .pdf
Записывает всю информацию в файл MS Excel
"""
import os

# pip install XlsxWriter
import xlsxwriter

MY_PATH = 'L:\\Подразделения\\Электротехнический цех\\АСУ\\!Общая\\Акты дефектации 2017-2020(скан)\\'

# Создаём дерево (объект-генератор) функции walk()
tree = os.walk(MY_PATH)

# Удаляем старый файл если он существует
if os.path.isfile('dir_scanner_files.xlsx'):
    print('Удаляем старый файл...')
    os.remove('dir_scanner_files.xlsx')

# Создаём новый файл Excel
workbook = xlsxwriter.Workbook('dir_scanner_files.xlsx')

# Добавляем жирный шрифт для подсветки
bold = workbook.add_format({'bold': True})

# записываем вывод скрипта в файл
for root, dirs, files in tree:
    # Создаём лист с именем директории root_name
    root_name = os.path.basename(root)
    # пропуск текущей директории ('.'), т.к. в ней нет файлов
    if root_name == '':
        continue
    worksheet = workbook.add_worksheet(root_name)
    # Готовим шапку таблицы
    worksheet.write('A1', 'Год', bold)
    worksheet.set_column('B:B', 50)
    worksheet.write('B1', 'Наименование', bold)
    # счётчики для установки позиций
    cnt_i = 1
    # перебираем все файлы
    for filename in files:
        if filename[-4:] == '.pdf':
            year, name = root[-4:], filename[:-4]
            worksheet.write(cnt_i, 0, year)
            worksheet.write(cnt_i, 1, name)
            cnt_i += 1

workbook.close()
