import sys
import re

def search_in_file(filename, pattern):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if re.search(pattern, line, re.IGNORECASE):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: ./extract_path_value.py <файл> <шаблон>")
        sys.exit(1)
    
    search_in_file(sys.argv[1], sys.argv[2])