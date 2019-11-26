#Old Learning to Photo#
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
        #wait(5)
        #origPic = camera.takePicture()
    yuvValues = []
    yiqPic = Picture(origPic)
    joshPic = Picture(origPic)
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
            
            joshPic.setRGB(x,y,yiqValues[0],yiqValues[1],yiqValues[2])
            yiqPixel = yiqPic.getRGB(x,y)
            #printedYIQPic = Picture(yiqPic)
            
            if yiqPixel[0] <= 0.580 and yiqPixel[1] >= 0.043 and yiqPixel[2] >= 0.030:
            #Old YIQ Numbers
            #if yiqPixel[0] <= .299 and yiqPixel[0] >=.066 and yiqPixel[1] <= 0.092  and yiqPixel[2] >= -0.030:
                yiqPic.setRGB(x,y,0,0,0)
                #yiqPic.setRGB(x,y,255,255,255)
                blackPixels.append([x,y])
                xBlack += x
                yBlack += y
            else:
                yiqPic.setRGB(x,y,255,255,255)
                #yiqPic.setRGB(x,y,0,0,0)
                whitePixels.append([x,y])
    #show(pic,"robot_display")
    #show(yiqPic,"blob_image")
    #show(origPic, "original_image")
    #show(I, "original_image")
    #xCentroid = xBlack/len(blackPixels)
    #yCentroid = yBlack/len(blackPixels)
    try:
        xCentroid = xBlack/len(blackPixels)
        yCentroid = yBlack/len(blackPixels)
    except ZeroDivisionError:
        print("Zero Division Error")
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
    show(joshPic, "blob_image")
    #learningToPhoto()
    #print(blackPixels)
    print("mass of centroid", len(blackPixels))
    print("AVERAGE X VALUE", xBlack/len(blackPixels) )
    print("AVERAGE Y VALUE", yBlack/len(blackPixels) )
    win.draw(Circle((xCentroid,yCentroid),5))



    ###
    #Old Messy centroid data#
    ###
    
    #print("mass of centroid", len(blackPixels))
    #print("AVERAGE X VALUE", xBlack/len(blackPixels) )
    #print("AVERAGE Y VALUE", yBlack/len(blackPixels) )