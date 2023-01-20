"""
Метод bananas, который принимает на вход строку и возвращает
все возможные вариации слов «banana» в строке.
(- используется для обозначения зачеркнутой буквы)
"""
from itertools import combinations


def bananas(s):
    if s == 'banana':
        return {'banana'}
    result = set()
    for i in combinations(range(len(s)), len(s) - 6):
        m = list(s)
        for j in map(int, i):
            m[j] = '-'
        if [k for k in m if k != '-'] == list('banana'):
            result.add(''.join(m))
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {
    "ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"
}
assert bananas("bbananana") == {
    "b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
    "-ban--ana", "b-anana--"
}
