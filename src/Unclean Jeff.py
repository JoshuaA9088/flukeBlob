from Myro import *
from Graphics import *
import colorsys
from socket import *

# win = Window("robot_display",427,266)
centroid = None
robot = getRobot()
if robot is None:
    camera = makeRobot("Scribbler", "com4")
    klaus = makeRobot("Scribbler", "com7")

"""
Graphics / Keypress Handle Setup START
"""
"""
alpha = makeColor(0,0,0,0)
green = makeColor(0,0,0)
white = makeColor(255,255,255)
vert13 = Line(Point(106.75,0),Point(106.75,266))
vert14 = Line(Point(213.5,0),Point(213.5,266))
vert15 = Line(Point(320.25,0),Point(320.25,266))
vert16 = Line(Point(427,0),Point(427,266))
vert13.draw(win)
vert14.draw(win)
vert15.draw(win)
vert16.draw(win)
hori4 = Line(Point(0,66.5),Point(427,66.5))
hori8 = Line(Point(0,133),Point(427,133))
hori12 = Line(Point(0,199.5),Point(427,199.5))
hori16 = Line(Point(0,266),Point(427,266))
hori4.draw(win)
hori8.draw(win)
hori12.draw(win)
hori16.draw(win)
vert13.tag = "temp"
vert14.tag = "temp"
vert15.tag = "temp"
vert16.tag = "temp"
hori4.tag = "temp"
hori8.tag = "temp"
hori12.tag = "temp"
hori16.tag = "temp"


def handleMouseDown(robot_display,event):
    print("x = ",event.x,"y = ",event.y)
    win.removeTagged("temp")
    win.removeTagged("line")
    lineToClick = Line(Point(event.x,event.y),Point(centroid[0],centroid[1]))
    lineToClick.draw(win)
    lineToClick.tag = "line"
    vert13.draw(win)
    vert14.draw(win)
    vert15.draw(win)
    vert16.draw(win)
    hori4.draw(win)
    hori8.draw(win)
    hori12.draw(win)
    hori16.draw(win)
    randCircle = Circle((200,200),7)
    randCircle.draw(win)
    global globalClickX
    global globalClickY
    globalClickX = event.x
    globalClickY = event.y
    if centroid != None:
        print(centroid)
win.onMouseDown(handleMouseDown)
"""
"""
Graphics / Keypress Handle Setup END
"""


def learningToPhoto():
    # Try Catch for system timeout error
    try:
        origPic = camera.takePicture()
    except SystemError:
        print("I'm in except")
        origPic = camera.takePicture()
    yuvValues = []
    transformPic = Picture(origPic)
    blobPic = Picture(transformPic)
    chassisBlobPic = Picture(transformPic)
    boardBlobPic = Picture(origPic)
    greenPixelsBoard = []
    whitePixelsBoard = []
    greenPixelsLed = []
    whitePixelsLed = []
    greenPixelsChassis = []
    whitePixelsChassis = []
    xGreenBoard = 0
    yGreenBoard = 0
    xGreenLed = 0
    yGreenLed = 0
    xGreenChassis = 0
    yGreenChassis = 0
    for x in range(origPic.width):
        for y in range(origPic.height):
            rgbStuffs = origPic.getRGB(x, y)
            foundChassis = detectChassis(
                rgbStuffs[0], rgbStuffs[1], rgbStuffs[2], transformPic, x, y)
            # foundLed = detectLed(rgbStuffs[0],rgbStuffs[1],rgbStuffs[2], transformPic,x,y)
            foundBoard = detectBoard(
                rgbStuffs[0], rgbStuffs[1], rgbStuffs[2], transformPic, x, y)
            """
            if foundLed == True:
                ledBlobPic.setRGB(x,y,0,0,0)
                greenPixelsLed.append([x,y])
                xGreenLed += x
                yGreenLed += y
            else:
                ledBlobPic.setRGB(x,y,255,255,255)
                whitePixelsLed.append([x,y])
            """
            if foundBoard is True:
                boardBlobPic.setRGB(x, y, 0, 0, 0)
                greenPixelsBoard.append([x, y])
                xGreenBoard += x
                yGreenBoard += y
            else:
                boardBlobPic.setRGB(x, y, 255, 255, 255)
                whitePixelsBoard.append([x, y])

            if foundChassis is True:
                chassisBlobPic.setRGB(x, y, 0, 0, 0)
                greenPixelsChassis.append([x, y])
                xGreenChassis += x
                yGreenChassis += y
            else:
                chassisBlobPic.setRGB(x, y, 255, 255, 255)
                whitePixelsChassis.append([x, y])

    # This is blob image not in yiq color space
    show(transformPic, "Transform")
    show(boardBlobPic, "Led Blob Image")
    show(chassisBlobPic, "Chassis Blob Image")
    win = getWindow("original_image")
    show(origPic, "original_image")

    try:
        xCentroidBoard = xGreenBoard / len(greenPixelsBoard)
        yCentroidBoard = yGreenBoard / len(greenPixelsBoard)
        # xCentroidLed = xGreenLed/len(greenPixelsLed)
        # yCentroidLed = yGreenLed/len(greenPixelsLed)
        xCentroidChassis = xGreenChassis / len(greenPixelsChassis)
        yCentroidChassis = yGreenChassis / len(greenPixelsChassis)
    except ZeroDivisionError:
        print("Zero Division Error")
    global centroid
    # centroid = [xCentroidLed,yCentroidLed,xCentroidChassis,yCentroidChassis,xCentroidBoard,yCentroidBoard]
    # Centroid with LED ^

    centroid = [xCentroidChassis, yCentroidChassis,
                xCentroidBoard, yCentroidBoard]
    """
    Grid of 16 START


    win.removeTagged("temp")
    blobPic.draw(win)
    vert13.draw(win)
    vert14.draw(win)
    vert15.draw(win)
    vert16.draw(win)
    hori4.draw(win)
    hori8.draw(win)
    hori12.draw(win)
    hori16.draw(win)


    Grid of 16 END
    """

    # Centroid Stats

    # print("mass of centroid", len(greenPixels))
    # print("AVERAGE X VALUE LED", xCentroidLed)
    # print("AVERAGE Y VALUE LED", yCentroidLed)
    print("AVERAGE X VALUE Chassis", xCentroidChassis)
    print("AVERAGE Y VALUE Chassis", yCentroidChassis)
    # win.draw(Circle((xCentroidLed,yCentroidLed),5))
    win.draw(Circle((xCentroidBoard, yCentroidBoard), 5))
    win.draw(Circle((xCentroidChassis, yCentroidChassis), 5))

    # marker2 = Circle((xCentroid,yCentroid),5)
    # ledMarker = Circle((xCentroidLed,yCentroidLed),60)
    ledMarker = Circle((xCentroidBoard, yCentroidBoard), 60)
    chassisMarker = Circle((xCentroidChassis, yCentroidChassis), 60)
    ledMarker.setFill(alpha)
    chassisMarker.setFill(alpha)
    ledMarker.draw(win)
    chassisMarker.draw(win)

    # marker.setFill(alpha)
    # marker.draw(win)
    # marker2.draw(win)

    # Centroid Stats


def detectChassis(r, g, b, chassisPic, x, y):
    yiqValues = colorsys.rgb_to_yiq(r, g, b)
    chassisPic.setRGB(x, y, yiqValues[0], yiqValues[1], yiqValues[2])
    yiqPixel = chassisPic.getRGB(x, y)
    return (yiqPixel[0] >= 0.580 and yiqPixel[1] >= 0.043 and yiqPixel[2] >= 0.030)


def detectLed(r, g, b, ledPic, x, y):
    yiqValues = colorsys.rgb_to_hsv(r, g, b)
    ledPic.setRGB(x, y, yiqValues[0], yiqValues[1], yiqValues[2])
    yiqPixel = ledPic.getRGB(x, y)
    if yiqPixel[2] >= 255:
        return True
    else:
        return False
# Uses YUV


def detectLed2(r, g, b, ledPic, x, y):
    yiqValues = colorsys.rgb_to_yuv(r, g, b)
    ledPic.setRGB(x, y, yiqValues[0], yiqValues[1], yiqValues[2])
    yiqPixel = ledPic.getRGB(x, y)
    if yiqPixel[2] >= 255:
        return True
    else:
        return False


def detectBoard(r, g, b, boardPic, x, y):
    yuvValues = rgb2yuv(r, g, b)
    boardPic.setRGB(x, y, yuvValues[0], yuvValues[1], yuvValues[2])
    yiqPixel = boardPic.getRGB(x, y)
    if yiqPixel[0] <= 200 and yiqPixel[1] >= 140 and yiqPixel[2] <= 200:
        return True
    else:
        return False


def gray():
    blackPixels = []
    whitePixels = []
    newPixels = []
    xBlackLed = 0
    yBlackLed = 0
    klaus.setLEDBack(1)
    try:
        gray1 = camera.takePicture("gray")
        # Try Catch for system timeout error
    except SystemError:
        gray1 = camera.takePicture("gray")
    wait(3)
    klaus.setLEDBack(0)
    gray2 = camera.takePicture("gray")
    joshPic = Picture(gray1)
    for x in range(gray1.width):
        for y in range(gray1.height):
            pixels1 = gray1.getRGB(x, y)

            if pixels1[0] > 254 and pixels1[1] > 254 and pixels1[2] > 254:
                joshPic.setRGB(x, y, 0, 0, 0)
                xBlackLed += x
                yBlackLed += y

            else:
                joshPic.setRGB(x, y, 255, 255, 255)

    show(joshPic, "blob_image")
    show(gray1, "gray1")
    show(gray2, "gray2")
