import math
from random import randint


def NOT(a):
    if a == 0:
        return 1
    return 0


def AND(a, b):
    s = a * b
    return s


def and1(A, B):
    output = []
    for i in range(len(A)):
        x = AND(A[i], B[i])
        output.append(x)
    return output


def not1(A):
    output = []
    for i in range(len(A)):
        x = NOT(A[i])
        output.append(x)
    return output


def MonteCarlo(N):
    a = []
    b = []
    c = []
    for i in range(N):
        a.append(randint(0, 1))
        b.append(randint(0, 1))
        c.append(randint(0, 1))
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    return a, b, c


def switchingact(D):
    switchesNumber = 0
    for k in range(len(D) - 1):
        if D[k] != D[k + 1]:
            switchesNumber += 1
    return switchesNumber / (len(D) - 1)


print()
a, b, c = MonteCarlo(10)
e = and1(a, b)
print('e = ', e)
f = not1(c)
print('f = ', f)
d = and1(e, f)
print('for N = 10 :\n d = ', d)
print('Switching Activity : ', switchingact(d), '\n')
a1, b1, c1 = MonteCarlo(100)
e1 = and1(a1, b1)
print('e = ', e1)
f1 = not1(c1)
print('f = ', f1)
d1 = and1(e1, f1)
print('for N = 100 :\n d = ', d1)
print('Switching Activity : ', switchingact(d1), '\n')
a2, b2, c2 = MonteCarlo(3300)
e2 = and1(a2, b2)
print('e = ', e2)
f2 = not1(c2)
print('f = ', f2)
d2 = and1(e2, f2)
print('for N = 3300 :\n d = ', d2)
print('Switching Activity : ', switchingact(d2), '\n')
