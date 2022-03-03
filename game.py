import numpy as np

number = np.random.randint(1, 101)
count = 0
#print (number)

while True:
    count += 1
    predict_num = int(input('Угадайте число от 1 до 100:    '))

    if predict_num < number:
        print('Загаданное число больше')
    elif predict_num > number:
        print('Загаданное число меньше')
    elif predict_num == number:
        print('Вы угадали! Это число = {}, за {} попыток'.format(number, count))
        break