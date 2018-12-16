"""Case-study #7 Proposal generation
Developers:
Selishchev A., Krivosheenkova E., Paymushkin K.,

"""

import random

list_of_symbols = ['"', '#', '$', '%', '&', "'", '(', ')', '*',	'+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']',
                   '^', '`', '{', '|', '}', '~', '_', '«', '»', '—']
end_symbols = [',', '.', '!', '?']
spaces = [' .', ' ,', ' !', ' ?']

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
