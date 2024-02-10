#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

def zoos():
    return zoo


# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

def insert(num, name, lst):
    lst.insert(num, name)
    return lst
# добавьте птиц из списка birds в последние клетки зоопарка
#for i in birds:
    #zoo.append(i)


#  и выведите список на консоль
#print(zoo)
def delete(word, lst):
    lst.remove(word)
    return lst
# уберите слона
#  и выведите список на консоль
#zoo.remove('elephant')

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
#print(f"{zoo.index('lion') + 1}\n{zoo.index('lark') + 1}")
