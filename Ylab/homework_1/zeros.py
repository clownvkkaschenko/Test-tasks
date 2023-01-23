"""
Метод zeros, который принимает на вход целое число (integer) и возвращает
количество конечных нулей в факториале заданного числа.
"""
def zeros(n):
    count = 0
    prime = 5
    while n / prime != 0:
        count += n / prime
        prime *= prime
    return int(count)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(12) == 2
assert zeros(30) == 7