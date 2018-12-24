"""Case-study #7 Proposal generation
Developers:
Selishchev A., Krivosheenkova E., Paymushkin K.,

"""

import random
from collections import defaultdict
import ru_local

list_of_symbols = ['"', '#', '$', '%', '&', "'", '(', ')', '*',	'+', '/', ':', ';', '<', '=', '>', '@', '[', ']',
                   '^', '`', '{', '|', '}', '~', '_', '«', '»', '—']
end_symbols = ['.', '!', '?']
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
        file_str = input('{}'.format(ru_local.NUM))
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

#Получаем "звенья и связи" и заносим в словарь функцией create_dict()
dict_txt = create_dict(list_text)

#Получаем список стартовых слов - начинающихся с заглавной буквы
start_words = []
for ch in list_text:
    if ch == ch.capitalize():
        if not ch in start_words:
            start_words.append(ch)

last_words = []
for sh in list_text:
    if sh in end_symbols:
        if not sh in last_words:
            last_words.append(sh)

n = int(input('{}'.format(ru_local.NUM)))
rave_text = []
for i in range(0,n):
    w1 = random.choice(start_words)
    rave_text.append(w1)

    a1 = dict_txt.get(w1)
    w2 = random.choice(a1)
    if w2 in last_words:
        while w2 in last_words:
            w2 = random.choice(a1)
        rave_text.append(w2)
    else:
        rave_text.append(w2)

    a2 = dict_txt.get(w2)
    w3 = random.choice(a2)
    rave_text.append(w3)

    a3 = dict_txt.get(w3)
    w4 = random.choice(a3)
    rave_text.append(w4)

    a4 = dict_txt.get(w4)
    w5 = random.choice(a4)
    rave_text.append(w5)

    a5 = dict_txt.get(w5)
    w6 = random.choice(a5)
    rave_text.append(w6)

    a6 = dict_txt.get(w6)
    w7 = random.choice(a6)
    rave_text.append(w7)

    a7 = dict_txt.get(w7)
    w8 = random.choice(a7)
    rave_text.append(w8)

    a8 = dict_txt.get(w8)
    w9 = random.choice(a8)
    rave_text.append(w9)

    a9 = dict_txt.get(w9)
    w10 = random.choice(a9)
    rave_text.append(w10)

    a10 = dict_txt.get(w10)
    w11 = random.choice(a10)
    rave_text.append(w11)

    a11 = dict_txt.get(w11)
    w12 = random.choice(a11)
    rave_text.append(w12)

    a12 = dict_txt.get(w12)
    w13 = random.choice(a12)
    rave_text.append(w13)

    a13 = dict_txt.get(w13)
    w14 = random.choice(a13)
    rave_text.append(w14)

    a14 = dict_txt.get(w14)
    w15 = random.choice(a14)
    rave_text.append(w15)

    a15 = dict_txt.get(w15)
    w16 = random.choice(a15)
    rave_text.append(w16)

    a16 = dict_txt.get(w16)
    w17 = random.choice(a16)
    rave_text.append(w17)

    a17 = dict_txt.get(w17)
    w18 = random.choice(a17)
    rave_text.append(w18)

    a18 = dict_txt.get(w18)
    w19 = random.choice(a18)
    rave_text.append(w19)

str_rave_text = ' '.join(rave_text)
print(str(str_rave_text))
