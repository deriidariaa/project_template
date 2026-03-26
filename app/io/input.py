import pandas
def input_text():
    """Це функція для введення тексту з консолі"""
    inp = input("Введіть щось: ")
    return inp
def reading_from_file(file_path):
    """Функція для зчитування з файлу за допомогою вбудованих можливостей python"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def reading_from_file_with_pandas(file_path):
    """Функція для зчитування з файлу за допомогою бібліотеки pandas"""
    data = pandas.read_csv(file_path)
    return data.to_string()