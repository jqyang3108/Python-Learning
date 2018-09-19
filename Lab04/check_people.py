import glob as gb
def identify_access():
    depList = gb.glob("Departments/*.txt")
    A={}
    tempList = []
    fileList = []
    for filename in depList:
        fileList.append(filename.split("/")[1])
    for filename in fileList:
        filepath = "Departments/" + filename
        with open(filepath, 'r', encoding="utf8") as myfile:
            name = myfile.readlines()
        output=[]
        for addname in name:
            output.append(addname.strip("\n"))
        nameList = output
        for name in nameList:
            if (name not in tempList):
                tempList.append(name)
            A.setdefault(name,[]).append(filename.split(".txt")[0])
    for sortName in A.keys():
        sortList = A[sortName]
        sortList.sort()
        A[sortName] = sortList
    return A

def get_common(name1, name2):
    dict = identify_access()
    if ((name1 not in dict.keys()) or (name2 not in dict.keys())):
        return None
    common=[]
    for search in dict.get(name1):
        if(search in dict.get(name2)):
            common.append(search)
    common = set(common)
    return common

if __name__ == "__main__":
    #result = readfile('ACC340.txt')
    result = identify_access()
    #result = get_common("Tamatha Granderson", "Tasha Shell")
    print(result)