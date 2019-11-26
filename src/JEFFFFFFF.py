from Myro import *
from Graphics import *
import colorsys



black = makeColor(0,0,0)
white = makeColor(255,255,255)

def learningToPhoto():
    blackPixels = []
    whitePixels = []
    xBlack = 0
    yBlack = 0
    #manualCamera(1024,1000,100)
    I = takePicture()
    pic = Picture(I)
    for x in range(pic.width):
        for y in range(pic.height):
            orderedPair = {}
            
            coloredPixel = pic.getRGBA(x,y)
            #orderedPair.append([x,y])
            
            if coloredPixel[0] >= 110  and coloredPixel[0] <= 255 and coloredPixel[1] <=120 and coloredPixel[2] <=80:
                #setPixel(orderedPair,black)
                pic.setRGBA(x,y,0,0,0,255)
                blackPixels.append([x,y])
                xBlack += x
                yBlack += y
                #orderedPair[str (x) + " " + str (y)]
            else:
                pic.setRGBA(x,y,255,255,255,255)
                whitePixels.append([x,y])
                #setPixel(orderedPair[0],orderedPair[1],white)
    show(pic,"blob_image")
    show(I, "original_image")
    xCentroid = xBlack/len(blackPixels)
    yCentroid = yBlack/len(blackPixels)

    #learningToPhoto()
    #print(blackPixels)
    print("mass of centroid", len(blackPixels))
    print("AVERAGE X VALUE", xBlack/len(blackPixels) )
    print("AVERAGE Y VALUE", yBlack/len(blackPixels) )
    win = getWindow("blob_image")
    win.draw(Circle((xCentroid,yCentroid),5))
    
    



def colorTest():
    origPic = takePicture()
    #yuvValues = []
    yuvPic = Picture(origPic)
    for x in range(origPic.width):
        for y in range(origPic.height):
            rgbStuffs = origPic.getRGB(x,y)
            #print(rgbStuffs)
            yuvValues=colorsys.rgb_to_yiq(rgbStuffs[0],rgbStuffs[1],rgbStuffs[2])
            print(yuvValues)
            yuvPic.setRGB(x,y,yuvValues[0],yuvValues[1],yuvValues[2])
    show(yuvPic,"blob_image")
    show(origPic, "original_image")
    #xCentroid = xBlack/len(blackPixels)
    #yCentroid = yBlack/len(blackPixels)