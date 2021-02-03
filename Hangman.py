import random
word_list = ['КЛЮЧ',]
def get_word():
    return random.choice(word_list)

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(f'Слово из {len(word)} букв ', *word_completion, sep='')
    while True:
        word_input = input('Введите слово или букву >> ')
        word_input = word_input.upper()
        if not word_input.isalpha():
            print('Вы ошиблись попробуйте снова')
            continue
        if word_input in guessed_letters or word_input in guessed_words:
            print('Уже было')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Поздравляем вы угадали слово !')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'Вы не угадали, осталось попыток - {tries}')
                print(display_hangman(tries))

        if word_input in word:
            guessed_letters.append(word_input)
            for i in word:
                if i not in guessed_letters:
                    print('Угадали букву')
                    print_word(word, guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:
                print_word(word, guessed_letters)
                print('Поздравляем, вы угадали слово! Вы победили!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'Не верно, осталось попыток {tries}')
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print(f'Вы не смогли угадать слово: {word}')
            break


play(get_word().upper())




