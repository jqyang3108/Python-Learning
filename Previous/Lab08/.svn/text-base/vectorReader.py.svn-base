import simpleVector


def loadVectors(filename):
    output = []
    with open(filename, "r")as myFile:
        for line in myFile:
            try:
                a = simpleVector.Vector(line)
                output.append(a)
            except:
                output.append(None)
    return output

if __name__ == "__main__":

    print(loadVectors('values.txt'))
