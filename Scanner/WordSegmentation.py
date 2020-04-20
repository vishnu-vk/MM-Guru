import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 



def Segment(image):
    
    # grayscale
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #binary
    ret,thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY_INV)

    #dilation
    kernel = np.ones((25,100), np.uint8)
    img_dilation = cv.dilate(thresh, kernel, iterations=1)
    # plt.imshow(img_dilation,cmap="gray")
    # plt.show()
    #find contours
    im,ctrs, hier = cv.findContours(img_dilation.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv.boundingRect(ctr)[0])

    words=[]
    for i, ctr in enumerate(sorted_ctrs):
        
        # Get bounding box
        x, y, w, h = cv.boundingRect(ctr)
        roi = image[y:y+h, x:x+w]
        words.append(roi)
    return words
