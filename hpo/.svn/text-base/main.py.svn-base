#!/usr/local/bin/python3.4
import urllib.request,flask,os,re, sys,hashlib,tempfile, shutil, contextlib,collections,mimetypes,cv2,shutil,numpy
from lxml.html import HTMLParser, document_fromstring
import lxml.etree

def get_html_at_url(url,charset="UTF-8"):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    return resp.read().decode(charset)
def make_etree(html,url):
    parser = HTMLParser(encoding='UTF-8')
    root = document_fromstring(html,parser=parser,base_url=url)
    return root

app = flask.Flask(__name__)

@app.route('/')
def root_page():
    return flask.render_template('root.html')

@app.route('/view/')
def view_page():
    social = r"facebook.com|whatsapp.com|instagram.com|twitter.com"
    url = flask.request.args.get("url")
    if re.search(social, url):
        sys.exit(1)
    else:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'PurdueUniversityClassProject/1.0 (yang900@purdue.edu https://goo.gl/dk8u5S)')
        htmldecode = test(url)
        return "<base href=" + url + htmldecode.decode('UTF-8') + ">"

#--------------------------------------------------milestone2

@contextlib.contextmanager
def pushd_temp_dir(base_dir=None, prefix="tmp.hpo."):
    if base_dir is None:
        proj_dir = sys.path[0]
        # e.g., "/home/ecegridfs/a/ee364z15/hpo"

        main_dir = os.path.join(proj_dir, "data")
        # e.g., "/home/ecegridfs/a/ee364z15/hpo/data"

    # Create temp directory
    temp_dir_path = tempfile.mkdtemp(prefix=prefix, dir=base_dir)

    try:
        start_dir = os.getcwd()  # get current working directory
        os.chdir(temp_dir_path)  # change to the new temp directory
        try:
            yield
        finally:
            # No matter what, change back to where you started.
            os.chdir(start_dir)
    finally:
        # No matter what, remove temp dir and contents.
        shutil.rmtree(temp_dir_path, ignore_errors=True)

def make_filename(url, extension):
    output = hashlib.sha1(url).hexdigest()
    return output+'.'+extension

@contextlib.contextmanager
def fetch_images(etree):
    with pushd_temp_dir():
        filename_to_node = collections.OrderedDict()
        imgsrc = etree.findall('.//img')
        for nodeimg in imgsrc:
            src = nodeimg.base_url + nodeimg.get('src')
            resp = urllib.request.urlopen(src)
            exten = mimetypes.guess_extension(resp.info().get("Content-Type"))
            regex = r"(?P<dot>.)(?P<ext>[A-Za-z0-9]+)"
            exten = re.match(regex,exten).group(2)
            url = src.encode('utf8')
            filename = make_filename(url, exten)
            with open(os.path.join(filename), "wb") as output:
                output.write(resp.read())
            filename_to_node[filename] = nodeimg
        yield filename_to_node

def get_image_info(filename):
    faceDictList = []
    outputDict = {}
    img = cv2.imread(filename)
    face_cascade = cv2.CascadeClassifier('/home/ecegridfs/a/ee364/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    facelist = face_cascade.detectMultiScale(img_grayscale, 1.3, 5)
    outputDict["w"] = img.shape[1]
    outputDict["h"] = img.shape[0]
    for faces in facelist:
        facesDict={}
        facesDict["x"] = faces[0]
        facesDict["y"] = faces[1]
        facesDict["w"] = faces[2]
        facesDict["h"] = faces[3]
        faceDictList.append(facesDict)
        add_glasses(filename,facesDict)
    outputDict["faces"] = faceDictList
# Credit: Adapted from tutorial in OpenCV-Python Tutorials, cv2.imread, Face Detection using Haar Cascades,
#         License: PSFL https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html
#         https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html?highlight=imread#cv2.imread
#         https://docs.opencv.org/3.4/d7/d8b/tutorial_py_face_detection.html
    return outputDict

def find_profile_photo_filename(filename_to_etree):
    for key in filename_to_etree:
            img=get_image_info(key)
            imgArea = img['w']*img['h']
            for faces in img['faces']:
                faceArea = faces['w']*faces['h']
                if (faceArea/imgArea >=0.1):
                    add_glasses(key,faces)
                    return [key,faces]
    return

def copy_profile_photo_to_static(filename):
    shutil.copy(filename, sys.path[0]+"/static")
    return os.path.join(app.static_folder,filename)

#-------------milestone3
def add_glasses(filename, face_info):
    ycenter=0
    centerOfEyes=[]
    eye_cascade = cv2.CascadeClassifier('/home/ecegridfs/a/ee364/site-packages/cv2/data/haarcascade_eye.xml')
    image = cv2.imread(filename)
    glass_img = cv2.imread(os.path.join(sys.path[0],'testglass.png')) #imporm glasses image
    img_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes =  eye_cascade.detectMultiScale(img_grayscale)
    for (eyeX,eyeY,eyeW,eyeH) in eyes:  #locate the center of eyes
        centerOfEyes.append([int(eyeX+0.5*eyeW), int(eyeY+0.5*eyeH)])
    if len(centerOfEyes) == 0:
        centerOfEyes.append([(int(face_info.get('w')*0.3)+face_info.get('x')), int(face_info.get('h')*0.4+face_info.get('y'))])
        centerOfEyes.append([(int(face_info.get('w')*0.7)+face_info.get('x')), int(face_info.get('h')*0.4+face_info.get('y'))])
    #---------
    overlay_img = numpy.ones(image.shape,numpy.uint8)*255
    hglass,wglass = glass_img.shape[:2]
    scaling_factor = 2.5*abs(centerOfEyes[1][0]-centerOfEyes[0][0])/wglass
    overlay_glasses = cv2.resize(glass_img,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
    xcenter = centerOfEyes[0][0] if centerOfEyes[0][0]<centerOfEyes[1][0] else centerOfEyes[1][0]
    xcenter -= 0.3*overlay_glasses.shape[1]
    ycenter += 1.2*overlay_glasses.shape[0]
    hoverlay, woverlay  = overlay_glasses.shape[:2]
    overlay_img[int(ycenter):int(ycenter+hoverlay), int(xcenter):int(xcenter+woverlay)] = overlay_glasses
    ret, mask = cv2.threshold(cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY), 120, 255, cv2.THRESH_BINARY)
    # Credit: Copied with minor changes from example in OpenCV Eye detection example- Try out glasses using OpenCV
    #           License: https://shahsparx.me/privacy-policy/
    #            https://shahsparx.me/opencv-eye-detection-glasses-opencv/

    #combine glass and face then save the photo in static folder
    final_img =cv2.add(cv2.bitwise_and(image, image, mask=mask),cv2.bitwise_and(overlay_img, overlay_img, mask=cv2.bitwise_not(mask)))
    cv2.imwrite(os.path.join(app.static_folder,"glassesface"+filename),final_img)
    return os.path.join(app.static_folder,"glassesface"+filename)

def test(url):
    html = get_html_at_url(url)
    etree = make_etree(html,url)
    with fetch_images(etree) as filename_to_node:
        facePhotoName = find_profile_photo_filename(filename_to_node)
        copy_profile_photo_to_static(facePhotoName[0])
        glassFace = add_glasses(facePhotoName[0],facePhotoName[1])
        static_url = flask.url_for('static', filename=os.path.basename(glassFace), _external=True)
        phtotNode = filename_to_node.get(facePhotoName[0])
        phtotNode.set("src", static_url)
    return lxml.etree.tostring(etree)

if __name__ == '__main__':

    app.run(host="127.0.0.1", port=os.environ.get("ECE364_HTTP_PORT", 8000),
            use_reloader=True, use_evalex=False, debug=True, use_debugger=False)
    # Credit:  Alex Quinn.  Used with permission.  Preceding line only.


    # print(make_filename('http://people.eecs.berkeley.edu/~graham/SLG1jpg.jpeg', 'jpg'))
    #filename = '43cdcd7c62213cf0af22cef70f330af53987d490.jpeg'
    #face_info = {'w': 99, 'x': 23, 'h': 99, 'y': 52}
    #add_glasses('manface.jpg', face_info)
    #test("http://alexquinn.org/")
    #get_image_info("testface.jpg")