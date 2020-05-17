# Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.


# def write_to_file(data):
#     with open('text.txt', 'w') as wtf:
#         wtf.write(data)
#         print(data)
#
#
# def read_file_data():
#     with open('text.txt') as rfd:
#         for r in rfd:
#             print(r.strip())


# write_to_file('''Привет медвед!
# мама пока
# здрасте
# лол
# кек
# !!''')

# read_file_data()
# ----------------------------------------------------------------------------------------------------------------------
# Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

# import requests
# import json
#
#
# def write_to_file(data):
#     with open('text.txt', 'w') as wtf:
#         wtf.write(data)
#         print(data)
#
#
# r = requests.get('https://jsonplaceholder.typicode.com/comments')
# di = dict(r.headers)
#
# j = json.dumps(di, indent=2)
# write_to_file(j)
# ----------------------------------------------------------------------------------------------------------------------

# Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие

# import requests
# import re
#
#
# req = requests.get('https://habrahabr.ru/')
# text = req.text
# resault = re.findall(r'http[s]?[\w\d:/\._]+', text)
# print(resault)

import os
print(os.getcwd())
print('/home/dmitry/PycharmProjects/project1/tceh_lesson9' == os.getcwd())
