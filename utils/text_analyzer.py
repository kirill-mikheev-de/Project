def text_analyzer(text):
    """
    Анализирует текст и возвращает различную статистику
    """
    if not text:
        return {
            'length': 0,
            'word_count': 0,
            'char_count': {},
            'words': [],
            'unique_words': 0,
            'avg_word_length': 0,
            'contains_digits': False,
            'uppercase_count': 0,
            'lowercase_count': 0
        }
    
    # Основные метрики
    length = len(text)
    words = text.split()
    word_count = len(words)
    
    # Подсчет символов
    char_count = {}
    uppercase_count = 0
    lowercase_count = 0
    contains_digits = False
    
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            contains_digits = True
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Уникальные слова
    unique_words = len(set(words))
    
    # Средняя длина слова
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / word_count if word_count > 0 else 0
    
    return {
        'length': length,
        'word_count': word_count,
        'char_count': char_count,
        'words': words,
        'unique_words': unique_words,
        'avg_word_length': avg_word_length,
        'contains_digits': contains_digits,
        'uppercase_count': uppercase_count,
        'lowercase_count': lowercase_count
    }
