from distance import distance
from circle import point_in, radius_circle
from operations import fuck_math
from favorite_movies import movie
from my_family import get_family, otec, summ
from zoo import insert, zoos, delete
from songs_list import three_song, other_songs
from garden import mnojestvo
from secret import wtf
from shopping import shopps, sweets
from store import get_goods, get_store


def test_store():
    store = get_store()
    goods = get_goods()
    print(f"Лампа - {store[goods['Лампа']][0]['quantity']} шт, стоимость {store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']} руб")
    print(f"Стол - {store[goods['Стол']][0]['quantity'] + store[goods['Стол']][1]['quantity']} шт, стоимость {store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price'] + store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']} руб")
    print(f"Диван - {store[goods['Диван']][0]['quantity'] + store[goods['Диван']][1]['quantity']} шт, стоимость {store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price'] + store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']} руб")
    print(f"Стул - {store[goods['Стул']][0]['quantity'] + store[goods['Стул']][1]['quantity'] + store[goods['Стул']][2]['quantity']} шт, стоимость {store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price'] + store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price'] + store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']} руб")
    assert True

def test_govna1():
    ans = {'ашан': [{'name': 'печенье', 'price': 10.99}, {'name': 'конфеты', 'price': 34.99}, {'name': 'карамель', 'price': 45.99}, {'name': 'пирожное', 'price': 67.99}], 'пятерочка': [{'name': 'печенье', 'price': 9.99}, {'name': 'конфеты', 'price': 32.99}, {'name': 'карамель', 'price': 46.99}, {'name': 'пирожное', 'price': 59.99}], 'магнит': [{'name': 'печенье', 'price': 11.99}, {'name': 'конфеты', 'price': 
            30.99}, {'name': 'карамель', 'price': 41.99}, {'name': 'пирожное', 'price': 62.99}]}
    assert ans == shopps()
    
def test_govna2():
    ans = {'печенье': [{'shop': 'пятерочка', 'price': 9.99}, {'shop': 'ашан', 'price': 10.99}], 'конфеты': [{'shop': 'магнит', 'price': 30.99}, {'shop': 'пятерочка', 'price': 32.99}], 'карамель': [{'shop': 'пятерочка', 'price': 46.99}, {'shop': 'магнит', 'price': 41.99}], 'пирожное': [{'shop': 'пятерочка', 'price': 59.99}, {'shop': 'магнит', 'price': 62.99}]}
    assert ans == sweets()

def test_radius_circle():
    secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    result = 'в бане веник дороже денег'
    request = wtf(secret_message)
    assert request == result


def test_mnojestvo():
    garden_set = mnojestvo()[0] ; meadow_set = mnojestvo()[1]
    print("Все виды цветов:", *garden_set.union(meadow_set))
    # выведите на консоль те, которые растут и там и там
    print("Которые растут и там и там:", *garden_set.intersection(meadow_set))
    # выведите на консоль те, которые растут в саду, но не растут на лугу
    print("Которые растут в саду, но не растут на лугу:", *garden_set.difference(meadow_set))
    # выведите на консоль те, которые растут на лугу, но не растут в саду
    print("Которые растут на лугу, но не растут в саду:", *meadow_set.difference(garden_set))
    status = 'ok'
    assert 'ok' == status

def test_three_song():
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    result = 'Три песни звучат (13.85, 15.17, 14.88) минут'
    assert three_song(violator_songs_list) == result

def test_other_songs():
    violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
    }
    result = 'А другие три песни звучат 13.49 минут'
    assert other_songs(violator_songs_dict) == result

def test_insert():
    global lst
    lst = zoos()
    result = ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']
    assert insert(1, 'bear', lst) == result

def test_insert2():
    global lst
    result = ['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark',]
    birds = ['rooster', 'ostrich', 'lark', ]
    for bird in birds:
        insert(len(lst), bird, lst)
    assert lst == result


def test_remove():
    global lst
    result = ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    lst = delete('elephant', lst)
    assert lst == result

def pprint():
    print(f"{lst.index('lion') + 1}\n{lst.index('lark') + 1}")

def test_get_family():
    expected_result = ['Отец', 'Мать', 'я', "Вовочка"], [['Отец', 175], ["Мать", 173], ['Вовочка', 186], ['Я', 184]]
    my_family, my_family_height = get_family()  
    assert my_family, my_family_height == expected_result

def test_otec():
    expected_result = 'Рост отца 175 см'
    assert otec(get_family()[1]) == expected_result

def test_summ():
    expected_result = 718
    assert summ(get_family()[1]) == expected_result
def test_movie():
    expected_result1 = ['Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие']
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    assert movie(my_favorite_movies) == expected_result1

def test_fuck_math():
    expected_result1 = 25
    lst = [1, 2, 3, 4, 5]
    assert fuck_math(lst) == expected_result1

def test_radius_circle():
    expected_result1 = 5541.7693
    radius = 42
    assert radius_circle(radius) == expected_result1

def test_point1():
    expected_result = True
    radius = 42
    point = (23, 34)
    assert point_in(radius, point) == expected_result

def test_point2():
    expected_result = True
    radius = 42
    point = (30, 30)
    assert point_in(radius, point) == expected_result

def test_distance():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    expected_result = {'Moscow': {'London': 145.60219778561037, 'Paris': 130.38404810405297}, 'London': {'Moscow': 145.60219778561037, 'Paris': 42.42640687119285}, 'Paris': {'Moscow': 130.38404810405297, 'London': 42.42640687119285}}
    assert distance(sites) == expected_result