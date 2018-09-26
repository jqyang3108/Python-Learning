



def getStudentInfo():
    d = {}

    with open("university.txt",'r') as f:
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


            if (name not in d):
                l = []
                d[name]=l

            for i in range(len(courseList)):
                grade = personalist[i]
                grade = grade.strip()
                if grade != '-':
                    testtuple = (courseList[i], float(grade))
                    value2 = d[name]
                    value2.append(testtuple)
                    d[name] = value2
    return d
def getClassInfo():
    x = {}
    d =getStudentInfo()

    for k, value in d.items():
        for cla in value:
            course,grade = cla

            if course not in x:
                l = []
                x[course] = l
            testtuple = (k,grade)
            value2 = x[course]
            value2.append(testtuple)
            x[course]=value2
    for k, value in x.items():
        value3 = x[k]
        value3 = sorted(value3)
        x[k] = value3

    return x

def getBestInCourse(course):
    y = getClassInfo()
    courseinfo = y[course]

    max1 = 0
    maxName = ''

    for value in courseinfo:
        name,grade = value
        if grade> max1:
            max1 = grade
            maxName = name
    return (maxName,max1)


def getCourseAverage(course):

    y = getClassInfo()
    courseinfo = y[course]

    sum = 0.0
    count = 0.0
    for value in courseinfo:
        name,grade = value
        sum += grade
        count +=1.0
    average = float(sum/count)
    average = round(average,2)

    return average

def getStudentGPA(name):
    y = getStudentInfo()
    studentinfo = y[name]

    sum = 0.0
    num = 0
    l = []
    with open('course.txt','r')as f:
        next(f)
        next(f)
        for line in f:
            course,hour = line.split()
            course = course.strip()
            hour = hour.strip()
            l[course] = int(hour)

    for cla in studentinfo:
        courseName, grade = cla
        getHour = l[courseName]
        num += getHour
        temp1 = grade*getHour

        sum+=temp1
    gpa = float(sum/num)
    gpa = round(getHour,2)

    return gpa






def getCourseAverage(course):
    y = getClassInfo()


