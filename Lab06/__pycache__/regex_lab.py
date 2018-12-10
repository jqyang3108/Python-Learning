import re

def extractValues(sentence):
    #print('here')
    regex  =r"[+-][\d]{1}.[\d]+e[+-][\d]+|[\d]{1}.[\d]+e[+-][\d]+|[+-][\d]+.[\d]+|[\d]+.[\d]+|[+-][\d]+|[\d]+"
    m = re.findall(regex, sentence, re.I)

    #print(m)
    return m

def getSwitches(commandline):
    #print(commandline)
    regex = r"[\\+]([a-z])[\s]+([^ +\\]+)"
    m = re.findall(regex, commandline)

    print(m)

def main():
    sentence = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55. Assume" \
               "that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023. "

    print(extractValues(sentence))

    commandline = r'myScript.bash +v 333 \a 2   +p /local/bin/somefolder  \a 666'
    getSwitches(commandline)

if __name__ == '__main__':
    main()