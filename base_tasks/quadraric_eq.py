
def f_num(n) :
    if n == 1 : # для единички
        return 1
    elif n <= 0 : # для отрицательных и нуля
        return 0
    elif n > 1 : # для нормальных
        return f_num(n - 1) + f_num(n - 2)

a = int(input('какое число требуется? '))
print(f_num(a))


def num(n) :
    num1 = 1
    num2 = 1
    for i in range(1, (n - 1)) :
        if i % 2 == 0 :
            num1 = num1 + num2
        else :
            num2 = num1 + num2
    if num2 > num1 :
        print(num2)
    else :
        print(num1)

N = int(input())
num(N)