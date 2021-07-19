from time import sleep

import numpy as np
from numpy import random
import pandas as pd


def gen_random_values(random_cards=10000000):
    # r_array = np.arange(1, 21, dtype=int)

    # f_card = [random.choice(r_array, size=4, replace=False) for each in range(random_cards)]

    # Генерим случайные числа / карточки карта 2
    entries_left = pd.DataFrame(random.randint(1, 21, size=(int(random_cards * 1.4), 4)),
                                columns=['l_first_c2', 'l_second_c2', 'l_third_c2', 'l_fourth_c2'])
    # Фильтруем повторяющиеся цифры в карточке
    entries_left['double_c2'] = np.where((entries_left['l_first_c2'] == entries_left['l_second_c2'])
                                         | (entries_left['l_first_c2'] == entries_left['l_third_c2'])
                                         | (entries_left['l_first_c2'] == entries_left['l_fourth_c2'])
                                         | (entries_left['l_second_c2'] == entries_left['l_third_c2'])
                                         | (entries_left['l_second_c2'] == entries_left['l_fourth_c2'])
                                         | (entries_left['l_third_c2'] == entries_left['l_fourth_c2']), 1, -1)
    # Удаляем карточки в которых есть повторяющиеся цифры
    entries_left = entries_left[entries_left.double_c2 < 0]
    # Выравниваем массив до нужных размеров
    entries_left = entries_left.iloc[:, :-1]
    entries_left = entries_left.iloc[:random_cards]
    # Перестраиваем индексы
    entries_left.reset_index(drop=True, inplace=True)

    entries_right = pd.DataFrame(random.randint(1, 21, size=(int(random_cards * 1.4), 4)),
                                 columns=['r_first_c2', 'r_second_c2', 'r_third_c2', 'r_fourth_c2'])
    # Фильтруем повторяющиеся цифры в карточке
    entries_right['double_c2'] = np.where((entries_right['r_first_c2'] == entries_right['r_second_c2'])
                                          | (entries_right['r_first_c2'] == entries_right['r_third_c2'])
                                          | (entries_right['r_first_c2'] == entries_right['r_fourth_c2'])
                                          | (entries_right['r_second_c2'] == entries_right['r_third_c2'])
                                          | (entries_right['r_second_c2'] == entries_right['r_fourth_c2'])
                                          | (entries_right['r_third_c2'] == entries_right['r_fourth_c2']), 1, -1)
    # Удаляем карточки в которых есть повторяющиеся цифры
    entries_right = entries_right[entries_right.double_c2 < 0]
    # Выравниваем массив до нужных размеров
    entries_right = entries_right.iloc[:, :-1]
    entries_right = entries_right.iloc[:random_cards]
    # Перестраиваем индексы
    entries_right.reset_index(drop=True, inplace=True)

    all_entries = pd.concat([entries_left, entries_right], axis=1)

    # Карточки и ответы сгенерили для одной части, далее вторая часть
    sleep(1)

    # Генерим случайные числа / карточки карта 1
    all_cards_left = pd.DataFrame(random.randint(1, 21, size=(int(random_cards * 1.4), 4)),
                                  columns=['l_first_c1', 'l_second_c1', 'l_third_c1', 'l_fourth_c1'])

    # Фильтруем повторяющиеся цифры в карточке
    all_cards_left['double_c1'] = np.where((all_cards_left['l_first_c1'] == all_cards_left['l_second_c1'])
                                           | (all_cards_left['l_first_c1'] == all_cards_left['l_third_c1'])
                                           | (all_cards_left['l_first_c1'] == all_cards_left['l_fourth_c1'])
                                           | (all_cards_left['l_second_c1'] == all_cards_left['l_third_c1'])
                                           | (all_cards_left['l_second_c1'] == all_cards_left['l_fourth_c1'])
                                           | (all_cards_left['l_third_c1'] == all_cards_left['l_fourth_c1']), 1, -1)
    # Удаляем карточки в которых есть повторяющиеся цифры
    all_cards_left = all_cards_left[all_cards_left.double_c1 < 0]
    # Выравниваем массив до нужных размеров
    all_cards_left = all_cards_left.iloc[:, :-1]
    all_cards_left = all_cards_left[:random_cards]
    # Перестраиваем индексы
    all_cards_left.reset_index(drop=True, inplace=True)

    all_cards_right = pd.DataFrame(random.randint(1, 21, size=(int(random_cards * 1.4), 4)),
                                   columns=['r_first_c1', 'r_second_c1', 'r_third_c1', 'r_fourth_c1'])
    # Фильтруем повторяющиеся цифры в карточке
    all_cards_right['double_c1'] = np.where((all_cards_right['r_first_c1'] == all_cards_right['r_second_c1'])
                                            | (all_cards_right['r_first_c1'] == all_cards_right['r_third_c1'])
                                            | (all_cards_right['r_first_c1'] == all_cards_right['r_fourth_c1'])
                                            | (all_cards_right['r_second_c1'] == all_cards_right['r_third_c1'])
                                            | (all_cards_right['r_second_c1'] == all_cards_right['r_fourth_c1'])
                                            | (all_cards_right['r_third_c1'] == all_cards_right['r_fourth_c1']), 1, -1)
    # Удаляем карточки в которых есть повторяющиеся цифры
    all_cards_right = all_cards_right[all_cards_right.double_c1 < 0]
    # Выравниваем массив до нужных размеров
    all_cards_right = all_cards_right[:random_cards]
    all_cards_right = all_cards_right.iloc[:, :-1]
    all_cards_left.reset_index(drop=True, inplace=True)

    all_cards = pd.concat([all_cards_left, all_cards_right, all_entries], axis=1)

    # Первая карта просчет
    all_cards['que_first_c1'] = np.where((all_cards['l_first_c1'] == all_cards['r_first_c1'])
                                         | (all_cards['l_first_c1'] == all_cards['r_second_c1'])
                                         | (all_cards['l_first_c1'] == all_cards['r_third_c1'])
                                         | (all_cards['l_first_c1'] == all_cards['r_fourth_c1']), 1, 0)
    all_cards['que_second_c1'] = np.where((all_cards['l_second_c1'] == all_cards['r_first_c1'])
                                          | (all_cards['l_second_c1'] == all_cards['r_second_c1'])
                                          | (all_cards['l_second_c1'] == all_cards['r_third_c1'])
                                          | (all_cards['l_second_c1'] == all_cards['r_fourth_c1']), 1, 0)
    all_cards['que_third_c1'] = np.where((all_cards['l_third_c1'] == all_cards['r_first_c1'])
                                         | (all_cards['l_third_c1'] == all_cards['r_second_c1'])
                                         | (all_cards['l_third_c1'] == all_cards['r_third_c1'])
                                         | (all_cards['l_third_c1'] == all_cards['r_fourth_c1']), 1, 0)
    all_cards['que_forth_c1'] = np.where((all_cards['l_fourth_c1'] == all_cards['r_first_c1'])
                                         | (all_cards['l_fourth_c1'] == all_cards['r_second_c1'])
                                         | (all_cards['l_fourth_c1'] == all_cards['r_third_c1'])
                                         | (all_cards['l_fourth_c1'] == all_cards['r_fourth_c1']), 1, 0)

    # Вторая карта просчет
    all_cards['que_first_c2'] = np.where((all_cards['l_first_c2'] == all_cards['r_first_c2'])
                                         | (all_cards['l_first_c2'] == all_cards['r_second_c2'])
                                         | (all_cards['l_first_c2'] == all_cards['r_third_c2'])
                                         | (all_cards['l_first_c2'] == all_cards['r_fourth_c2']), 1, 0)
    all_cards['que_second_c2'] = np.where((all_cards['l_second_c2'] == all_cards['r_first_c2'])
                                          | (all_cards['l_second_c2'] == all_cards['r_second_c2'])
                                          | (all_cards['l_second_c2'] == all_cards['r_third_c2'])
                                          | (all_cards['l_second_c2'] == all_cards['r_fourth_c2']), 1, 0)
    all_cards['que_third_c2'] = np.where((all_cards['l_third_c2'] == all_cards['r_first_c2'])
                                         | (all_cards['l_third_c2'] == all_cards['r_second_c2'])
                                         | (all_cards['l_third_c2'] == all_cards['r_third_c2'])
                                         | (all_cards['l_third_c2'] == all_cards['r_fourth_c2']), 1, 0)
    all_cards['que_forth_c2'] = np.where((all_cards['l_fourth_c2'] == all_cards['r_first_c2'])
                                         | (all_cards['l_fourth_c2'] == all_cards['r_second_c2'])
                                         | (all_cards['l_fourth_c2'] == all_cards['r_third_c2'])
                                         | (all_cards['l_fourth_c2'] == all_cards['r_fourth_c2']), 1, 0)
    # считаем суммы совпадений в первой
    all_cards['sum_c1'] = all_cards[['que_first_c1', 'que_second_c1', 'que_third_c1', 'que_forth_c1']].sum(axis=1)
    # считаем суммы совпадений во второй
    all_cards['sum_c2'] = all_cards[['que_first_c2', 'que_second_c2', 'que_third_c2', 'que_forth_c2']].sum(axis=1)

    return [math3x4or4x3(all_cards), math2x4or4x2(all_cards), math1x4or4x1(all_cards), math0x4or4x0(all_cards)]


# считаем 4х4
def math4x4(all_cards):
    # Совпали 4 первая и 4 вторая
    united_cards_matched = all_cards.loc[((all_cards['sum_c2'] == 4)
                                          & (all_cards['sum_c1'] == 4))]
    return united_cards_matched.shape[0]


# считаем 3х3
def math3x3(all_cards):
    united_cards_matched = all_cards.loc[((all_cards['sum_c2'] == 3)
                                          & (all_cards['sum_c1'] == 3))]
    return united_cards_matched.shape[0]


# считаем 2х2
def math2x2(all_cards):
    united_cards_matched = all_cards.loc[((all_cards['sum_c2'] == 2)
                                          & (all_cards['sum_c1'] == 2))]
    return united_cards_matched.shape[0]


# считаем 3х4 или 4x3
def math3x4or4x3(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 3)
                                             & (all_cards['sum_c1'] == 4))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 4)
                                             & (all_cards['sum_c1'] == 3))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 2х4 или 4x2
def math2x4or4x2(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 2)
                                             & (all_cards['sum_c1'] == 4))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 4)
                                             & (all_cards['sum_c1'] == 2))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 1х4 или 4x1
def math1x4or4x1(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 1)
                                             & (all_cards['sum_c1'] == 4))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 4)
                                             & (all_cards['sum_c1'] == 1))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 0х4 или 4x0
def math0x4or4x0(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 0)
                                             & (all_cards['sum_c1'] == 4))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 4)
                                             & (all_cards['sum_c1'] == 0))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 2х3 или 3x2
def math2x3or3x2(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 2)
                                             & (all_cards['sum_c1'] == 3))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 3)
                                             & (all_cards['sum_c1'] == 2))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 1х3 или 3x1
def math1x3or3x1(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 1)
                                             & (all_cards['sum_c1'] == 3))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 3)
                                             & (all_cards['sum_c1'] == 1))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 1х3 или 3x1
def math0x3or3x0(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 0)
                                             & (all_cards['sum_c1'] == 3))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 3)
                                             & (all_cards['sum_c1'] == 0))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 1х2 или 2x1
def math1x2or2x1(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 2)
                                             & (all_cards['sum_c1'] == 1))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 1)
                                             & (all_cards['sum_c1'] == 2))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]


# считаем 0х2 или 2x0
def math0x2or2x0(all_cards):
    united_cards_matched_p1 = all_cards.loc[((all_cards['sum_c2'] == 2)
                                             & (all_cards['sum_c1'] == 0))]
    united_cards_matched_p2 = all_cards.loc[((all_cards['sum_c2'] == 0)
                                             & (all_cards['sum_c1'] == 2))]
    return united_cards_matched_p2.shape[0] + united_cards_matched_p1.shape[0]
