import pytest


def fib(n):
    """Вычисление чисел фибоначи"""
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def quick_sort(A):
    """Быстрая сортировка массива"""
    if len(A) <= 1:
        return A
    else:
        q = A[0]
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return quick_sort(L) + M + quick_sort(R)


def binary_search(N, arr):
    """Бинарный поиск элемента в массиве"""
    left = -1;
    right = len(arr)
    while right > left + 1:
        mid = (left + right)//2
        if arr[mid] >= N:
            right = mid 
        else:
            left = mid 

    return right 


def sorted_dict(dict1):
    """Соритровка словаря по значениям"""
    sorted_values = sorted(dict1.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in dict1.keys():
            if dict1[k] == i:
                sorted_dict[k] = dict1[k]
                break
    return sorted_dict


def test_list():
    """Проверка правильности нахождения чисел фибоначи"""
    assert list(fib(5)) == [0, 1, 1, 2, 3]


def test_quick_sort():
    """Проверка правильности работы быстрой сортировки"""
    arr = [1, 3, -4, 0, 5]
    assert quick_sort(arr) == [-4, 0, 1, 3, 5]


def test_binary_search():
    """Проверка правильности работы бинарного поиска"""
    arr = [1, 3, -4, 0, 5]
    assert binary_search(3, quick_sort(arr)) == 3


@pytest.mark.parametrize('response,key', [({'name': 'Dmitrii', 'age': 21}, 'age'), ({'name': 'Egor', 'country': 'Russia'}, 'age')] )
def test_response(response, key):
    """Проверка нахождения ключа в словаре"""
    try:
        assert response[key] 
    except KeyError:
        pass


def test_delete_values():
    """Удаление ключа в словаре"""
    users = {1: {'first_name': 'Dmitrii',
                 'last_name':'Grekov'},
             2: {'first_name': 'Egor',
                 'last_name': 'Petrow'}}
    assert users.pop(2) == {'first_name': 'Egor', 'last_name': 'Petrow'}


def test_sorted_dict():
    """Проверка сортировки словаря по значениям"""
    users = {'Bob': 'Bob',
             'Michail': 'Michail',
             'Alice': 'Alice'}
    valid_users = {'Alice': 'Alice',
                   'Bob': 'Bob',
                   'Michail': 'Michail'}
    assert sorted_dict(users) == valid_users



