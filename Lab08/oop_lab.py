import os, subprocess,re
class Image:
    def __init__(self,file,wid,hei):
        nameList = file.split('.')
        self.filename = nameList[0]
        self.extension = nameList[1]
        self.width = wid
        self.height = hei
class Video(Image):
    def __init__(self,file,wid,hei,dura):
        Image.__init__(self,file,wid,hei)
        self.duration_secs = dura
def create_media_file(filename):
    name = re.search(r"([a-zA-Z]+)\.([a-zA-Z0-9]+)",filename)
    extension=name.group(2)
    if extension == 'jpg' or extension == 'png':
        identify = subprocess.check_output(['identify',filename],stderr=subprocess.STDOUT)
        ma = re.search(r"([0-9]+)x([0-9]+)",str(identify))
        return Image(name.group(0),int(ma.group(1)),int(ma.group(2)))
    elif extension == 'avi' or extension == 'mp4':
        identify = subprocess.check_output(['ffprobe','-i',filename],stderr=subprocess.STDOUT)
        ma = re.search(r" ([0-9]+)x([0-9]+) ",str(identify))
        du = re.search(r"Duration: ([0-9]+)\:([0-9]+)\:([0-9]+)\.([0-9]+)",str(identify))
        return Video(name.group(0),int(ma.group(1)),int(ma.group(2)),int(du.group(3)))
    else:
        return None
if __name__ == "__main__":
    filename = "flowers.avi"
    filename2 = "jellyfish.png"
    path = os.path.expanduser('~ee364/Lab08_media/'+filename2)
    print(path)
    print((create_media_file(path)))