import matplotlib.pyplot as plt
import math
from random import randint
import numpy as np
#from ask3_3 import ask34
from signalprob import spNOT, spnAND, spnOR, spnNOR, spnNAND, spnXOR, spnXNOR


global TopInputs
global Inputs
global Outputs
global Commands
global FinalCommands
global CalculatedOut
global SignalsTable
global ElementsTable
global ElementTypes
global x
global sum
global Names
global HelpArray
global summm
global Signalsfor4

SignalsTable = []
ElementsTable = []
Names = []
HelpArray = []
Signalsfor4 = []
ElementTypes = ['NOT', 'AND', 'OR', 'XOR', 'NAND', 'NOR', 'XNOR']
TopInputs = []
sum = 0
summm = 0


TopInputs = []
Inputs = []
Outputs = []
Commands = []  # lista apo listes, 1-1 tis grammes
FinalCommands = []
CalculatedOut = []


class Element:
    def __init__(self, type, inputs, output):
        self.type = type
        self.inputs = inputs
        self.output = output


def process2(element):
    global sum
    global x
    global SignalsTable
    global Names
    global HelpArray
    global summm
    global Signalsfor4
    signalarray = []
    Names.append(element.output)
    #print(Names)
    HelpArray.append(summm)
    if element.type != 'NOT':
        for i in element.inputs:
            #print(SignalsTable)
            if i == 0 or i == 1:
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


def fillarrays2():
    with open('ask4.txt') as f:
        strlines = f.readlines()
    #lines = strlines.split()
    for i in strlines:
        #print('aa')
        Command = []
        line = i.split()
        if line[0] == 'top_inputs' or line[0] == 'TLPINPUTS':
            for z in range(1, len(line)):
                TopInputs.append(line[z])
        for y in range(0, len(line)):
            if y == 1:
                Outputs.append(line[y])
            if y >= 2:
                Inputs.append(line[y])
            Command.append(line[y])
        Commands.append(Command)
    return


def ask34(Workload):
    #print("a")
    global Commands
    global CalculatedOut
    global FinalCommands
    fillarrays2()
    #for i in Inputs:
        #if i not in Outputs:
            #TopInputs.append(i)
    #print('Top inputs : ')
    #topinputs2 = sorted(set(TopInputs))
    #for i in topinputs2:
        #print(i+' ')
    taksinomisi()
    while len(Commands) != len(CalculatedOut) :
        #print(Commands)
        #print(CalculatedOut)
        taksinomisi2()
        CalculatedOut = sorted(set(CalculatedOut))
    #for z in Commands:
        #if z not in FinalCommands:
            #FinalCommands.append(z)
    #print('Ta logika stoixeia taksinomhmena : \n')
    #printer()
    #print('Please give input for the ', len(topinputs2),'top inputs')
    #x = input('divided by commas(e.g 0.5,0.5,0.5)\n')
    #xxx = x.split(",")
    #for i in range(1, len(TopInputs)):
        #x = input('Signal Prob of ', TopInputs[i-1], 'is : ')
        #for y in FinalCommands:
            #for z in y:
                #if z == TopInputs[i-1]:
                    #z = x
    for y in range(0, len(FinalCommands)):
        for z in range(0, len(FinalCommands[y])):
            for i in range(0, len(TopInputs)):
                if FinalCommands[y][z] == TopInputs[i]:
                    FinalCommands[y][z] = Workload[i]
    #print(FinalCommands)
    ask114(FinalCommands, len(TopInputs))
    return


def taksinomisi():
    global Commands
    global CalculatedOut
    global FinalCommands
    k = -1
    arr = []
    for i in Commands:
        k = k + 1
        flag = True
        for y in range(2, len(i)):
            if flag == False:
                continue
            if i[y] not in TopInputs:
                flag = False
        if flag == True:
            FinalCommands.append(i)
            CalculatedOut.append(i[1])
            arr.append(k)
            k = k - 1
    #for z in arr:
        #del Commands[z]

    return


def taksinomisi2():
    global Commands
    global CalculatedOut
    global FinalCommands
    k = -1
    arr = []
    for i in Commands:
        k = k + 1
        flag = True
        for y in range(2, len(i)):
            if flag == True:
                #print(i[y])
                #print(CalculatedOut)
                if i[y] not in CalculatedOut and i[y] not in TopInputs:
                    flag = False
        if flag == True:
            if i not in FinalCommands:
                FinalCommands.append(i)
            CalculatedOut.append(i[1])
            arr.append(k)

    #print('mphka')
    #if arr != []:
        #for z in arr:
            #del Commands[z]
    return


def generateWorkload(inputs):
    Workload = []
    for i in range(0, inputs):
        x = randint(0, 1)
        Workload.append(x)
    return Workload


def countSwitches(SignalsB, Signals):
    switches = 0
    for i in range(0, len(SignalsB)):
        if Signals[i] != SignalsB[i]:
            switches = switches + 1
    return switches


def ask114(commandsarr, topinp):
    #print('mphka')
    #print(commandsarr)
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
    return


def gui(array):
    guiarray = []
    for i in range(1,len(array)+1):
        guiarray.append(i)
    plt.plot(guiarray, array)
    plt.show()
    return


#def get_variance(arr, sum):
    #mean = sum / len(arr)
    #su = 0
    #for x in arr:
        #su += (x-mean)**2
    #return su/len(arr)


def ask41():
    global TopInputs
    global Inputs
    global Outputs
    global Commands
    global FinalCommands
    global CalculatedOut
    global SignalsTable
    global ElementsTable
    global ElementTypes
    global x
    global sum
    global Names
    global HelpArray
    global summm
    global Signalsfor4
    switcharray = []
    for i in range(0, 2000):
        print(i, 'Individual')
        TopInputs = []
        Inputs = []
        Outputs = []
        Commands = []
        FinalCommands = []
        CalculatedOut = []
        SignalsTable = []
        ElementsTable = []
        x = 0
        sum = 0
        Names = []
        HelpArray = []
        summm = 0
        Signalsfor4 = []
        workload = generateWorkload(20)
        #print(workload)
        ask34(workload)
        a = Signalsfor4
        workload2 = generateWorkload(20)
        TopInputs = []
        Inputs = []
        Outputs = []
        Commands = []
        FinalCommands = []
        CalculatedOut = []
        SignalsTable = []
        ElementsTable = []
        x = 0
        sum = 0
        Names = []
        HelpArray = []
        summm = 0
        Signalsfor4 = []
        ask34(workload2)
        b = Signalsfor4
        #print(a)
        #print(b)
        switches = countSwitches(a, b)
        switcharray.append(switches)
    summ = 0
    for i in switcharray:
        summ = i + summ
    avg = summ/len(switcharray)
    print('Mean is:', round(avg, 2))
    print('Variance is:', np.var(switcharray))
    gui(switcharray)
    return


ask41()