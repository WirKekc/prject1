# Игра угадай слово
import random


def index_in_word(w, l, s):
    for i in range(len(w)):
        if w[i] == l:
            s[i] = l
    return s


keywords = []
with open('word_list.txt') as a:
    for line in a:
        keywords.append(line.strip())
word = keywords[random.randint(0, 99)]
# print(word)
life = 3
space = ['_'] * len(word)

while True:
    letter = input('Введите букву: ')
    if letter in word:
        space = index_in_word(word, letter, space)
        print(space)
        if '_' not in space:
            print('Поздравляю, Вы победили!')
            break
    else:
        life -= 1
        print('Нет такой буквы!')
        print('Жизней осталось:', life)
    if life == 0:
        print('Увы, Вы проиграли. Ответом было слово: "'+word+'"')
        break
