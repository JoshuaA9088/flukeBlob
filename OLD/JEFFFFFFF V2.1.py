from Myro import *
from Graphics import *
import colorsys 

camera = makeRobot("Scribbler","com9")
klaus = makeRobot("Scribbler","com11")
alpha = makeColor(0,0,0,0)
green = makeColor(0,0,0)
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
    origPic = camera.takePicture()
    yuvValues = []
    yiqPic = Picture(origPic)
    printedYIQPic = Picture(yiqPic)
    greenPixels = []
    whitePixels = []
    xGreen = 0
    yGreen = 0
    for x in range(origPic.width):
        for y in range(origPic.height):
            rgbStuffs = origPic.getRGB(x,y)
            #print(rgbStuffs)
            yiqValues=colorsys.rgb_to_yiq(rgbStuffs[0],rgbStuffs[1],rgbStuffs[2])
            
            yiqPic.setRGB(x,y,yiqValues[0],yiqValues[1],yiqValues[2])
            yiqPixel = yiqPic.getRGB(x,y)
            #printedYIQPic = Picture(yiqPic)
            
            if yiqPixel[0] >= 0.580 and yiqPixel[1] >= 0.043 and yiqPixel[2] >= 0.030:
                yiqPic.setRGB(x,y,0,0,0)
                greenPixels.append([x,y])
                xGreen += x
                yGreen += y
            else:
                yiqPic.setRGB(x,y,255,255,255)
                whitePixels.append([x,y])
            
                
    show(yiqPic,"blob_image")
    show(origPic, "original_image")
    #show(printedYIQPic, "GET_GUD")
    xCentroid = xGreen/len(greenPixels)
    yCentroid = yGreen/len(greenPixels)

    #learningToPhoto()
    #print(blackPixels)
    print("mass of centroid", len(greenPixels))
    print("AVERAGE X VALUE", xGreen/len(greenPixels) )
    print("AVERAGE Y VALUE", yGreen/len(greenPixels) )
    win = getWindow("blob_image")
    marker2 = Circle((xCentroid,yCentroid),5)
    marker = Circle((xCentroid,yCentroid),60)
    marker.setFill(alpha)
    marker.draw(win)
    marker2.draw(win)
    #xCentroid = xBlack/len(blackPixels)
    #yCentroid = yBlack/len(blackPixels)