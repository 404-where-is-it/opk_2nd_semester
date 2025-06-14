from operator import truediv

import math

i = 1
begin = 0
range = 50

while (range > 1) :

    range = math.ceil(100 / (2 ** i))

    ans = input(f'ваше число больше {begin + range} ? ')

    if ans == 'д' :
        begin = begin + range

    i += 1

print(f'ответ {begin}')