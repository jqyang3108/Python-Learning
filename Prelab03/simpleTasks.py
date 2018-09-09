#! /usr/bin/env python3.4

#Jiaqi Yang 09-07-2018

#------------------------------question1

def find(pattern):
  #  print("run find()")
    #read file
    with open('sequence.txt', 'r') as myFile:
        string = myFile.read()
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
                output.append(int(testString))
        else:
            break
    return output
#_________________________________question2

def getStreakProduct(sequence, maxSize, product):
   # print("run getStreakProduct()")
    output = []
    lenS = len(sequence)
    testRange = maxSize + 1
    i=0
    while(i <= lenS):
        j=2
        while(j < testRange):
            testString = sequence[i:i+j]
            testProduct = 1
            k=0
            for k in testString:
                testProduct = testProduct * int(k)
            if(testProduct == product):
                output.append(int(testString))
                break
            j+=1
        i+=1
    return output
#---------------------------------question3
def writePyramids(filePath,baseSize, count, char):
   # print("run writePyramids()")
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
#---------------------------------question4
def getStreaks(sequence, letters):
    #print("run getSteaks()")
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

#---------------------------question5
def findNames(nameList, part, name):
    #print("run findNames()")
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


#-------------------------------------question6
def convertToBoolean(num,size):
   # print("run convertToBoolean()")
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
                    output.append(True)
                else:
                    output.append(False)
        elif(lenB == size):
            for i in range(lenB):
                if (num2[i] == "1"):
                    output.append(True)
                else:
                    output.append(False)
        else:
            j = 0
            while(j < size - lenB):
                output.append(False)
                j += 1
            for i in range(lenB):
                if (num2[i] == "1"):
                    output.append(True)
                else:
                    output.append(False)
    return output

#---------------------------------question7
def convertToInteger(boolList):
    #print("run convertToInteger()")
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
    pattern = "154"
    sequence = "1547896154321687984"
    sequence2 = "14822"
    sequence4 ="AAASSSSSSAPPPSSPPBBCCCSSS"
    bList = [True, False, False, False, False, True, True, True]
    bList2 = [False, False, True, False, False, True]

    names=["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
#------------------------------

    result1 = find(pattern)
    print(result1,"\n")

    result2 = getStreakProduct(sequence, 3, 20)
    print(result2,"\n")

    result3 = writePyramids("pyramid12.out", 15, 5, "*")
    print(result3,"\n")

    result4 = getStreaks(sequence4, "SAQT")
    print(result4,"\n")

    result5 = findNames(names,"FL", "johnson")
    print(result5,"\n")

    result6 = convertToBoolean(9,3)
    print(result6, "\n")

    result7 = convertToInteger(bList2)
    print(result7)
