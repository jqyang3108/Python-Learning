import os
import glob
#-----------------helper functions--------------------------------
def projectDict():
    with open('projects.txt', 'r') as myFile:
        line = myFile.readlines()[2:]
    i=0
    list =[]
    circuit=[]
    project=[]

    while(i<len(line)):
        line[i] = line[i].strip()
        circuit.append((line[i].split())[0])
        project.append((line[i].split())[1])
        i+=1
    A={}
    i=0
    while(i<len(line)):
        A.setdefault(project[i],[]).append(circuit[i])
        i+=1
    C={}
    i=0
    while(i<len(line)):
        C.setdefault(circuit[i],[]).append(project[i])
        i+=1
    B=["0","1","2","3"]
    B[0] = A
    B[1] = circuit
    B[2] = project
    B[3] = C
    return B

def studentsDict():
    with open('students.txt', 'r') as myFile:
        line = myFile.readlines()[2:]
    i=0
    list =[]
    name=[]
    id=[]
    while(i<len(line)):
        line[i] = line[i].strip()
        name.append((line[i].split("|"))[0].strip())
        id.append((line[i].split("|"))[1].strip())
        i+=1
    A={}
    i=0
    while(i<len(line)):
        A.setdefault(name[i],[]).append(id[i])
        i+=1
    C={}
    i=0
    while(i<len(line)):
        C.setdefault(id[i],[]).append(name[i])
        i+=1
    B=["0","1","2","4"]
    B[0] = A
    B[1] = name
    B[2] = id
    B[3] = C
    return B

def readCircuit(fileName):
    filePath = "Circuits/circuit_" + fileName + ".txt"
    with open(filePath, 'r') as myFile:
        id = myFile.readlines()[1:2]
        id = id[0].split(",")
        id[len(id)-1] = id[len(id)-1].strip("\n")
    i=0
    while(i<len(id)):
        id[i] = id[i].strip()
        i+=1

    with open(filePath, 'r') as myFile:
        component = myFile.readlines()[4:5]
        component = component[0].split(",")
    i=0
    while(i<len(component)):
        component[i] = component[i].strip()
        i+=1
    returnList = ['1',"2"]
    returnList[0] = id
    returnList[1] = component
    return returnList


#-----------------------------------------------------------------------------

#_________________________problem1________________________________

def getComponentCountByProject(projectID):
    project = projectDict()[0]
    if(projectID not in project):
        return None

    i = 0
    list = project.get(projectID)
    re=0
    l=0
    ca=0
    tr=0
    item = []
    while(i < len(list)):
        read = readCircuit(list[i])[1]      #
        j=0
        while(j<len(read)):
            if(read[j] not in item):
                item.append(read[j])
            j+=1
        i+=1
    i=0

    while(i<len(item)):
        if(item[i][0] == 'R'):
            re+=1
        elif(item[i][0] == 'L'):
            l+=1
        elif(item[i][0] == 'C'):
            ca+=1
        elif(item[i][0] == 'T'):
            tr+=1
        i+=1
    T = (re,l,ca,tr)
    return T

#_________________________problem2________________________________
def getComponentCountByStudent(studentName):
    students = studentsDict()[0]

    if(studentName not in students):
        return None
    else:
        re=0
        l=0
        ca=0
        tr=0

        circuitList = projectDict()[1]
        item = []

        i=0
        T=()
        while(i<len(circuitList)):
            if(students.get(studentName)[0] in readCircuit(circuitList[i])[0]):
                read = readCircuit(circuitList[i])[1]
                j=0
                while(j<len(read)):
                    if(read[j] not in item):
                        item.append(read[j])
                    j+=1


            i+=1
        i=0

        while(i<len(item)):
            if(item[i][0] == 'R'):
                re+=1
            elif(item[i][0] == 'L'):
                l+=1
            elif(item[i][0] == 'C'):
                ca+=1
            elif(item[i][0] == 'T'):
                tr+=1
            i+=1
        T = (re,l,ca,tr)
        if(T == (0,0,0,0)):
            T=()
            return T
        return T

#_________________________problem3________________________________
def getParticipationByStudent(studentName):
    students = studentsDict()[0]
    if(studentName not in students.keys()):
        return None
    else:
        project = projectDict()[0]
        circuitList = projectDict()[1]

        i=0
        par = []

        while(i<len(circuitList)):
            if(students[studentName][0] in readCircuit(circuitList[i])[0]):
                for project2 in project.keys():
                    if(circuitList[i] in project[project2]):
                        par.append(project2)
            i+=1
        par = set(par)
        if(len(par) == 0):
            return set()
        return par

#_________________________problem4________________________________
def getParticipationByProject(projectID):
    project = projectDict()[0]
    if(projectID not in project):
        return None
    else:
        restudents = studentsDict()[3]
        proj=[]
        for project2 in project.keys():
            if(project2 == projectID):
                list = project[project2]
                i=0
                while(i<len(list)):
                    #print(list[i])
                    parid = readCircuit(list[i])[0]
                    #print(list[i],parid)
                    j=0
                    while(j<len(parid)):
                        if(restudents[parid[j]] not in proj):
                            proj.append(restudents[parid[j]][0])
                        j+=1
                    i+=1
        proj=set(proj)
        return proj  #--------------------------?:set


#_________________________problem5________________________________
def getProjectByComponent(components):
    circuitList = projectDict()[1]
    projList = projectDict()[2]
    project = projectDict()[3]
    i= 0
    listOutput =[]
    components = list(components)
    while(i<len(components)):                                       #each component
        listUsed = []
        j=0
        while(j<len(circuitList)):
            if(components[i] in readCircuit(circuitList[j])[1]):   #component in circuit file
                #print("a")
                #print(project.get(circuitList[j]))

                k=0
                while(k<len(project.get(circuitList[j]))):
                    if(project.get(circuitList[j])[k] not in listUsed):
                        listUsed.append(project.get(circuitList[j])[k])

                    k+=1

            j+=1

        listOutput.append(listUsed)
        i+=1
    i=0
    A={}
    while(i<len(listOutput)):
        C = set(listOutput[i])
        B={components[i]: C}
        A.update(B)
        i+=1

    return A
#_________________________problem6________________________________
def getStudentByComponent(components):
    circuitList = projectDict()[1]
    students = studentsDict()[3]
    i= 0
    listOutput =[]
    components = list(components)
    while(i<len(components)):                                       #each component
        listUsed = []
        j=0
        while(j<len(circuitList)):
            if(components[i] in readCircuit(circuitList[j])[1]):   #component in circuit file
                k=0
                while(k<len(readCircuit(circuitList[j])[0])):
                    if((readCircuit(circuitList[j])[0])[k] not in listUsed):
                        listUsed.append((students.get((readCircuit(circuitList[j])[0])[k]))[0])
                    k+=1

            j+=1

        listOutput.append(listUsed)
        i+=1

    i=0
    A={}
    while(i<len(listOutput)):
        C = set(listOutput[i])
        B={components[i]: C}
        A.update(B)
        i+=1

    return A
#_________________________problem7________________________________
def getComponentByStudent(studentNames):
    circuitList = projectDict()[1]
    students = studentsDict()[0]
    studentNames = list(studentNames)
    i= 0
    listOutput =[]
    while(i<len(studentNames)):                                       #each component
        listUsed = []
        j=0
        while(j<len(circuitList)):
            #print(students.get(studentNames[i]),readCircuit(circuitList[j])[0])
            if(students.get(studentNames[i])[0] in readCircuit(circuitList[j])[0]):   #find name in circuit file
                k = 0
                while(k<len(readCircuit(circuitList[j])[1])):                         #update comp name
                    if((readCircuit(circuitList[j])[1])[k] not in listUsed):
                        listUsed.append((readCircuit(circuitList[j])[1])[k])
                    k+=1
            j+=1
        listOutput.append(listUsed)
        i+=1

    i=0
    A={}
    while(i<len(listOutput)):
        C = set(listOutput[i])
        B={studentNames[i]: C}
        A.update(B)
        i+=1

    return A
#_________________________problem8________________________________

def getCommonByProject(projectID1, projectID2):
    project = projectDict()[0]

    if ((projectID1 not in project) or (projectID2 not in project)):
        return None

    list1 =(project.get(projectID1))

    list2 =(project.get(projectID2))

    i=0

    listProj1=[]
    while(i<len(list1)):
        j=0
        eachList = readCircuit(list1[i])[1]
        while(j<len(eachList)):
            if(eachList[j] not in listProj1):
                listProj1.append(eachList[j])
            j+=1
        i+=1
    listProj1 = set(listProj1)

    i=0
    listProj2=[]
    while(i<len(list2)):
        j=0
        eachList = readCircuit(list2[i])[1]
        while(j<len(eachList)):
            if(eachList[j] not in listProj2):
                listProj2.append(eachList[j])
            j+=1
        i+=1
    listProj2 = set(listProj2)
    output = []
    for comp in listProj1:
        if comp in listProj2:
            output.append(comp)
    output.sort()
    if(len(output) ==0):
        return
    return output
#_________________________problem9________________________________
def getCommonByStudent(studentName1, studentName2):
    students = studentsDict()[0]

    if((studentName1 not in students) or (studentName2 not in students)):
        return None
    else:
        id1 = students.get(studentName1)
        id2 = students.get(studentName2)
        listStu1 = []
        listStu2 = []
        circuitList = projectDict()[1]
        i=0
        while(i<len(circuitList)):
            if(id1[0] in readCircuit(circuitList[i])[0]):
                j=0
                compList = readCircuit(circuitList[i])[1]
                while(j<len(compList)):
                    if(compList[j] not in listStu1):
                        listStu1.append(compList[j])
                    j+=1
            if(id2[0] in readCircuit(circuitList[i])[0]):
                j=0
                compList = readCircuit(circuitList[i])[1]
                while(j<len(compList)):
                    if(compList[j] not in listStu2):
                        listStu2.append(compList[j])
                    j+=1
            i+=1
    output=[]

    for comp in listStu1:
        if comp in listStu2:
            output.append(comp)
    if(len(output) ==0):
        return output
    output.sort()

    return output
#_________________________problem10________________________________
def getProjectByCircuit():
    circuitList = projectDict()[1]
    project = projectDict()[3]
    i=0
    output={}
    updated = []
    while(i<len(circuitList)):
        if(circuitList[i] not in updated):
            updated.append(circuitList[i])
            b = project.get(circuitList[i])
            b.sort()
            A = {circuitList[i]:b}
            output.update(A)
        i+=1
    return output
#_________________________problem11________________________________
def getCircuitByStudent():

    students = studentsDict()[3]
    circuitList = projectDict()[1]
    nameList = studentsDict()[1]
    i=0
    output={}
    while(i<len(circuitList)):
        parList = readCircuit(circuitList[i])[0]
        j=0
        while(j<len(parList)):

            if(circuitList[i] not in output.values()):
                output.setdefault(students.get(parList[j])[0],[]).append(circuitList[i])
            j+=1
        i+=1
    i=0
    for name in output.keys():
        output[name]=set(output[name])
        a=list(output[name])
        a.sort()
        output[name]=a
        i+=1
    for name2 in nameList:
        if(name2 not in output.keys()):
            output[name2]=[]

    return output
#_________________________problem12________________________________
def getCircuitByStudentPartial(studentName):

    output = []
    nameList = studentsDict()[1]
    i=0
    nameSplit= []
    fn=[]
    ln=[]
    while(i<len(nameList)):
        nameSplit = nameList[i].split(",")
        fn.append(nameSplit[0])
        ln.append(nameSplit[1].split()[0])
        i+=1
    if(studentName not in fn and studentName not in ln):
        return
    else:
        nameDic = getCircuitByStudent()
        output={}
        i=0
        while(i<len(nameList)):
            #print(studentName,fn[i],ln[i])
            if(studentName in fn[i] or studentName in ln[i]):
                a=(nameDic.get(nameList[i]))
                a.sort()
                #print(a)
                B = {nameList[i]:a}
                output.update(B)
            i+=1

    return output
if __name__ == "__main__":

    #result = projectDict()
    #result = readCircuit("54609")
    #result = studentsDict()

    #result = getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6") #1
    #result = getComponentCountByStudent("Sanders, Emily")                        #2
    #result = getParticipationByStudent("Sanders, Emily")                           #3
    #result = getParticipationByProject("90BE0D09-1438-414A-A38B-8309A49C02EF")       #4
    #result = getProjectByComponent({"T71.386", "C407.660","L760.824"})   #5

    result = getStudentByCompenent({"T71.386", "C407.660","L760.824"})  #6
    #result = getComponentByStudent({"Morgan, Edward", "White, Diana", "Sanders, Emily", "Wright, Eric"})  #7
    #result = getCommonByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "082D6241-40EE-432E-A635-65EA8AA374B6") #8
    #result = getCommonByStudent("Allen, Amanda","Adams, Keith")  #9
    #result = getProjectByCircuit()   #10

    #result = getCircuitByStudent()
    #result = getCircuitByStudentPartial("Rogers")
    print(result)