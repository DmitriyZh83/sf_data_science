"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def fork_method_predict(number: int = 1) -> int:
    """Угадываем число методом артиллерийской вилки
    Определяем центр числового отрезка.
    Если не попали в искомое число - работаем с отрезком спарва или слева.
    Координаты точки на отрезке - реальное число (float).
    Его надо перевести в целое (int), чтобы сверить с загаданным.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    borders = [0,101] # задаём начало и конец поиска
    while True:
        count += 1
        center = (borders[0]+borders[1])/2 # Определяем центр отрезка
        if int(center) == number:
            break  # выход из цикла если попали
        elif int(center) < number:
            borders[0] = center # Если загаданное число больше - ищем от центра до конца
        elif int(center) > number:
            borders[1] = center # Если загаданное число меньше - ищем от начала до центра
    return count


def score_game(fork_method_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(fork_method_predict(number))

    score = round(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(fork_method_predict)