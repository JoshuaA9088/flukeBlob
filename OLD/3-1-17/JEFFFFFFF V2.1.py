from Myro import *
from Graphics import *
import colorsys 
from socket import *

win = Window("robot_display",427,266)
centroid = None


robot = getRobot()

if robot == None:   
    camera = makeRobot("Scribbler","com6")
    klaus = makeRobot("Scribbler","com8")
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
def learningToPhoto():
    """
    blackPixels = []
    whitePixels = []
    xBlack = 0
    yBlack = 0
    """
    try:
        origPic = camera.takePicture()
    except SystemError:
        print("I'm in except")
        origPic = camera.takePicture()
    yuvValues = []
    yiqPic = Picture(origPic)
    printedYIQPic = Picture(yiqPic)
    blackPixels = []
    whitePixels = []
    xBlack = 0
    yBlack = 0
    #camera.manualCamera(900,900,100)
    I = camera.takePicture()
    #I = klaus.manualCamera(900,600,900)
    pic = Picture(I)
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
                blackPixels.append([x,y])
                xBlack += x
                yBlack += y
            else:
                yiqPic.setRGB(x,y,255,255,255)
                whitePixels.append([x,y])
    #show(pic,"robot_display")
    #show(yiqPic,"blob_image")
    #show(origPic, "original_image")
    #show(I, "original_image")
    #xCentroid = xBlack/len(blackPixels)
    #yCentroid = yBlack/len(blackPixels)
    xCentroid = xBlack/len(blackPixels)
    yCentroid = yBlack/len(blackPixels)
    global centroid
    centroid = [xCentroid,yCentroid]
    ### Grid of 16
    win.removeTagged("temp")
    yiqPic.draw(win)
    vert13.draw(win)
    vert14.draw(win)
    vert15.draw(win)
    vert16.draw(win)
    hori4.draw(win)
    hori8.draw(win)
    hori12.draw(win)
    hori16.draw(win)

    #learningToPhoto()
    #print(blackPixels)
    print("mass of centroid", len(blackPixels))
    print("AVERAGE X VALUE", xBlack/len(blackPixels) )
    print("AVERAGE Y VALUE", yBlack/len(blackPixels) )
    win.draw(Circle((xCentroid,yCentroid),5))

def goToPoint():
    testerForDirection = False
    if globalClickY >= 0 and globalClickY < 66.5:
        motors(1,1)
        wait(1)
        learningToPhoto()
        if globalClickY == centroid[0] or globalClickX == centroid[0]:
            print("I work!")
            stop()
       
    if globalClickY >= 66.5 and globalClickY < 133:
        filler
    if globalClickY >= 133 and globalClickY < 99.5:
        filler
    if globalClickY >= 199.5 and globalClickY < 266:
        filler
    if globalClickX >= 0 and globalClickX < 106.75:
        filler
    if globalClickX >= 106.75 and globalClickX < 213.5:
        filler
    if globalClickX >= 213.5 and globalClickX < 320.25:
        filler
    if globalClickX >= 320.25 and globalClickX < 427:
        filler
    
    


'''
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
            
    yiqPic.draw(win)            
    #show(yiqPic,"blob_image")
    show(origPic, "original_image")
    #show(printedYIQPic, "GET_GUD")
    xCentroid = xGreen/len(greenPixels)
    yCentroid = yGreen/len(greenPixels)
    yiqpic.draw(win)

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
'''