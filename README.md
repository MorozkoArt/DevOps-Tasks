# Выполнение тестовых заданий. DevOps. Разработка радиочастотных систем

## Структура проекта

```plaintext
📂DevOps-Tasks/
├──📂radio_frequency_systems/         # Задания для команды: "Радиочастотные системы"
│ ├──📄1.1-1.2_LinuxСommands.md       #  Задание №1 - Linux команды
│ ├──📄extract_path_value.py          #  Задание №2 - Bash/Python скрипт
│ ├──📄cofig.txt                      #  Текст для Задания №2
│ └──📄Dockerfile                     #  Задание №3 - Docker
├──📂1_HTTP_script/                   # 1-ое Задание для Телеком команды
│ └──📄http_checker.py                #  Python скрипт 
├──📂2_Docker_image/                  # 2-ое Задание для Телеком команды 
│ └──📄Dockerfile                     #  Dockerfile
└──📂3_Ansible_automation/            # 3-ье Задание для Телеком команды
  └──📄playbook.yml                   #  playbook
```

## Инструкция по запуску Dockerfile

### Для задания от команды: "Радиочастотные системы"

```bash
# Перейдем в директорию с заданием
cd radio_frequency_systems

# Соберем образ
docker build -t extract_path_value .

# Запустим
docker run --name extract_v extract_path_value

```

### Для задания от Телеком команды

```bash
# Перейдем в коревую директорию, если Вы не в ней
cd ..

# Соберем образ из корня проекта
docker build -f 2_Docker_image/Dockerfile -t http-checker .

# Запустим
docker run --name checker http-checker

# Посмотреть логи
docker logs checker

```

## Инструкция по запуску Ansible playbook

1. Установите Ansible

```bash
pip install ansible
```

2. Измените файл inventory.ini в директории: "3_Ansible_automation"

```ini
# Если запускаете локально - ничего менять не нужно - это готовая конфигурация
[local]
localhost ansible_connection=local  # Для локального запуска

# Для удалённого сервера замените:

#   your-server-ip → IP-адрес или доменное имя сервера
#   ubuntu → имя пользователя на сервере
#   ~/.ssh/your-key.pem → путь к вашему SSH-ключу
[remote]
your-server-ip ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/your-key.pem
```

3. Запустите playbook

```bash
ansible-playbook -i inventory.ini playbook.yml
```
