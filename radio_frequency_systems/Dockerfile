FROM ubuntu:latest

# Объединяем RUN команды для уменьшения количества слоев
RUN apt-get update && \
    apt-get install -y \
    wget \
    python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Копируем все файлы одной командой
COPY extract_path_value.py config.txt /tmp/

# Устанавливаем права одной командой
RUN chmod +x /tmp/extract_path_value.py

# Указываем рабочую директорию
WORKDIR /tmp

CMD ["python3", "extract_path_value.py", "config.txt", "path"]