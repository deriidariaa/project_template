from app.io.input import input_text, reading_from_file, reading_from_file_with_pandas
from app.io.output import output, writing_to_file
def main():
    text = input_text()
    output(f"Введено в консоль: {text}")
    writing_to_file("data/result_from_console.txt", text)
    try:
        file_data=reading_from_file("data/test.txt")
        output(f"Зчитано: {file_data}")
        writing_to_file("data/result_from_file.txt", file_data)
    except FileNotFoundError:
        print("Нема такого файлу")
    
    try:
        file_data1 =reading_from_file_with_pandas("data/test.csv")
        output("Зчитано: ", file_data1)
        writing_to_file("data/result_from_pandas.txt", file_data1)
    except Exception as e:
        print("Error!")
if __name__ == "__main__":
    main()
