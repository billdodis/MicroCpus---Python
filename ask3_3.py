from ask3_1 import ask11, ask114, testbench333
from askisi2_1 import testbenchfor3_3
global TopInputs
global Inputs
global Outputs
global Commands
global FinalCommands
global CalculatedOut


TopInputs = []
Inputs = []
Outputs = []
Commands = []  # lista apo listes, 1-1 tis grammes
FinalCommands = []
CalculatedOut = []


def fillarrays():
    with open('ask3.txt') as f:
        strlines = f.readlines()
    #lines = strlines.split()
    for i in strlines:
        Command = []
        line = i.split()
        if line[0] == 'top_inputs' or line[0] == 'TLPINPUTS':
            continue
        for y in range(0, len(line)):
            if y == 1:
                Outputs.append(line[y])
            if y >= 2:
                Inputs.append(line[y])
            Command.append(line[y])
        Commands.append(Command)
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


def printer():
    for i in FinalCommands:
        for y in i:
            print(y, ' ')
        print()
    return


def ask3():
    global Commands
    global CalculatedOut
    global FinalCommands
    fillarrays()
    for i in Inputs:
        if i not in Outputs:
            TopInputs.append(i)
    print('Top inputs : ')
    topinputs2 = sorted(set(TopInputs))
    for i in topinputs2:
        print(i+' ')
    taksinomisi()
    while len(Commands) != len(CalculatedOut) :
        #print(Commands)
        #print(CalculatedOut)
        taksinomisi2()
        CalculatedOut = sorted(set(CalculatedOut))
    #for z in Commands:
        #if z not in FinalCommands:
            #FinalCommands.append(z)
    print('Ta logika stoixeia taksinomhmena : \n')
    printer()
    print('Please give input for the ', len(topinputs2),'top inputs')
    x = input('divided by commas(e.g 0.5,0.5,0.5)\n')
    xxx = x.split(",")
    #for i in range(1, len(TopInputs)):
        #x = input('Signal Prob of ', TopInputs[i-1], 'is : ')
        #for y in FinalCommands:
            #for z in y:
                #if z == TopInputs[i-1]:
                    #z = x
    for y in range(0, len(FinalCommands)):
        for z in range(0, len(FinalCommands[y])):
            for i in range(0, len(topinputs2)):
                if FinalCommands[y][z] == topinputs2[i]:
                    FinalCommands[y][z] = xxx[i]
    print(FinalCommands)
    ask11(FinalCommands, len(topinputs2))
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


def testbench():
    arr = testbenchfor3_3()
    arr2 = testbench333()
    if arr == arr2:
        print('Testbench Run SUCCESFULLY!')
    else:
        print('ERROR 404')
    return


zedd = input('For testbench press 1')
if zedd == '1':
    testbench()
else:
    ask3()