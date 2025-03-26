import random
import math

def random_number_operations(iterations):
    """
    Генерирует случайные числа и выполняет над ними различные математические операции
    """
    results = []
    for i in range(iterations):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        # Сложение
        add_result = num1 + num2
        # Вычитание
        sub_result = num1 - num2
        # Умножение
        mul_result = num1 * num2
        # Деление (с обработкой исключения)
        try:
            div_result = num1 / num2
        except ZeroDivisionError:
            div_result = "undefined"
        
        # Возведение в степень
        pow_result = num1 ** num2 if num2 < 5 else "too large"
        # Квадратный корень
        sqrt_result1 = math.sqrt(num1) if num1 >= 0 else "invalid"
        sqrt_result2 = math.sqrt(num2) if num2 >= 0 else "invalid"
        
        
        # Логарифм
        try:
            log_result1 = math.log(num1) if num1 > 0 else "invalid"
            log_result2 = math.log(num2) if num2 > 0 else "invalid"
        except ValueError:
            log_result1 = log_result2 = "invalid"
        
        # Тригонометрические функции
        sin_result1 = math.sin(num1)
        cos_result1 = math.cos(num1)
        tan_result1 = math.tan(num1)
        
        results.append({
            'numbers': (num1, num2),
            'add': add_result,
            'sub': sub_result,
            'mul': mul_result,
            'div': div_result,
            'pow': pow_result,
            'sqrt': (sqrt_result1, sqrt_result2),
            'log': (log_result1, log_result2),
            'trig': (sin_result1, cos_result1, tan_result1)
        })
    
    return results
