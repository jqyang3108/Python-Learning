#! /usr/bin/env python3.4


#------------------------------------------------------------------------Problem 1
def find(pattern):
    #read file
    with open('sequence.txt', 'r') as myFile:
        string = myFile.read()
    print(string)
    lenP = len(pattern)
    lenC = len(string)
    offset = lenC % lenP
    i = 0
    output = []
    for i in range(lenC):
        testString = string[i:i+lenP]                              #get part of the string to be tested
        c=0
        if (len(testString)==lenP):                                #length of pattern must == length of string

            for j in range(lenP):                                      #test pattern in each part of string
                if((testString[j] == pattern[j]) or (pattern[j] == "X")):  #+1 if each digit matches
                    c += 1
            if(c == lenP):                                              #c = length of pattern means every digit matches
                output.append(testString)
        else:
            break
    return output


#------------------------------------------------------------------------Problem 2
def getStreakProduct(sequence, maxSize, product):
    output = []
    lenS = len(sequence)
    testRange = maxSize + 1
    #for i in range(lenS):
    i=0
    while(i <= lenS):
        j=2
        while(j < testRange):
        #for j in range(2,maxSize+1):
            testString = sequence[i:i+j]
            testProduct = 1
            k=0
            for k in testString:
                testProduct = testProduct * int(k)

            if(testProduct == product):
                output.append(testString)
                break
            j+=1
        i+=1
    return output


#------------------------------------------------------------------------Problem 3
def writePyramids(filePath, baseSize, count, char):
    open(filePath,"w").close()
    middleSpace = count-1
    tip = 1
    level = (baseSize + 1) / 2
    while(level > 0):
        #process current level -----------------------------------
        space = level
        middleSpace = count-1
        countRem = count
        while(countRem > 0):
            #left--------------------------------
            i = 1
            while(i < space):
                with open(filePath,"a") as myfile:
                    myfile.write(" ")
                i+= 1
            #middle---------------------------------------------
            j=1
            tip = baseSize - 2*(space-1)
            while(j <= tip):
                with open(filePath,"a") as myfile:
                    myfile.write(char)
                j+=1
            #right----------------------------------------------------
            k=1
            while(k < space):
                with open(filePath,"a") as myfile:
                    myfile.write(" ")
                k+=1
            #sperator---------------------------------------------
            if(middleSpace > 0):
                with open(filePath,"a") as myfile:
                    myfile.write(" ")
            middleSpace -= 1
            countRem-=1
        #next level-------------------------------------------------
        level -=1
        with open(filePath, "a") as myfile:
            myfile.write("\n")
    return

#------------------------------------------------------------------------Problem 4
def getStreaks(sequence, letters):
    lenS = len(sequence)
    lenL = len(letters)
    i = 0
    k = 0
    output = []
    while(i < lenS):
        for j in range(lenL):
            if(i >= lenS):
                break
            if(sequence[i] == letters[j]):
                k = i
                while(sequence[i] == sequence[k]):
                    k += 1
                    if( k >= lenS):
                        break
                testString = sequence[i:k]
                output.append(testString)
                i = k-1
                k = 0
        i+=1
    return output

#------------------------------------------------------------------------Problem 5
def findNames(nameList, part, name):
    i = 0
    lenN = len(nameList)
    firstName = []
    lastName = []
    output = []
    while(i < lenN):
        list = nameList[i].split()
        firstName.append(list[0])
        lastName.append(list[1])
        i +=1

    for j in range(lenN):
        if( part == "L"):
            if(lastName[j].lower()==name.lower() ):
                output.append(nameList[j])
        elif(part == "F"):
            if(firstName[j].lower() == name.lower()):
                output.append(nameList[j])
        elif(part == "FL"):
            if(firstName[j].lower() == name.lower()):
                output.append(nameList[j])
            if(lastName   [j].lower() == name.lower()):
                output.append(nameList[j])
    return output

#------------------------------------------------------------------------Problem 6
def convertToBoolean(num, size):
    output = []
    if(type(num) != int or type(size) != int):
        return output
    else:
        num2 = bin(num)
        num2 = num2[2:]
        lenB = len(num2)
        if(lenB > size):
            for i in range(lenB):
                if(num2[i]=="1"):
                    output.append("True")
                else:
                    output.append("False")
        elif(lenB == size):
            for i in range(lenB):
                if (num2[i] == "1"):
                    output.append("True")
                else:
                    output.append("False")
        else:
            j = 0
            while(j < size - lenB):
                output.append("False")
                j += 1
            for i in range(lenB):
                if (num2[i] == "1"):
                    output.append("True")
                else:
                    output.append("False")
    return output


#------------------------------------------------------------------------Problem 7
def convertToInteger(bList):
    if(type(bList) != list):
        return
    elif(len(bList) == 0):
        return
    else:
        output = 0
        lenB = len(bList)
        i=lenB-1
        j=0
        k=0
        while(i >= 0):
            if(type(bList[i]) != bool):
                return
            if(bList[i] == True):
                j=0
                power2=1
                if (k == 0):
                    power2 = 1                        #2^0
                while(j < k):                        #2^j
                    power2 = power2 * 2
                    j+=1
                output = output + power2
            k+=1
            i-=1

    return output



if __name__ == "__main__":
    pattern = "X5969XX"
    bList=[True,False,False, False, False, True, True, True]
    bList2 =[False, False,True,False,False,True]
    bList3 =[True, 1,0,22]
    sequence = "AAASSSSSAPPPSSPPBBCCCSSS"
    sequence2 = "314X9X"
    names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    result = find(pattern)
    #result = getStreakProduct(sequence2, 3, 32)
    #result = writePyramids("pyramid12.txt", 15,5,"*")
    #result =convertToInteger(bList3)
    #result =convertToBoolean(3,4)
    #result=findNames(names,"FL", "asd")
    #result=getStreaks(sequence, "T")
    print(result)



