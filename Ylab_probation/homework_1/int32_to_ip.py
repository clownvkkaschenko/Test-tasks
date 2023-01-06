"""
Метод int32_to_ip, который принимает на вход 32-битное целое число (integer)
и возвращает строковое представление его в виде IPv4-адреса.
"""
def int32_to_ip(int32):
    o1 = int(int32 / 16777216) % 256
    o2 = int(int32 / 65536) % 256
    o3 = int(int32 / 256) % 256
    o4 = int(int32) % 256
    return f'{o1}.{o2}.{o3}.{o4}'


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
assert int32_to_ip(32) == "0.0.0.32"
