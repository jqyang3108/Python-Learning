import moduleTasks

def loadMultiple(signalNames, folderName, maxCount):
    dict = {}
    for signalName in signalNames:
        try:
            singal, nfc = moduleTasks.loadDataFrom(signalName, folderName)
        except:
            dict[signalName] = None
            continue
        if nfc <= maxCount:
            dict[signalName] = singal
        else:
            dict[signalName] = []
    return dict

def saveData(signalsDictionary, targerFolder, bounds, threshold):
    for singal in signalsDictionary:
        path = targerFolder + '/' + singal + '.txt'

        try:
            if(moduleTasks.isBounded(signalsDictionary[singal],bounds, threshold)):
                with open(path, "w") as myFile:
                    for lines in range(len(signalsDictionary[singal])):                  #write new file
                        myFile.write("{0:.3f}".format(signalsDictionary[singal][lines]))
                        if not lines == (len(signalsDictionary[singal]) - 1): #start new line
                            myFile.write("\n")
        except:
                pass

def main():
    signalNames = ["AKB-048","CIG-308","PKB-567"]
    folderName = "Signals"
    maxCount = 12
    targerFolder = "target"
    bounds = (-15.00, 20.11)
    threshold = 12
    a = loadMultiple(signalNames, folderName, maxCount)
    b = saveData(a,targerFolder,bounds,threshold)

    return b

if __name__ == "__main__":

    print(main())