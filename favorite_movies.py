def movie(my_favorite_movies):
    lst = []
    lst.append(my_favorite_movies[:10])
    lst.append(my_favorite_movies[-15:])
    lst.append(my_favorite_movies[12:25])
    lst.append(my_favorite_movies[-22:-17])
    return lst

# Есть строка с перечислением фильмов

#my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
#print(my_favorite_movies[:10])
#print(my_favorite_movies[-15:])
#print(my_favorite_movies[12:25])
#print(my_favorite_movies[-22:-17])

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
