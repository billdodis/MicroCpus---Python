def spNOT(input1sp):
    first = float(input1sp)
    s = 1 - first
    sw = 2 * s * (1 - s)
    return s, sw


def sp2AND(input1sp, input2sp):
    # print("AND Gate for input probabilities (", input1sp, ',', input2sp, ') :\n')
    first = float(input1sp)
    second = float(input2sp)
    s = first * second
    # print('ans = ', s)
    sw = 2 * s * (1 - s)
    # print('Switching activity = ', sw, '\n')
    return s, sw


text = input('Please insert the probabilities for a,b and c with commas (a,b,c)(e.g."0.15,0.44,0.88")\n')
x = text.split(",")
a = x[0]
b = x[1]
c = x[2]
e, esw = sp2AND(a, b)
print('Switching activity of e is: ', esw)
f, fsw = spNOT(c)
print('Switching activity of f is: ', fsw)
d, dsw = sp2AND(e, f)
print('Switching activity of d is: ', dsw)
