import socket
import os
from man import Terminal
from man import get_funcs
# Моя библиотека имеет возможность подклчючения настроек пути через файл настроек
# Для демонстрации буду использовать упрощённый вариант из методички с созданием папки "docs" в папке со скриптом


PORT = 9107

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
conn, addr = sock.accept()
terminal = Terminal(os.path.join(os.getcwd(), 'docs'))

print("Прослушиваем порт", PORT)
# Получаем доступные функции файлового менеджера
funcs = get_funcs()
funcs_str = str1 = ' '.join(str(e) for e in funcs)

while True:
    answer = ""
    request = conn.recv(1024).decode()
    print(request)
    try:
        request = request.split()
        if request[0] not in funcs:
            answer = f"{request[0]} is not defined.\nList of functions: " + funcs_str + "\n"
        else:
            try:
                answer = getattr(terminal, request[0])(*request[1:])
            except Exception as exc:
                answer = f"Some error: {exc}"

    except IndexError:
        answer = "Failed request"

    if answer is None:
        conn.send("Done".encode())
    else:
        conn.send(answer.encode())

conn.close()
