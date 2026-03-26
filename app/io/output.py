def output(text):
    """Функція для виводу тексту в консоль"""
    print(text)
def writing_to_file(file_path, text):
    """Функція для запису до файлу за допомогою вбудованих можливостей python"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)