# TODO импортировать необходимые молули


import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def csv_to_json(input_filename, output_filename): # Определение функции для преобразования CSV в JSON
    data = [] # Создание пустого списка для хранения данных
    with open(input_filename, 'r') as file: # Открытие входного файла в режиме чтения
        reader = csv.DictReader(file) # Создание объекта-читателя для файла CSV
        for row in reader: # Чтение каждой строки из файла
            data.append(row) # Добавление строки в список данных

    with open(output_filename, 'w') as file: # Открытие выходного файла в режиме записи
        json.dump(data, file, indent=4) # Преобразование списка данных в формат JSON и запись его в файл

def main(): # Определение основной функции main
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME) # Вызов функции для преобразования CSV в JSON

    with open(OUTPUT_FILENAME) as output_f: # Открытие выходного файла
        for line in output_f: # Чтение каждой строки из файла
            print(line, end="") # Вывод строки

if __name__ == '__main__': # Проверка, запущен ли данный скрипт напрямую
    main() # Вызов основной функции
