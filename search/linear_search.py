"""
Функции линейного поиска в списке (массиве).

>>> linear_search([2, 10, 6, 8, 4], 5, 6)
2

>>> better_linear_search([2, 10, 6, 8, 4], 5, 6)
2
"""


def linear_search(a, n, x):
    """Возвращает позицию элемента x в n первых элементах списка a.
    Если элемент не найден, возвращает -1.

    >>> linear_search([2, 10, 6, 8, 4], 5, 6)
    2
    >>> linear_search([2, 10, 6, 8, 4], 5, 25)
    -1
    >>> linear_search([2, 10, 6, 8, 4, 25], 5, 25)
    -1
    """
    answer = -1
    for i in range(n):
        if a[i] == x:
            answer = i
    return answer


def better_linear_search(a, n, x):
    """Оптимизированная версия функции linear_search.

    Возвращает позицию элемента x в n первых элементах списка a.
    Если элемент не найден, возвращает -1.

    >>> better_linear_search([2, 10, 6, 8, 4], 5, 6)
    2
    >>> better_linear_search([2, 10, 6, 8, 4], 5, 25)
    -1
    >>> better_linear_search([2, 10, 6, 8, 4, 25], 5, 25)
    -1
    """
    for i in range(n):
        if a[i] == x:
            return i
    return -1


def sentinel_linear_search(a, n, x):
    """Оптимизированная версия функции better_linear_search.

    Возвращает позицию элемента x в n первых элементах списка a.
    Если элемент не найден, возвращает -1.

    >>> sentinel_linear_search([2, 10, 6, 8, 4], 5, 6)
    2
    >>> sentinel_linear_search([2, 10, 6, 8, 4], 5, 25)
    -1
    >>> sentinel_linear_search([2, 10, 6, 8, 4, 25], 5, 25)
    -1
    """
    last, a[n-1] = a[n-1], x

    i = 0
    while x != a[i]:
        i += 1
    a[n-1] = last

    if i < (n - 1) or a[n-1] == x:
        return i

    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
