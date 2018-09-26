#! /usr/bin/env python3.4

#Jiaqi Yang
#Lab03

#-------------------------------------
def filterByLetter(sentence, c):

    s = sentence.split()
    lens = len(s)
    output = []
    i=0
    while(i<len(s)):
        j=0
        if(s[i].startswith(c) or s[i].endswith(c)):
            if(s[i] not in output):
                output.append(s[i])
        i+=1
    return output


def getCumulativeSum():
    i = 1
    list=[]
    while(i<=100):
        j=1
        part = 0
        while(j<=i):
            part = part+j
            j+=1
        list.append(part)
        i+=1
    return list


if __name__ == "__main__":
    s="the power of this engine matches that of the one we had last year"

    result = filterByLetter(s, "e")
    #result = getCumulativeSum()
    print(result)