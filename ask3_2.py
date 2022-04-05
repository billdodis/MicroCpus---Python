from ask3_1 import ask11, testbench222
from askisi2_1 import testbenchfor3_2
global TopInputs
global Commands
TopInputs = []
Commands = []


def bmethod(lines, first):
    for i in range(2, len(first)):
        TopInputs.append(first[i])
    second = lines[1].split()
    for i in range(2, len(second)):
        TopInputs.append(second[i])
    return


def ask2():
    with open('ask2.txt') as f:
        strlines = f.readlines()
    #lines = strlines.split()
    iftopinp = strlines[0].split()
    if iftopinp[0] != 'top_inputs':
        bmethod(strlines, iftopinp)
    else:
        for i in iftopinp:
            if i > 0:
                TopInputs.append(iftopinp[i])
    print('Top inputs : ')
    for i in TopInputs:
        print(i)
    for i in strlines:
        Command = []
        line = i.split()
        for y in range(0, len(line)):
            Command.append(line[y])
        Commands.append(Command)
    print('Please give input for the top inputs,')
    x = input('divided by commas(e.g 0.5,0.5,0.5)\n')
    xxx = x.split(",")
    #print(xxx)
    for y in range(0, len(Commands)):
        for z in range(0, len(Commands[y])):
            #print(Commands[y][z])
            for i in range(0, len(TopInputs)):
                if Commands[y][z] == TopInputs[i]:
                    Commands[y][z] = xxx[i]
    print(Commands)
    ask11(Commands, len(TopInputs))
    return


def testbench():
    # a = 0.50 , b = 0.40 , c = 0.30
    avg = testbenchfor3_2()
    avg2 = testbench222()
    if avg == avg2:
        print('Testbench run SECCESFULLY!')
    else:
        print('ERROR 404')
    return


zedd = input('For testbench press 2 ')
if zedd == '2':
    testbench()
else:
    ask2()