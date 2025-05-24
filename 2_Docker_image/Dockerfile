FROM ubuntu:22.04

# Установка зависимостей
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install requests && \
    rm -rf /var/lib/apt/lists/*

# Копируем скрипт
COPY 1_HTTP_script/http_checker.py /app/http_checker.py

# Рабочая директория
WORKDIR /app

# Команда запуска
CMD ["python3", "http_checker.py"]