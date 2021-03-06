import numpy as np
from scipy import spatial,interpolate
import imageio
from PIL import Image, ImageDraw
import time
import os

class Affine:
    def __init__(self, source, destination):
        if(source.dtype is not np.dtype('float64')):
            raise ValueError("incorrect source")
        if(destination.dtype is not np.dtype('float64')):
            raise ValueError("incorrect destination")
        if(source.shape != (3,2)):
            raise ValueError('source incorrect ratio')
        if(destination.shape != (3,2)):
            raise ValueError('destionation incorrect ratio')
        self.source = source
        self.destination = destination
        h = np.linalg.solve(np.array([[source[0][0], source[0][1],1,0,0,0], [0,0,0,source[0][0],source[0][1],1],[source[1][0],source[1][1],1,0,0,0],[0,0,0,source[1][0],source[1][1],1],[source[2][0],source[2][1],1,0,0,0],[0,0,0,source[2][0],source[2][1],1]]),np.array([destination[0][0],destination[0][1],destination[1][0],destination[1][1],destination[2][0],destination[2][1]]))
        self.matrix = np.array([[h[0],h[1],h[2]],[h[3],h[4],h[5]],[0,0,1]])
        self.corX = [int(max(self.source[0][0],self.source[1][0],self.source[2][0])),int(min(self.source[0][0],self.source[1][0],self.source[2][0]))]
        self.corY = [int(max(self.source[0][1],self.source[1][1],self.source[2][1])),int(min(self.source[0][1],self.source[1][1],self.source[2][1]))]

    def transform(self,sourceImage, destinationImage):
        if(not isinstance(sourceImage,np.ndarray)):
            raise TypeError('transform: sourceImage type incorrect')
        if(not isinstance(destinationImage,np.ndarray)):
            raise TypeError('transform: destinationImage type incorrect')

        self.interpolation = interpolate.RectBivariateSpline(range(self.corY[0]-self.corY[1]),range(self.corX[0]-self.corX[1]),sourceImage[self.corY[1]:self.corY[0],self.corX[1]:self.corX[0]],kx=1,ky=1)
        output = Image.new('L',(sourceImage.shape[1],sourceImage.shape[0]),0)
        vert = [tuple(a) for a in self.destination]
        ImageDraw.Draw(output).polygon(vert, outline=255, fill=255)
        mask = np.array(output)
        inv_h = np.linalg.inv(self.matrix)

        a, b = np.where(mask == 255)
        m = np.ones(shape=(3,len(a)),dtype=np.float64)
        m[1],m[0] = a,b
        first = np.matmul(inv_h, m)
        new_p = np.round(self.interpolation.ev(first[1]-self.corY[1],first[0]-self.corX[1]).astype(np.uint8))
        i = [j for j in range(len(a))]
        destinationImage[a,b] = new_p[i]

class Blender:
    def __init__(self, startImage, startPoints, endImage, endPoints):
        if(not isinstance(startImage,np.ndarray)):
            raise TypeError("1.startImage incorrect")
        if(not isinstance(startPoints,np.ndarray)):
             raise TypeError("2.startPoints incorrect")
        if(not isinstance(endImage,np.ndarray)):
             raise TypeError("3.endImage incorrect")
        if(not isinstance(endPoints,np.ndarray)):
             raise TypeError("4.endPoints incorrect")

        self.startImage = startImage
        self.startPoints = startPoints
        self.endImage = endImage
        self.endPoints = endPoints

    def getBlendedImage(self,alpha):
        if(not(alpha >= 0 and alpha <= 1)):
            raise ValueError("0 <= alpha <= 1")
        source = spatial.Delaunay(self.startPoints)
        startTriArray = self.startPoints[source.simplices]
        endTriArray = self.endPoints[source.simplices]
        newImg1 = np.array(Image.new('L',(self.startImage.shape[1],self.startImage.shape[0]), 0))
        newImg2 = np.array(Image.new('L',(self.endImage.shape[1],self.endImage.shape[0]), 0))

        startInterpolation = interpolate.RectBivariateSpline(range(self.startImage.shape[0]),range(self.startImage.shape[1]),self.startImage,kx=1,ky=1)
        endInterpolation = interpolate.RectBivariateSpline(range(self.endImage.shape[0]),range(self.endImage.shape[1]),self.endImage,kx=1,ky=1)

        i = 0
        while i<(len(startTriArray)):
            triangle3 = np.array([startTriArray[i][0] * (1 - alpha) + alpha * endTriArray[i][0],startTriArray[i][1] * (1 - alpha) + alpha * endTriArray[i][1], startTriArray[i][2] * (1 - alpha) + alpha * endTriArray[i][2]])#

            startAffine = Affine(startTriArray[i],triangle3)
            startAffine.interpolation = startInterpolation
            startAffine.transform(self.startImage,newImg1)
            endAffine = Affine(endTriArray[i],triangle3)
            endAffine.interpolation = endInterpolation
            endAffine.transform(self.endImage,newImg2)
            i+=1

        outputImage = np.round(((1-alpha)*newImg1 + alpha*newImg2).astype(np.uint8))
        return outputImage
    def generateMorphVideo(self, targerFolderPath, sequenceLength, includeReversed):
        if(sequenceLength < 10):
            raise ValueError("sequenceLength is greater than or equal to 10")
        if(os.path.exists(targerFolderPath) is False):
            os.mkdir(targerFolderPath)
        alpha = 0
        increment = 1 / (sequenceLength-1)
        i=0
        while (i<sequenceLength):
            a = self.getBlendedImage(alpha)
            digit = str(i+1).zfill(3)
            imageio.imwrite(targerFolderPath+"/frame"+digit+".jpg",a)
            i+=1
            alpha+=increment
            if(alpha > 1):
                 alpha = 1
        if(includeReversed is True):
            j = i
            i = 0
            alpha = 0
            while(i<sequenceLength):
                a = self.getBlendedImage((1-alpha))
                digit = str(j+1).zfill(3)
                imageio.imwrite(targerFolderPath+"/frame"+digit+".jpg",a)
                i+=1
                j+=1
                alpha+=increment
                if(alpha > 1):
                    alpha = 1
        video = imageio.get_writer(targerFolderPath+'/'+'morph.mp4',fps=5,macro_block_size = None)
        for file in os.listdir(targerFolderPath):
            path = targerFolderPath+'/'+file
            video.append_data(imageio.imread(path))
        video.close()




class ColorAffine:
    def __init__(self, source, destination):
        if(source.dtype is not np.dtype('float64')):
            raise ValueError("incorrect source")
        if(destination.dtype is not np.dtype('float64')):
            raise ValueError("incorrect destination")
        if(source.shape != (3,2)):
            raise ValueError('source incorrect ratio')
        if(destination.shape != (3,2)):
            raise ValueError('destionation incorrect ratio')
        # self.source = source
        # self.destination = destination
        # h = np.linalg.solve(np.array([[source[0][0], source[0][1],1,0,0,0], [0,0,0,source[0][0],source[0][1],1],[source[1][0],source[1][1],1,0,0,0],[0,0,0,source[1][0],source[1][1],1],[source[2][0],source[2][1],1,0,0,0],[0,0,0,source[2][0],source[2][1],1]]),np.array([destination[0][0],destination[0][1],destination[1][0],destination[1][1],destination[2][0],destination[2][1]]))
        # self.matrix = np.array([[h[0],h[1],h[2]],[h[3],h[4],h[5]],[0,0,1]])
        # self.corX = [int(max(self.source[0][0],self.source[1][0],self.source[2][0])),int(min(self.source[0][0],self.source[1][0],self.source[2][0]))]
        # self.corY = [int(max(self.source[0][1],self.source[1][1],self.source[2][1])),int(min(self.source[0][1],self.source[1][1],self.source[2][1]))]
    def transform(self,sourceImage, destinationImage):
        print("trans")
        if(not isinstance(sourceImage,np.ndarray)):
            raise TypeError('transform: sourceImage type incorrect')
        if(not isinstance(destinationImage,np.ndarray)):
            raise TypeError('transform: destinationImage type incorrect')
        # output = Image.new('RGB',(sourceImage.shape[1],sourceImage.shape[0]),0)
        # mask = np.array(output)
        # vert = [tuple(a) for a in self.destination]
        # ImageDraw.Draw(output).polygon(vert, outline=255, fill=255)
        # inv_h = np.linalg.inv(self.matrix)
        # maskWhite = np.where(mask==255)
        # xList,yList,zList = maskWhite
        # m = np.ones(shape=(3,len(xList)),dtype=np.float64)
        # m[1],m[0] = xList,yList
        # first = np.matmul(inv_h, m)
        # subImg = sourceImage[self.corY[1]+1 if self.corY[1]-1 >=0 else 0:self.corY[0]+1 if self.corY[0]+1 <= sourceImage.shape[0] else sourceImage.shape[0], self.corX[1]-1 if self.corX[1]-1 >=0 else 0: self.corX[0]+1 if self.corX[0]+1 <= sourceImage.shape[1] else sourceImage.shape[1]]
        # xInd = range((self.corX[0]+1 if self.corX[0]+1 <= sourceImage.shape[1] else sourceImage.shape[1])-(self.corX[1]-1 if self.corX[1]-1 >= 0 else 0))
        # yInd = range((self.corY[0]+1 if self.corY[0]+1 <= sourceImage.shape[0] else sourceImage.shape[0])-(self.corY[1]-1 if self.corY[1]-1 >= 0 else 0))
        #
        # intlR = interpolate.RectBivariateSpline(yInd,xInd,z=subImg[:,:,0],kx=1,ky=1)
        # intlG = interpolate.RectBivariateSpline(yInd,xInd,z=subImg[:,:,1],kx=1,ky=1)
        # intlB = interpolate.RectBivariateSpline(yInd,xInd,z=subImg[:,:,2],kx=1,ky=1)
        #
        # new_pR = np.round(intlR.ev(first[1]-(self.corY[1]-1 if self.corY[1]-1 >= 0 else 0),first[0]-(self.corX[1]-1 if self.corX[1]-1 >= 0 else 0))).astype(np.uint8)
        # new_pG = np.round(intlG.ev(first[1]-(self.corY[1]-1 if self.corY[1]-1 >= 0 else 0),first[0]-(self.corX[1]-1 if self.corX[1]-1 >= 0 else 0))).astype(np.uint8)
        # new_pB = np.round(intlB.ev(first[1]-(self.corY[1]-1 if self.corY[1]-1 >= 0 else 0),first[0]-(self.corX[1]-1 if self.corX[1]-1 >= 0 else 0))).astype(np.uint8)
        #
        # i = [j for j in range(len(xList))]
        # destinationImage[xList,yList,0] = new_pR
        # destinationImage[xList,yList,1] = new_pG
        # destinationImage[xList,yList,2] = new_pB

class ColorBlender:
    def __init__(self,startImage, startPoints, endImage, endPoints):
        self.startImage = startImage
        self.startPoints = startPoints
        self.endImage = endImage
        self.endPoints = endPoints

    def getBlendedImage(self,alpha):
        if(not(alpha >= 0 and alpha <= 1)):
            raise ValueError("0 <= alpha <= 1")
        source = spatial.Delaunay(self.startPoints)
        startTriArray = self.startPoints[source.simplices]
        endTriArray = self.endPoints[source.simplices]
        newImg1 = np.array(Image.new('RGB',(self.startImage.shape[1],self.startImage.shape[0]), 0))
        newImg2 = np.array(Image.new('RGB',(self.endImage.shape[1],self.endImage.shape[0]), 0))
        #
        startInterpolation = interpolate.RectBivariateSpline(range(self.startImage.shape[0]),range(self.startImage.shape[1]),self.startImage,kx=1,ky=1)
        endInterpolation = interpolate.RectBivariateSpline(range(self.endImage.shape[0]),range(self.endImage.shape[1]),self.endImage,kx=1,ky=1)

        i = 0
        while i<(len(startTriArray)):
            triangle3 = np.array([startTriArray[i][0] * (1 - alpha) + alpha * endTriArray[i][0],startTriArray[i][1] * (1 - alpha) + alpha * endTriArray[i][1], startTriArray[i][2] * (1 - alpha) + alpha * endTriArray[i][2]])#
            startAffine = ColorAffine(startTriArray[i],triangle3)
            startAffine.interpolation = startInterpolation
            startAffine.transform(self.startImage,newImg1)
            endAffine = ColorAffine(endTriArray[i],triangle3)
            endAffine.interpolation = endInterpolation
            endAffine.transform(self.endImage,newImg2)
            i+=1

        outputImage = np.round(((1-alpha)*newImg1 + alpha*newImg2).astype(np.uint8))
        return outputImage


    def generateMorphVideo(self, targerFolderPath, sequenceLength, includeReversed):
        if(sequenceLength < 10):
            raise ValueError("sequenceLength is greater than or equal to 10")
        if(os.path.exists(targerFolderPath) is False):
            os.mkdir(targerFolderPath)


def main(startFile,startPointFile, endFile,endPointFile):
    start_time = time.time()
    readStartImage = imageio.imread(startFile)
    readEndImage = imageio.imread(endFile)

    startImageArray = np.array(readStartImage)
    endImageArray = np.array(readEndImage)
    startPoint = np.loadtxt(startPointFile, dtype = np.float64)
    endPoint = np.loadtxt(endPointFile, dtype = np.float64)

    blender = Blender(startImageArray,startPoint,endImageArray,endPoint)
    # blender = Blender(grayTrans(startImageArray),startPoint,grayTrans(endImageArray),endPoint)
    blender.getBlendedImage(1)
    blender.generateMorphVideo("gay",10,False)
    #blender = ColorBlender(startImageArray,startPoint,endImageArray,endPoint)
    #blender.getBlendedImage(1)

    print(" %s  seconds" % (time.time() - start_time))

def grayTrans(array):
    print(type(array))
    output = []
    for i in range(len(array)):
        output.append(array[i][0:799,0])
    return np.array(output)

if __name__ == '__main__':
    # startFile = "pip.jpg"
    # endFile = "wang.jpg"
    # startPointFile = "pip.jpg.txt"
    # endPointFile = "wang.jpg.txt"
    # startFile = "WolfGray.jpg"
    # endFile = "Tiger2Gray.jpg"
    startPointFile = "wolf.jpg.txt"
    endPointFile = "tiger2.jpg.txt"
    # main(startFile,startPointFile,endFile,endPointFile)
    startFile = "WolfColor.jpg"
    endFile = "Tiger2Color.jpg"
    main(startFile,startPointFile,endFile,endPointFile)
