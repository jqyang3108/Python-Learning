import re

def extract_values(sentence):
    regex1 = r"[+-][\d]{1}.[\d]+e[+-][\d]+" #scientice notation  with +or-
    regex2 = r"[\d]{1}.[\d]+e[+-][\d]+"    #scientice notation  without +or-
    regex3 = r"[+-][\d]+.[\d]+|[\d]+.[\d]+" #float with +or-
    regex4 = r"[\d]+.[\d]"                  #float without +or-
    regex5 = r"[+-][\d]+"                   #int with +or-
    regex6 = r"[\d]+"                       #int without +or-
    regex = regex1+"|"+ regex2+"|"+regex3+"|"+regex4+"|"+regex5+"|"+regex6  #search from the most detailed regex
    output = re.findall(regex,sentence, re.I)

    return output

def get_switches(commandline):
    regex1 = r"[\\+]([a-z])"  #starts with + or \ followed by a lower case letter
    regex2 = r"[\s]+"  #one or more spaces
    regex3 = r"([^ \\+]+)"  #any value that is not the switch(doesnot start with + and /)
    regex = regex1+regex2+regex3
    m = re.findall(regex, commandline)
    return m