"""Case-study #7 Proposal generation
Developers:
Selishchev A., Krivosheenkova E., Paymushkin K.,

"""

import random
from collections import defaultdict

list_of_symbols = ['"', '#', '$', '%', '&', "'", '(', ')', '*',	'+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']',
                   '^', '`', '{', '|', '}', '~', '_', '«', '»', '—', '–']
end_symbols = [',', '.', '!', '?']
spaces = [' .', ' ,', ' !', ' ?']

def create_dict(ltxt):
    d = defaultdict(list)
    unique_word = []
    for wrd in ltxt:
        if wrd not in unique_word:
            unique_word.append(wrd)
    for wrd in unique_word:
        for kk in range(len(ltxt) -1):
            if ltxt[kk] == wrd:
                stn = ltxt[kk + 1]
                we = False
                for ii in range(len(d[wrd])):
                    if stn == d[wrd][ii]:
                        we = True
                        break
                    else:
                        we = False
                if not we:
                    d[wrd].append(stn)
    return d

while True:
    try:
        file_str = input('Имя файла: ')
        with open(file_str) as f_in:
            text = f_in.read()
    except FileNotFoundError:
        print('Файл {} не найден'.format(file_str))
        continue
    break

for i in text:
    if i in list_of_symbols:
        text = text.replace(i, '')
for j in spaces:
    if j in text:
        if j == ' .':
            text = text.replace(j, '.')
        elif j == ' ,':
            text = text.replace(j, ',')
        elif j == ' !':
            text = text.replace(j, '!')
        elif j == ' ?':
            text = text.replace(j, '?')

#Делим текст на слова и заносим в список
list_text = list(text.split())
print(list_text)

#Получаем "звенья и связи" и заносим в словарь функцией create_dict()
dict_txt = create_dict(list_text)
print(dict_txt)

#Получаем список стартовых слов - начинающихся с заглавной буквы
start_words = []
for ch in list_text:
    if ch == ch.capitalize():
        if not ch in start_words:
            start_words.append(ch)

print(start_words)

