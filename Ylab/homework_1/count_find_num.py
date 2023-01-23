"""
Метод count_find_num, который принимает на вход список простых множителей
(primesL) и целое число, предел (limit), после чего генерирует
по порядку все числа. Меньшие значения предела, которые имеют все и только
простые множители простых чисел primesL.

primesL = [2, 5, 7]
limit = 500
count_find_num(primesL, limit) == [5, 490]
List of Numbers Under 500          Prime Factorization
___________________________________________________________
           70                         [2, 5, 7]
          140                         [2, 2, 5, 7]
          280                         [2, 2, 2, 5, 7]
          350                         [2, 5, 5, 7]
          490                         [2, 5, 7, 7]
"""
def count_find_num(primesL, limit):
    min_limit = 1
    for i in primesL:
        min_limit *= i
    if min_limit > limit:
        return list()
    lis_limit = [min_limit]
    for i in primesL:
        for j in list(set(lis_limit)):
            while True:
                j *= i
                if j <= limit:
                    lis_limit.append(j)
                    continue
                break
    return [len(lis_limit), max(lis_limit)]


primesL = [2, 5, 7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
