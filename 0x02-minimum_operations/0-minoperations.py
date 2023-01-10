#!/usr/bin/python3
""" module doc string """


def minOperations(n):
    """min ops"""
    if not n:
        return 0

    if n == 1:
        return 0

    all_max_divs = set()

    divisors = get_divisors(n)

    path = sorted(get_halves_recurs(divisors, all_max_divs))
    if path[-1] == 1:
        return 0

    return get_ops(path, n)


def get_divisors(n: int):
    """ returns divisors of n """
    lst = []
    half = n / 2
    x = 1  # if n % 2 else 2
    while x < half + 1:
        if n % x == 0:
            lst.append(x)
        x = x + 1

    return lst


def get_halves_recurs(lst, all_max_divs):
    """ recursively get the max divisors of each max divisor """
    max = lst[-1]
    all_max_divs.add(max)
    divisors = get_divisors(max)
    if max == 1:
        return all_max_divs
    return get_halves_recurs(divisors, all_max_divs)


def get_ops(lst, n):
    """ computes number of operatons needed"""
    lst.append(n)
    ln = len(lst)
    idx = 0
    res = 0

    # print(lst)
    while idx < ln - 1:
        res = res + (lst[idx + 1] / lst[idx])
        idx = idx + 1

    return int(res)


if __name__ == "__main__":
    print(minOperations(8))
    print(minOperations(17))
    print(minOperations(50))
    print(minOperations(9))
    print(minOperations(4))
    print(minOperations(12))
