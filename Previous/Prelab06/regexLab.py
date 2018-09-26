import re

def extractValues(sentence):
    print(sentence)
    pattern = r"((\+|\-|)([\d])\.([\d]+)(e)([\+\-])([\d]+))|((\|+|\-|)([\d]+)(\.)([\d]+)(\,|\.| ))|([\+\-]?)[\d]+)"
    match = re.findall(pattern,sentence,re.I)
    #print(match)

    i = 0
    output = []
    while(i<len(match)):
        j = 0
        while(match[i][j] == ''):
            j+=1
        output.append(match[i][j])
        i+=1



   # match = re.findall(r"([\+\-]?)([\d]+)",sentence)
    #print(match)
    return output

