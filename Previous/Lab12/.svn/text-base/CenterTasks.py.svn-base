def getDetails():
    output = {}
    with open("community.txt",'r') as f:
        next(f)
        coursenames = f.readline()
        courseList = coursenames.split()
        courseList = courseList[2:]
        next(f)
        for line in f:
            lineList = line.split('|')
            personalist = lineList[1:]
            name = lineList[0]
            name = name.strip()
            if (name not in output):
                l = []
                output[name]=l
            i = 0
            for i in range(len(courseList)):
                grade = personalist[i]
                grade = grade.strip()
                if grade != '-':
                    value2 = output[name]
                    value2.append((courseList[i], float(grade)))
                    output[name] = value2
    return output

def getPerformance():
    output = {}
    dict =getDetails()

    for name, value in dict.items():
        for cla in value:
            course,grade = cla
            if course not in output:
                output[course] = []
            nameAndGrade = (name,grade)
            value2 = output[course]
            value2.append(nameAndGrade)
            output[course]=value2
    for key, value in output.items():
        value3 = output[key]
        value3 = sorted(value3)
        output[key] = value3

    return output

def getHighest(course):
    dict = getPerformance()
    maxScore = 0
    maxName = ''
    i = 0
    while(i<len(dict[course])):
        name = dict[course][i][0]
        grade = dict[course][i][1]
        if grade > maxScore:
            maxScore = grade
            maxName = name
        i+=1
    return (maxName,maxScore)

def getMean(course):
    dict = getPerformance()
    i = 0
    sum = 0
    total = 0
    while(i<len(dict[course])):
        sum+=dict[course][i][1]
        total+=1
        i+=1
    average = round(float(sum/total),2)

    return average


def getCumulativeScore(name):
    dict = getDetails()[name]
    sum = 0.0
    numOfClasses = 0
    hourDict = {}
    with open('hours.txt','r')as myFile:
        next(myFile)
        next(myFile)
        for line in myFile:
            course = line.split()[0]
            hour = line.split()[1]
            course = course.strip()
            hour = hour.strip()
            hourDict[course] = int(hour)

    for cla in dict:
        courseName = cla[0]
        grade = cla[1]
        numOfClasses += hourDict[courseName]
        sum+= grade*hourDict[courseName]


    cumulative =  round(float(sum/numOfClasses),2)
    return cumulative


if __name__ == "__main__":
    a = getPerformance()
    print(getCumulativeScore("Floria Uribe"))
