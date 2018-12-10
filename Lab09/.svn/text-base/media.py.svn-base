import os, subprocess,re,glob,sys
class Image:
    def __init__(self,file,width,height):
        self.filename = file
        self.extension = file.rsplit(".",1)[-1]
        self.width = width
        self.height = height

    def play(self):
        if (os.path.exists(self.filename) is True):
            subprocess.check_output(['display', self.filename])
        else:
           raise MediaNotFound(self)


class Video(Image):
    def __init__(self,file,width,height,duration):
        super().__init__(file,width,height)
        self.duration_secs = duration
    def play(self):
        if (os.path.exists(self.filename) is True):
            subprocess.check_output(['mplayer', self.filename])
        else:
           raise MediaNotFound(self)

class MediaNotFound(FileNotFoundError):
    def __init__(self,obj):
        self.filename = obj.filename
        self.media_type = type(obj)
        super().__init__(self.filename)

def create_media_file(filename):
    extension = filename.rsplit(".",1)[-1]
    path = os.path.expanduser(filename)
    if extension in('jpg','png'):
        identify = subprocess.check_output(['identify',path],stderr=subprocess.STDOUT)
        ma = re.search(r"([0-9]+)x([0-9]+)",str(identify))
        return Image(path,int(ma.group(1)),int(ma.group(2)))
    elif extension in('avi','mp4'):
        identify = subprocess.check_output(['ffprobe','-i',path],stderr=subprocess.STDOUT)
        ma = re.search(r" ([0-9]+)x([0-9]+) ",str(identify))
        du = re.search(r"Duration: ([0-9]+)\:([0-9]+)\:([0-9]+)\.([0-9]+)",str(identify))
        return Video(path,int(ma.group(1)),int(ma.group(2)),int(du.group(3)))
    else:
        pass

def get_media_files(dir_path):
    dir_path = os.path.expanduser(dir_path)+'*'
    output = []
    for file in glob.glob(dir_path):
        add = create_media_file(file)
        if add is None:
            continue
        else:
            output.append(add)
    return output

def main():
    media_files = get_media_files(sys.argv[1])
    while True:
        entry = input("> ")
        print("you just entered " + entry)
if __name__ == "__main__":
    path1 = "~ee364/Lab08_media/flowers.avi"
    path2 = "~ee364/Lab08_media/jellyfish.png"
    path = "~ee364/Lab08_media/"
    print(get_media_files(path))
    #a = create_media_file(path1)
    #a.play()
    main()