print('Вас приветствует программа "Шифр Цезаря".')

#  y=(x+k) % n,
# x=(y−k) % n, x — символ открытого текста, y — символ шифрованного текста, n — мощность алфавита (количество символов), а k — шаг
def scrambler(txt, lngUP, lnglow, step):   # шифрование
    answer = ''
    for symbol in txt:
         if symbol.isalpha() and symbol.islower():
             answer += lnglow[(int(lnglow.find(symbol) + int(step))) % len(lnglow)]
         elif symbol.isalpha() and symbol.upper():
             answer += lngUP[(int(lngUP.find(symbol)) + int(step)) % len(lngUP)]
         else:
             answer += symbol
    return answer

def decoder (txt, lngUP, lnglow, step): # дешифратор
    answer = ''
    for symbol in txt:
        if symbol.isalpha() and symbol.islower():
            answer += lnglow[(int(lnglow.find(symbol)) - int(step)) % len(lnglow)]
        elif symbol.isalpha() and symbol.upper():
            answer += lngUP[(int(lngUP.find(symbol)) - int(step)) % len(lngUP)]
        else:
            answer += symbol
    return answer


while True:
    choice_chipher = int(input('Выберите направление: шифрование или дешифрование.'
                               '\nГде 1 - шифрование и 2 - дешифрование > '))
    if choice_chipher == 1 or choice_chipher == 2:
        break
    else:
        print('\nОшибка ввода попробуйте еще раз')

while True:
    language = input('Выберите язык.\nГде ru - русский eng - английский > ')
    if language == 'ru' or language == 'eng':
        break
    else:
        print('\nОшибка ввода попробуйте еще раз')

while True:
    shift_step = input('Введите шаг сдвига (со сдвигом вправо) > ')
    if shift_step.isdigit():
        shift_step == int(shift_step)
        break
    else:
        print('Вы ошиблись при вводе, попробуйте еще раз.')

en_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
text = input('Введите текст > ')

if choice_chipher == 1: # вызов шифрования
    print(f'Вы выбрали зашифровку текста "{text}"')
    if language == 'ru':
        print('Язык русский')
        print(scrambler(text, rus_upper_alphabet, rus_lower_alphabet, shift_step))
    else:
        print('Язык английский')
        print(scrambler(text, en_upper_alphabet, en_lower_alphabet, shift_step))
else:
    print(f'Вы выбрали расшифровку текста "{text}"')
    if language == 'ru':
        print('Язык русский')
        print(decoder(text, rus_upper_alphabet, rus_lower_alphabet, shift_step))
    else:
        print('Язык английский')
        print(decoder(text, en_upper_alphabet, en_lower_alphabet, shift_step))

