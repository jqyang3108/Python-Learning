import module_tasks

def load_multiple(signal_names, folder_name, max_count):
    dict = {}
    for signalName in signal_names:
        try:
            singal, nfc = module_tasks.loadDataFrom(signalName, folder_name)
        except:
            dict[signalName] = None
            continue
        if nfc <= max_count:
            dict[signalName] = singal
        else:
            dict[signalName] = []
    return dict

def save_data(signals_dictionary, target_folder, bounds, threshold):
    for singal in signals_dictionary:
        path = target_folder + '/' + singal + '.txt'

        try:
            if(module_tasks.isBounded(signals_dictionary[singal],bounds, threshold)):
                with open(path, "w") as myFile:
                    for lines in range(len(signals_dictionary[singal])):                  #write new file
                        myFile.write("{0:.3f}".format(signals_dictionary[singal][lines]))
                        if not lines == (len(signals_dictionary[singal]) - 1): #start new line
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
    a = load_multiple(signalNames, folderName, maxCount)
    b = save_data(a,targerFolder,bounds,threshold)

    return b

if __name__ == "__main__":

    print(main())


    ###
        name = re.search(r"([a-zA-Z]+)\.([a-zA-Z0-9]+)",filename)
    extension=name.group(2)
    if extension == 'jpg' or extension == 'png':
        identify = subprocess.check_output(['identify',filename],stderr=subprocess.STDOUT)
        ma = re.search(r"([0-9]+)x([0-9]+)",str(identify))
        return Image(name.group(0),ma.group(1),ma.group(2))
    elif extension == 'avi' or extension == 'mp4':
        identify = subprocess.check_output(['ffprobe','-i',filename],stderr=subprocess.STDOUT)
        ma = re.search(r" ([0-9]+)x([0-9]+) ",str(identify))
        du = re.search(r"Duration: ([0-9]+)\:([0-9]+)\:([0-9]+)\.([0-9]+)",str(identify))
        return Video(name.group(0),int(ma.group(1)),int(ma.group(2)),int(du.group(3)))
    else:
        return None

    ###