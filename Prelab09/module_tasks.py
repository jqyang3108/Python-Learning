import re
from exModule import run_network_code

#Part I ----------------------------------------------------
def check_network(**kwargs):
    try:
        run_network_code(**kwargs)
    except ConnectionError as e:
        raise
    except OSError as e:
        return "An issue encountered during runtime. The name of the error is: "+ type(e).__name__
    except:
        return False
    return True

#Part II --------------------------------------------------------
def is_ok(signal_name):
    nameMatch = re.search(r"^[A-Z]{3}\-[0-9]{3}$" ,signal_name)
    if(nameMatch):
        return True
    else:
        return False

def load_data_from(signal_name, folder_name):
    if(not is_ok(signal_name)):
        raise ValueError('{} is invalid'.format(signal_name))
    path = folder_name+ '/'+signal_name+'.txt'
    try:
        with open(path,'r') as myFile:
            read = myFile.readlines()
    except:
        raise OSError("{} is not present in the {}.".format(signal_name,folder_name))
    numList = []
    nonFloatCount = 0
    for num in read:
        try:
            numList.append(float(num))
        except:
            nonFloatCount+=1
    return (numList, nonFloatCount)

def is_bounded(signal_values, bonds, threshold):
    if(len(signal_values) ==0 ):
        raise ValueError("Signal contains no data.")
    lowBond  = min(bonds)
    highBond = max(bonds)
    highList = []
    lowList = []
    for signal in signal_values:
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
    singal, nfc = load_data_from("AFW-481","Signals")
    bounds = (-15.00, 20.11)
    threshold = 5
    #print(isBounded(singal, bounds, threshold))
    check_network()
    return check_network()

if __name__ == "__main__":

   # print(checkNetwork())
    #print(isOK("XZC-012"))
   #print(loadDataForm("AFW-481","Signals"))

    print(main())
   #main()