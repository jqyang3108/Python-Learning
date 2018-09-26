

def getHorizontalMax():
    with open("square.txt",'r') as myFile:
        read = myFile.readlines()[:]
    i = 0
    while(i<len(read)):

        read[i] = read[i].strip('\n')
        read[i] = read[i].split(' ')
        i+=1
    #print(read)

    numRow = len(read)
    numCol = len(read[0])
    i = 0
    product = 0
    max = 0
    locali = 0
    localj = 0
    while(i<numRow):
        j = 0
        while(j<(numCol-3)):

            product = int(read[i][j])*int(read[i][j+1])*int(read[i][j+2])*int(read[i][j+3])
            #print(int(read[i][j]), int(read[i][j+1]),int(read[i][j+2]),int(read[i][j+3]), product)
            if(product > max):
                max = product
                locali = i
                localj = j
            j+=1
        i+=1
    listMax = [int(read[locali][localj]),int(read[locali][localj+1]),int(read[locali][localj+2]),int(read[locali][localj+3])]
    output = [max , listMax ]
    output = tuple(output)
    return output

def getVerticalMax():
    with open("square.txt",'r') as myFile:
        read = myFile.readlines()[:]
    i = 0
    while(i<len(read)):
        read[i] = read[i].strip('\n')
        read[i] = read[i].split(' ')
        i+=1


    numRow = len(read)
    numCol = len(read[0])
    j = 0
    product = 0
    max = 0
    locali = 0
    localj = 0

    while(j<numCol):
        i = 0
        while(i<(numRow-3)):
            product = int(read[i][j])*int(read[i+1][j])*int(read[i+2][j])*int(read[i+3][j])
            #print(int(read[i][j]), int(read[i+1][j]),int(read[i+2][j]),int(read[i+3][j]), product)
            if(product > max):
                max = product
                locali = i
                localj = j
            i+=1
        j+=1
    listMax = [int(read[locali][localj]),int(read[locali+1][localj]),int(read[locali+2][localj]),int(read[locali+3][localj])]
    output = [max , listMax ]
    output = tuple(output)

    return output

def buildDict(day):
    with open("codes.txt",'r') as myFile:
        index = myFile.readlines()[1:2]
    with open("codes.txt",'r') as myFile:
        read = myFile.readlines()[3:]
    i = 0
    name = []
    code = []
    while(i<len(read)):
        read[i] = read[i].strip('\n')
        read[i] = read[i].split()
        name.append(read[i][0]+' '+read[i][1])
        code.append(read[i][2:])
        i+=1
    #print(code)
    index[0]=index[0].strip('\n')
    dayList = index[0].split()
    dayList = dayList[2:]

    dayNum = 0
    dayFind = 0
    #print(dayList)
    while(dayNum < len(dayList)):
        if(day == dayList[dayNum]):
            dayFind = dayNum
            break
        dayNum+=1

    i = 0
    dict={}
    while(i<len(read)):
        dict.setdefault(name[i],[]).append(code[i][dayFind])
        i+=1
    i=0
    dict2={}
    while(i<len(read)):
        dict2.setdefault(code[i][dayFind],[]).append(name[i])
        i+=1
    dict3={}
    i=0
    while(i<len(read)):
        dict3.setdefault(name[i],[]).append(code[i])
        i+=1
    #print(dict)
    output = []
    output.append(dict) #0
    output.append(name) #1
    output.append(dayList) #2
    output.append(dayFind) #3
    output.append(code)   #4
    output.append(dict2) #5
    output.append(dict3) #6
    return output



def getCode(name, day):
    dict = buildDict(day)[0]
    nameList = buildDict(day)[1]
    dayList = buildDict(day)[2]
    if(name not in nameList or day not in dayList):
        return None

    output = dict.get(name)[0]


    return output

def getCodesOn(day):
    dict = buildDict(day)[0]
    dayList = buildDict(day)[2]
    dayFind = buildDict(day)[3]
    codeList = buildDict(day)[4]

    if(day not in dayList):
        output = set()
        return output
    i = 0
    outputList = []
    while(i<len(codeList)):
        outputList.append(codeList[i][dayFind])
        i+=1

    output = []
    for code in outputList:
        output.append(code)
    output = set(output)
    return output


def getUserOf(code):

    return

def getCommonCodes(name1, name2):
    dict = buildDict("aa")[6]
    #print(dict)
    nameList = buildDict("aa")[1]
    if(name1 not in nameList or name2 not in nameList):
        output = set()
        return output

    list1 = (dict.get(name1)[0])
    list2 = (dict.get(name2)[0])
    output = []
    for comp in list1:
        if comp in list2:
            output.append(comp)
    output = set(output)
    return output
result = getCommonCodes("Moore, John","Ross, Frances")
print(result)