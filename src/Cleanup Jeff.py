sfrom Myro import *
from Graphics import *
import colorsys
from socket import *

centroid = None
robot = getRobot()
if robot == None:
    camera = makeRobot("Scribbler","com4")
    klaus = makeRobot("Scribbler","com7")

def learningToPhoto():
    #Try Catch for system timeout error
    try:
        origPic = camera.takePicture()
    except SystemError:
        print("I'm in except")
        origPic = camera.takePicture()
    #YUV Values used in board tracking
    yuvValues = []
    transformPic = Picture(origPic)
    blobPic = Picture(transformPic)
    #Picture in YIQ to find chassis
    chassisBlobPic = Picture(transformPic)
    #Picture in YUV to find board
    boardBlobPic = Picture(origPic)
    #Pixel data for board
    greenPixelsBoard = []
    whitePixelsBoard = []
    #Pixel data for chassis
    greenPixelsChassis = []
    whitePixelsChassis = []
    #Centroid data for board
    xGreenBoard = 0
    yGreenBoard = 0
    #Centroid data for Chassis
    xGreenChassis = 0
    yGreenChassis = 0
    for x in range(origPic.width):
        for y in range(origPic.height):
            rgbValues = origPic.getRGB(x,y)
            #Passing other functions the rgb, pic, and coordinate data
            foundChassis = detectChassis(rgbValues[0],rgbValues[1],rgbValues[2], transformPic,x,y)
            foundBoard = detectBoard(rgbValues[0],rgbValues[1],rgbValues[2], transformPic,x,y)
            #Create blob image for board
            if foundBoard == True:
               boardBlobPic.setRGB(x,y,0,0,0)
               greenPixelsBoard.append([x,y])
               xGreenBoard += x
               yGreenBoard += y
            else:
                boardBlobPic.setRGB(x,y,255,255,255)
                whitePixelsBoard.append([x,y])
            #Create blob image for chassis
            if foundChassis == True:
                chassisBlobPic.setRGB(x,y,0,0,0)
                greenPixelsChassis.append([x,y])
                xGreenChassis += x
                yGreenChassis += y
            else:
                chassisBlobPic.setRGB(x,y,255,255,255)
                whitePixelsChassis.append([x,y])


    #Picture image in YUV space
    show(transformPic, "Transform")
    #Blob image for board
    show(boardBlobPic,"Board Blob Image")
    #Blob image for chassis
    show(chassisBlobPic, "Chassis Blob Image")
    #attack win handle to original image
    win = getWindow("original_image")
    show(origPic, "original_image")

    #Calculates centroid data
    try:
        xCentroidBoard = xGreenBoard / len(greenPixelsBoard)
        yCentroidBoard = yGreenBoard / len(greenPixelsBoard)
        xCentroidChassis = xGreenChassis/len(greenPixelsChassis)
        yCentroidChassis = yGreenChassis/len(greenPixelsChassis)
    #Mostly used during debugging to prevent error when no pixels were detected in blob image
    except ZeroDivisionError:
        print("Zero Division Error")
    #Globalize centroid data to be used in other functions
    global centroid
    centroid = [xCentroidChassis,yCentroidChassis,xCentroidBoard,yCentroidBoard]


    #Centroid Stats Chassis
    print("AVERAGE X VALUE Chassis", xCentroidChassis)
    print("AVERAGE Y VALUE Chassis", yCentroidChassis)
    print("AVERAGE X VALUE Board", xCentroidBoard)
    print("AVERAGE Y VALUE Board", yCentroidBoard)
    #Draw circles around board and chassis
    win.draw(Circle((xCentroidBoard,yCentroidBoard),5))
    win.draw(Circle((xCentroidChassis,yCentroidChassis),5))
    boardMarker = Circle((xCentroidBoard,yCentroidBoard),60)
    chassisMarker = Circle((xCentroidChassis, yCentroidChassis),60)
    boardMarker.setFill(alpha)
    chassisMarker.setFill(alpha)
    boardMarker.draw(win)
    chassisMarker.draw(win)

#Uses YIQ to detect red. Predator vision, red is green and everything else is red.
def detectChassis(r,g,b,chassisPic,x,y):
    yiqValues=colorsys.rgb_to_yiq(r,g,b)
    chassisPic.setRGB(x,y,yiqValues[0],yiqValues[1],yiqValues[2])
    yiqPixel = chassisPic.getRGB(x,y)
    if yiqPixel[0] >= 0.580 and yiqPixel[1] >= 0.043 and yiqPixel[2] >= 0.030:
        return True
    else:
        return False

#Uses YUV to see board or balloon, best works with blue.
def detectBoard(r,g,b,boardPic,x,y):
    yuvValues = rgb2yuv(r,g,b)
    boardPic.setRGB(x,y,yuvValues[0],yuvValues[1],yuvValues[2])
    yiqPixel = boardPic.getRGB(x,y)
    if yiqPixel[0] <= 200 and yiqPixel[1] >=140 and yiqPixel[2] <=200:
        return True
    else:
        return False

