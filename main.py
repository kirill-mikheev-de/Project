from utils.datetime_converter import datetime_converter
from utils.random_number_operations import random_number_operations
from utils.text_analyzer import text_analyzer


# Основная функция, которая использует все три функции
def main():
    print("Демонстрация работы программы с тремя функциями")
    print("=" * 50 + "\n")
    
    # Демонстрация функции 1
    print("Функция 1: Генератор случайных чисел с операциями")
    random_results = random_number_operations(5)
    for i, result in enumerate(random_results, 1):
        print(f"\nРезультат {i}:")
        print(f"Числа: {result['numbers']}")
        print(f"Сложение: {result['add']}")
        print(f"Вычитание: {result['sub']}")
        print(f"Умножение: {result['mul']}")
        print(f"Деление: {result['div']}")
        print(f"Степень: {result['pow']}")
        print(f"Квадратные корни: {result['sqrt']}")
        print(f"Логарифмы: {result['log']}")
        print(f"Тригонометрические функции (sin, cos, tan): {result['trig']}")
    print("\n" + "=" * 50 + "\n")
    
    # Демонстрация функции 2
    print("Функция 2: Анализатор текста")
    sample_text = """
    Python — высокоуровневый язык программирования общего назначения, 
    ориентированный на повышение производительности разработчика и читаемости кода. 
    Синтаксис ядра Python минималистичен. В то же время стандартная библиотека 
    включает большой объём полезных функций. Python поддерживает несколько 
    парадигм программирования, в том числе структурное, объектно-ориентированное, 
    функциональное, императивное и аспектно-ориентированное. Основные архитектурные 
    черты — динамическая типизация, автоматическое управление памятью, 
    полная интроспекция, механизм обработки исключений, поддержка многопоточных 
    вычислений, высокоуровневые структуры данных. Поддерживается разбиение 
    программ на модули, которые, в свою очередь, могут объединяться в пакеты.
    """
    analysis = text_analyzer(sample_text)
    print(f"Длина текста: {analysis['length']} символов")
    print(f"Количество слов: {analysis['word_count']}")
    print(f"Уникальные слова: {analysis['unique_words']}")
    print(f"Средняя длина слова: {analysis['avg_word_length']:.2f} символов")
    print(f"Содержит цифры: {'Да' if analysis['contains_digits'] else 'Нет'}")
    print(f"Прописные буквы: {analysis['uppercase_count']}")
    print(f"Строчные буквы: {analysis['lowercase_count']}")
    print("\nТоп 5 самых частых символов:")
    sorted_chars = sorted(analysis['char_count'].items(), key=lambda x: x[1], reverse=True)[:5]
    for char, count in sorted_chars:
        print(f"'{char}': {count} раз")
    print("\n" + "=" * 50 + "\n")
    
    # Демонстрация функции 3
    print("Функция 3: Конвертер дат и времени")
    date_formats = [
        ("25-12-2022", "%d-%m-%Y", "%Y/%m/%d"),
        ("2023.01.15", "%Y.%m.%d", "%B %d, %Y"),
        ("07/04/1776", "%m/%d/%Y", "%A, %d %B %Y"),
        ("invalid date", "%d-%m-%Y", "%Y-%m-%d")
    ]
    
    for input_date, input_fmt, output_fmt in date_formats:
        result = datetime_converter(input_date, input_fmt, output_fmt)
        print(f"\nИсходная дата: {input_date} (формат: {input_fmt})")
        if result['success']:
            print(f"Конвертированная дата: {result['converted_date']} (формат: {output_fmt})")
            print(f"День недели: {result['day_of_week']}")
            print(f"День года: {result['day_of_year']}")
            print(f"Номер недели: {result['week_number']}")
            print(f"Високосный год: {'Да' if result['is_leap_year'] else 'Нет'}")
        else:
            print(f"Ошибка конвертации: {result['error']}")
    
    print("\n" + "=" * 50 + "\n")
    print("Демонстрация завершена!")


if __name__ == "__main__":
    main()