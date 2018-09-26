import re
def getNumberPattern():
    output = "[2][5][0-5]|[2][0-5][0-9]|[0-1][0-9][0-9]"

    return output
def getLinkPattern():
    output = r'[\s]*<a href="(?P<url>((ftps://)|((ftp://)(http://)|(https://)))[\w]+[(\.)(\w)]*)">(?P<text>[\w]+[\s]?[\w]+)</a>'
    return output

def parseFile(fileName):

    return

if __name__ == "__main__":
    pattern = getNumberPattern()
    m = re.search(pattern, "We can get less tham 300 pii, but more than 005.")


    htmlSnip = 'your can download the file from    <a href="ftps://local.files.io">The Repository</a> or you can search for it <a href="https://www.google.com">here.</a>'
    pattern = getLinkPattern()
    m = re.search(pattern ,htmlSnip )
    print(m.group("url"))