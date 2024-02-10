def radius_circle(radius):
    return round(3.1415926 * radius ** 2, 4)

def point_in(radius, point):
    return True if (point[1] < radius and point[0] < radius and -point[0] < radius and -point[1] < radius) else False
# Есть значение радиуса круга
#radius = 42

#print(round(3.1415926 * radius ** 2, 4))
# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код


# Далее, пусть есть координаты точки
#point_1 = (23, 34)
# где 23 - координата х, 34 - координата у
#print(True if (point_1[1] < radius and point_1[0] < radius and -point_1[0] < radius and -point_1[1] < radius) else False)


# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код

# Аналогично для другой точки
#point_2 = (30, 30)
#print(True if (point_2[1] < radius and point_2[0] < radius and -point_2[0] < radius and -point_2[1] < radius) else False)


# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


