import cv2 as cv
import numpy as np


def Segment(image):
    
    #grayscale
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

    #binary
    ret,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)

    #dilation
    kernel = np.ones((5,5), np.uint8)
    img_dilation = cv.dilate(thresh, kernel, iterations=1)

    hp=img_dilation
    hp[img_dilation == 0]   = 0
    hp[img_dilation == 255] = 1
    horizontal_projection = np.sum(hp, axis = 1)

    sP=None
    eP=None

    lines=[]

    for i in range(len(horizontal_projection)):
        if(not(horizontal_projection[i]==0) and sP==None):
            sP=i
        elif(horizontal_projection[i]==0 and not(sP==None)):
            eP=i
            lines.append((sP,eP))
            sP=None
        else:
            pass

    op=[]
    for line in lines:
        if(image.shape[1]*(line[1]-line[0])>100000):
            crop_img = image[line[0]:line[1], 0:image.shape[1]]
            op.append(crop_img)
    return op
