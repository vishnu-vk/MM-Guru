import cv2 as cv
import numpy as np


def Segment(image):
    # grayscale
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

    # binary
    ret,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)
    # find contours and their hierarchies
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    chrs_and_pos=[]
    # to fill black colours in the contours 
    for i,cnt in enumerate(contours):
        HI=hierarchy[0][i].tolist()

        # to remove the noise with area less than 100
        if(cv.contourArea(cnt)>100 and HI[3]==-1):
            drawing = 255 * np.ones(image.shape, np.uint8)
            cv.fillPoly(drawing, pts =[cnt], color=(0,0,0))

            # to fill white colours to the inner contours
            for j,conts in enumerate(contours):
                H=hierarchy[0][j].tolist()
                if(H[3]==i):
                    cv.fillPoly(drawing, pts =[conts], color=(255,255,255))
            x,y,w,h=cv.boundingRect(cnt)
            crop_img=drawing[y:y+h, x:x+w]
            chrs_and_pos.append((crop_img,(x,y,w,h)))

    chrs_and_pos = sorted(chrs_and_pos,key=lambda entry: entry[1][0])
    characters=[ i[0] for i in chrs_and_pos ]

    return characters
