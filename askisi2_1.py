def spNOT(input1sp):
    first = float(input1sp)
    s = 1 - first
    sw = 2 * s * (1 - s)
    return s


def sp2AND(input1sp, input2sp):
    # print("AND Gate for input probabilities (", input1sp, ',', input2sp, ') :\n')
    first = float(input1sp)
    second = float(input2sp)
    s = first * second
    # print('ans = ', s)
    sw = 2 * s * (1 - s)
    # print('Switching activity = ', sw, '\n')
    return s


def spNOT2(input1sp):
    first = float(input1sp)
    s = 1 - first
    sw = 2 * s * (1 - s)
    return s, sw


def sp2AND2(input1sp, input2sp):
    # print("AND Gate for input probabilities (", input1sp, ',', input2sp, ') :\n')
    first = float(input1sp)
    second = float(input2sp)
    s = first * second
    # print('ans = ', s)
    sw = 2 * s * (1 - s)
    # print('Switching activity = ', sw, '\n')
    return s, sw


def testbenchfor3_2():
    e, esw = sp2AND2(0.50, 0.40)
    f, fsw = spNOT2(0.30)
    d, dsw = sp2AND2(e, f)
    summ = esw + fsw + dsw
    return summ/3


def testbenchfor3_3():
    e, esw = sp2AND2(0.3300, 0.3300)
    f, fsw = spNOT2(0.3300)
    d, dsw = sp2AND2(e, f)
    array = [e, esw, f, fsw, d, dsw]
    return array


def ask21():
    text = input('Please insert the probabilities for a,b and c with commas (a,b,c)(e.g."0.15,0.44,0.88")\n')
    x = text.split(",")
    a = x[0]
    b = x[1]
    c = x[2]
    e = sp2AND(a, b)
    f = spNOT(c)
    d = sp2AND(e, f)
    print('Probability of output(d) is: ', d)
    return


zedd = input('For testbench press 1 , for running 2_1 press anything else.\n')
if zedd != '1':
    ask21()