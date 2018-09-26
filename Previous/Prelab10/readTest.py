import re
def loadDataFromFile(filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***


        *** This method is required for unit tests! ***
        """
        with open(filePath, "r") as myFile:
            list = myFile.readlines()[2:-2]
        i = 0
        nameList = []
        countList = []
        while(i < len(list)):
            if(i==0):
                read = re.search("\<StudentName graduate=\"(true|false)\"\>(.+?)\</StudentName\>$", list[i])
                gradChk = read.group(1)
                name = read.group(2)
            elif(i==1):
                read = re.search("\<StudentID\>(.+?)\</StudentID\>$", list[i])
                id = read.group(1)
            elif(i==2):
                read = re.search("\<College\>(.+?)\</College\>$", list[i])
                college = read.group(1)
            elif(i==3):
                i+=1
                continue
            elif(i>3):
                read = re.search("\<Component name=\"(.+?)\" count=\"(.+?)\" /\>", list[i])
                name = read.group(1)
                count = read.group(2)
                nameList.append(name)
                countList.append(count)
            else:
                i+=1
                continue

            i+=1
        return list
if __name__ == "__main__":
   result = loadDataFromFile("input.xml")
   print(result)
