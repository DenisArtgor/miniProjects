count_answer = 0
true_number = 1
false_namber = 100

while True:
    guess_number = int((true_number + false_namber) / 2)
    print('Твое число равно, меньше или больше, чем число ', guess_number)
    the_answer = int(input('Введите 1. 2 . 3....где 1 - равно, 2 больше, 3 меньше  '))

    if the_answer == 3:
        count_answer += 1
        print("Загаданное число меньше")
        false_namber = guess_number
    elif the_answer == 2:
        count_answer += 1
        true_number = guess_number
        print("Загаданное число больше")
    elif the_answer == 1:
        break
print('Вы угадали с ', count_answer)