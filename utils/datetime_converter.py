
from datetime import datetime

def datetime_converter(input_date, input_format, output_format):
    """
    Конвертирует дату из одного формата в другой
    """
    try:
        # Парсинг входной даты
        parsed_date = datetime.strptime(input_date, input_format)
        
        # Преобразование в новый формат
        converted_date = parsed_date.strftime(output_format)
        
        # Дополнительная информация
        day_of_week = parsed_date.strftime("%A")
        day_of_year = parsed_date.timetuple().tm_yday
        week_number = parsed_date.isocalendar()[1]
        is_leap_year = (parsed_date.year % 4 == 0 and 
                       (parsed_date.year % 100 != 0 or parsed_date.year % 400 == 0))
        

        


        return {
            'original_date': input_date,
            'converted_date': converted_date,
            'day_of_week': day_of_week,
            'day_of_year': day_of_year,
            'week_number': week_number,
            'is_leap_year': is_leap_year,
            'success': True,
            'error': None
        }
    except ValueError as e:
        return {
            'original_date': input_date,
            'converted_date': None,
            'day_of_week': None,
            'day_of_year': None,
            'week_number': None,
            'is_leap_year': None,
            'success': False,
            'error': str(e)
        }
