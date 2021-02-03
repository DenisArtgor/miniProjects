import random
def generate_password(lenght, chars):
    return random.sample(chars, lenght)

number = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = 'il1Lo0O'
chars = ''

total_pasword = int(input('Введите количество требуемых паролей > '))
length_pasword = int(input('Введите длину пароля от 1 до 9 > '))

custom_number_password = input('Включать ли цифры 0123456789? > '
                               '\nОтветьте, пожалуйста в формате да или нет >')
custom_upper_letter = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? '
                            '\nОтветьте, пожалуйста в формате да или нет > ')
custom_lower_letter = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? '
                            '\nОтветьте, пожалуйста в формате да или нет > ')
custom_symbol = input('Включать ли символы !#$%&*+-=?@^_?'
                      '\nОтветьте, пожалуйста в формате да или нет > ')
exception_in_password = input('Исключать ли неоднозначные символы il1Lo0O ?'
                              '\nОтветьте, пожалуйста в формате да или нет > ')

if custom_number_password.lower() == 'да':
    chars += number
if custom_upper_letter.lower() == 'да':
    chars += uppercase_letters
elif custom_lower_letter.lower() == 'да':
    chars += lowercase_letters
elif custom_symbol.lower() == 'да':
    chars += punctuation

if exception_in_password.lower() == 'да':
    chars = list(chars)
    chars = ''.join((filter(lambda s: s not in exception, chars)))


answer_password = []
new_answer_password = []
for password in range(total_pasword):
    new_answer_password = generate_password(length_pasword, chars)
    new_answer_password = ''.join(new_answer_password)
    answer_password.append(new_answer_password)


print('\n'.join(answer_password))