import re
from exModule import runNetworkCode

#Part I ----------------------------------------------------
def checkNetwork(**kwargs):
    try:
        runNetworkCode(**kwargs)
    except ConnectionError as e:
        raise
    except OSError as e:
        return "An issue encountered during runtime. The name of the error is: "+ type(e).__name__
    except:
        return False
    return True

#Part II --------------------------------------------------------
def isOK(signalName):
    nameMatch = re.search(r"^[A-Z]{3}\-[0-9]{3}$" ,signalName)
    if(nameMatch):
        return True
    else:
        return False

def loadDataFrom(signalName, folderName):
    if(not isOK(signalName)):
        raise ValueError('{} is invalid'.format(signalName))
    path = folderName+ '/'+signalName+'.txt'
    try:
        with open(path,'r') as myFile:
            read = myFile.readlines()
    except:
        raise OSError("{} is not present in the {}.".format(signalName,folderName))
    numList = []
    nonFloatCount = 0
    for num in read:
        try:
            numList.append(float(num))
        except:
            nonFloatCount+=1
    return (numList, nonFloatCount)

def isBounded(signalValues, bonds, threshold):
    if(len(signalValues) ==0 ):
        raise ValueError("Signal contains no data.")
    lowBond  = min(bonds)
    highBond = max(bonds)
    highList = []
    lowList = []
    for signal in signalValues:
        if(signal > 0):
            highList.append(signal)
        elif(signal < 0):
            lowList.append(signal)
    higher = 0
    for signal in highList:
        if(float(signal) > float(highBond)):
            higher+=1
    lower = 0
    for signal in lowList:
        if signal < lowBond:
            lower+=1
    if(lower+higher) <= threshold:
        return True
    else:
        return False

def main():
    singal, nfc = loadDataFrom("AFW-481","Signals")
    bounds = (-15.00, 20.11)
    threshold = 5
    #print(isBounded(singal, bounds, threshold))
    checkNetwork()
    return checkNetwork()

if __name__ == "__main__":

   # print(checkNetwork())
    #print(isOK("XZC-012"))
   #print(loadDataForm("AFW-481","Signals"))

    print(main())
   #main()