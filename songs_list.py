#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round


def three_song(violator_songs_list):
    lst = []
    for i in range(0, 9, 3):
        lst.append(round(violator_songs_list[i][1] + violator_songs_list[i + 1][1] + violator_songs_list[i + 2][1], 2))
    return f"Три песни звучат {*lst,} минут"
# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)


# Есть словарь песен группы Depeche Mode


# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
def other_songs(violator_songs_dict):
    return f"А другие три песни звучат {round(violator_songs_dict['Blue Dress'] + violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'], 2)} минут"
