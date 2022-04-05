from signalprob import spNOT, spnAND, spnOR, spnNOR, spnNAND, spnXOR, spnXNOR

global SignalsTable
global ElementsTable
global ElementTypes
global TopInputs
global x
global sum
global Names
global HelpArray
global summm
global Signalsfor4
global testarray
global testarray2

testarray2 = []
testarray = []
SignalsTable = []
ElementsTable = []
Names = []
HelpArray = []
Signalsfor4 = []
ElementTypes = ['NOT', 'AND', 'OR', 'XOR', 'NAND', 'NOR', 'XNOR']
TopInputs = []
sum = 0
summm = 0


class Element:
    def __init__(self, type, inputs, output):
        self.type = type
        self.inputs = inputs
        self.output = output


def spNOT2(input1sp):
    first = float(input1sp)
    s = 1 - first
    sw = 2 * s * (1 - s)
    return s, sw


def sp2AND2(input1sp):
    # print("AND Gate for input probabilities (", input1sp, ',', input2sp, ') :\n')
    first = float(input1sp[0])
    second = float(input1sp[1])
    s = first * second
    # print('ans = ', s)
    sw = 2 * s * (1 - s)
    # print('Switching activity = ', sw, '\n')
    return s, sw


def process(element):
    global sum
    global x
    global SignalsTable
    global testarray
    global testarray2
    if sum == 1:
        kappa = int(x)+1
    elif sum == 2:
        kappa = int(x)+2
    else:
        kappa = int(x)
    signalarray = []
    if element.type != 'NOT':
        for i in element.inputs:
            #print(SignalsTable)
            signalarray.append(SignalsTable[i])
    if element.type == 'AND':
        #print(kappa)
        #print(SignalsTable[kappa])
        #print(signalarray)
        SignalsTable[kappa] = spnAND(signalarray)
        #print(SignalsTable[kappa])
        return
    elif element.type == 'ANDtest':
        #print(signalarray)
        SignalsTable[kappa], d = sp2AND2(signalarray)
        testarray.append(d)
    elif element.type == 'NOTtest':
        SignalsTable[kappa], de = spNOT2(SignalsTable[element.inputs[0]])
        testarray.append(de)
    elif element.type == 'ANDtest2':
        #print(signalarray)
        SignalsTable[kappa], d = sp2AND2(signalarray)
        testarray2.append(SignalsTable[kappa])
        testarray2.append(d)
    elif element.type == 'NOTtest2':
        SignalsTable[kappa], de = spNOT2(SignalsTable[element.inputs[0]])
        testarray2.append(SignalsTable[kappa])
        testarray2.append(de)
    elif element.type == 'OR':
        SignalsTable[kappa] = spnOR(signalarray)
        return
    elif element.type == 'XAND':
        SignalsTable[kappa] = spnXOR(signalarray)
        return
    elif element.type == 'NAND':
        SignalsTable[kappa] = spnNAND(signalarray)
        return
    elif element.type == 'NOR':
        SignalsTable[kappa] = spnNOR(signalarray)
        return
    elif element.type == 'XNOR':
        SignalsTable[kappa] = spnXNOR(signalarray)
        return
    elif element.type == 'XOR':
        SignalsTable[kappa] = spnXOR(signalarray)
        return
    elif element.type == 'NOT':
        SignalsTable[kappa] = spNOT(SignalsTable[element.inputs[0]])
        #print('not', SignalsTable[kappa])
        #print(kappa)
        return
    return


def process2(element):
    global sum
    global x
    global SignalsTable
    global Names
    global HelpArray
    global summm
    global Signalsfor4
    new = 0
    signalarray = []
    Names.append(element.output)
    #print(Names)
    HelpArray.append(summm)
    if element.type != 'NOT':
        for i in element.inputs:
            #print(SignalsTable)
            if i not in Names:
                if float(i) >= 0 and float(i) <= 1:
                    signalarray.append(i)
            else:
                for y in range(0, len(Names)):
                    if i == Names[y]:
                        new = HelpArray[y]
                signalarray.append(SignalsTable[x+new])
    if element.type == 'AND':
        #print(kappa)
        #print(SignalsTable[kappa])
        #print(signalarray)
        #print('summm',summm)
        #print(SignalsTable)
        SignalsTable[x+summm] = spnAND(signalarray)
        Signalsfor4.append(SignalsTable[x+summm])
        #print(SignalsTable[kappa])
    elif element.type == 'OR':
        SignalsTable[x+summm] = spnOR(signalarray)
        Signalsfor4.append(SignalsTable[x + summm])
    elif element.type == 'XAND':
        SignalsTable[x+summm] = spnXOR(signalarray)
        Signalsfor4.append(SignalsTable[x + summm])
    elif element.type == 'NAND':
        SignalsTable[x+summm] = spnNAND(signalarray)
        Signalsfor4.append(SignalsTable[x + summm])
    elif element.type == 'NOR':
        SignalsTable[x+summm] = spnNOR(signalarray)
        Signalsfor4.append(SignalsTable[x + summm])
    elif element.type == 'XOR':
        SignalsTable[x + summm] = spnXOR(signalarray)
        Signalsfor4.append(SignalsTable[x + summm])
    elif element.type == 'XNOR':
        SignalsTable[x + summm] = spnXNOR(signalarray)
        Signalsfor4.append(SignalsTable[x + summm])
    elif element.type == 'NOT':
        SignalsTable[x+summm] = spNOT(SignalsTable[element.inputs[0]])
        Signalsfor4.append(SignalsTable[x + summm])
        #print('not', SignalsTable[kappa])
        #print(kappa)
    summm = summm + 1
    return


def GiveTopInputs():
    global x
    x = input('Please insert the number of the top inputs: ')
    print()
    k = 0
    for i in range(0, int(x)+3):
        SignalsTable.append(0)
    for i in range(1, int(x)+1):
        a = input("Please insert signal probability:")
        TopInputs.append(k)
        SignalsTable[TopInputs[i-1]] = a
        k = k+1
    print()
    return


def ask1():
    global x
    global sum
    array = []
    GiveTopInputs()
    for i in range(1, int(x)):
        array.append(i-1)
    E1 = Element('AND', array, int(x)+1)
    E2 = Element('NOT', [int(x)-1], int(x)+2)
    E3 = Element('AND', [int(x)+1, int(x)+2], int(x))
    ElementsTable.append(E1)
    ElementsTable.append(E2)
    ElementsTable.append(E3)
    for i in ElementsTable:
        sum = sum + 1
        process(i)
    return


def ask11(commandsarr, topinp):
    global x
    global SignalsTable
    global sum
    x = topinp
    z = -1
    sum = 0
    flag = 0
    bool = False
    for i in range(0, int(topinp)+len(commandsarr)):
        SignalsTable.append(0)
    #print(SignalsTable)
    for i in commandsarr:
        if i[0] == 'TLPINPUTS':
            continue
        #flag = flag + 1
        table = []
        for y in range(2, len(i)):
            table.append(i[y])
        E = Element(i[0], table, i[1])
        ElementsTable.append(E)
        sum = sum + 1
        process2(E)
    return


def ask114(commandsarr, topinp):
    #print('mphka')
    print(commandsarr)
    global Signalsfor4
    global x
    global SignalsTable
    global sum
    global Names
    global HelpArray
    x = topinp
    z = -1
    sum = 0
    flag = 0
    bool = False
    for i in range(0, int(topinp)+len(commandsarr)-1):
        SignalsTable.append(0)
    #print(SignalsTable)
    for i in commandsarr:
        if i[0] == 'TLPINPUTS':
            continue
        #flag = flag + 1
        table = []
        for y in range(2, len(i)):
            table.append(i[y])
        #print(table)
        E = Element(i[0], table, i[1])
        ElementsTable.append(E)
        sum = sum + 1
        process2(E)
    #print(Signalsfor4)
    #print(len(Signalsfor4))
    return Signalsfor4


def testbench():
    # TEST FOR
    # AND e a b = AND e 0 1 = 0
    # NOT f c = NOT f 0 = 1
    # AND d e f = AND d 0 1 = 0
    global SignalsTable
    global sum
    global x
    x = 3
    array = []
    for i in range(0, 3+3):
        SignalsTable.append(0)
    #SignalsTable
    for i in range(1, 3):
        array.append(i-1)
    E1 = Element('AND', array, 3+1)
    E2 = Element('NOT', [3-1], 3+2)
    E3 = Element('AND', [3+1, 3+2], 3)
    ElementsTable.append(E1)
    ElementsTable.append(E2)
    ElementsTable.append(E3)
    for i in ElementsTable:
        sum = sum + 1
        process(i)
    #print(SignalsTable)
    if SignalsTable[6-2] == 0 and SignalsTable[6-1] == 1 and SignalsTable[6-3] == 0: # the last one is the d , the output
        print('Testbench run SUCCESFULLY!')
    else:
        print("ERROR 404")
    return


def testbench222():
    global testarray
    global SignalsTable
    global sum
    global x
    x = 3
    array = []
    SignalsTable.append(0.50)
    SignalsTable.append(0.40)
    SignalsTable.append(0.30)
    for i in range(0, 3):
        SignalsTable.append(0)
    for i in range(1, 3):
        array.append(i-1)
    E1 = Element('ANDtest', array, 3+1)
    E2 = Element('NOTtest', [3-1], 3+2)
    E3 = Element('ANDtest', [3+1, 3+2], 3)
    ElementsTable.append(E1)
    ElementsTable.append(E2)
    ElementsTable.append(E3)
    for i in ElementsTable:
        sum = sum + 1
        process(i)
    #print(SignalsTable)
    sumaaaa = testarray[0] + testarray[1] + testarray[2]
    return sumaaaa/3


def testbench333():
    global testarray
    global SignalsTable
    global sum
    global x
    global testarray2
    x = 3
    array = []
    SignalsTable.append(0.3300)
    SignalsTable.append(0.3300)
    SignalsTable.append(0.3300)
    for i in range(0, 3):
        SignalsTable.append(0)
    for i in range(1, 3):
        array.append(i-1)
    E1 = Element('ANDtest2', array, 3+1)
    E2 = Element('NOTtest2', [3-1], 3+2)
    E3 = Element('ANDtest2', [3+1, 3+2], 3)
    ElementsTable.append(E1)
    ElementsTable.append(E2)
    ElementsTable.append(E3)
    for i in ElementsTable:
        sum = sum + 1
        process(i)
    #print(SignalsTable)
    return testarray2


zedd = input('Type 1 for run ask3_1')
if zedd == '1':
    #testbench()
    ask1()