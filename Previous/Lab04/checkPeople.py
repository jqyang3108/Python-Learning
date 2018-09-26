import glob as gb
def readFile(fileName):
    filePath = "Departments/" + fileName
    with open(filePath, "r") as myFile:
        name = myFile.readlines()
    i=0
    while(i<len(name)):
        name[i] = name[i].strip("\n")
        i+=1
    return name

def identifyAccess():
    A = {}
    fileList = gb.glob("Departments/*.txt")
    i = 0
    while(i<len(fileList)):
        fileList[i] = (fileList[i].split("/"))[1]
        i+=1

    list = []
    i=0
    while(i<len(fileList)):
        nameList = readFile(fileList[i])
        j = 0
        while(j<len(nameList)):
            if(nameList[j] not in list):
                list.append(nameList[j])
            A.setdefault(nameList[j],[]).append(fileList[i].split(".txt")[0])
            j+=1
        i+=1
    for sortName in A.keys():
        sortList = A[sortName]
        sortList.sort()
        A[sortName] = sortList
    return A

def getCommon(name1, name2):
    dict = identifyAccess()
    if((name1 not in dict.keys()) or (name2 not in dict.keys())):
        return None

    common = []
    listName1 = dict.get(name1)
    listName2 = dict.get(name2)

    for room in listName1:
        if (room in listName2):
            common.append(room)
    common = set(common)

    return common

result = len(readFile("ACC340.txt"))
#result = identifyAccess()
#result = getCommon("Merideth Kind", "Melba Gist")
print(result)