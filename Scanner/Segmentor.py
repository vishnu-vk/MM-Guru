import argparse
import matplotlib.pyplot as plt
import cv2 as cv

from .LineSegmentation import Segment as LS
from .WordSegmentation import Segment as WS
from .CharacterSegmentation import Segment as CS
from .scanFile import predict
# from docx import Document
# from docx.shared import Inches

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
# args = vars(ap.parse_args())


# image = cv.imread(args["image"], cv.IMREAD_UNCHANGED)


def Segment(image):
    text = ""

    #segmentation of document into individual lines
    lines = LS(image)

    #segmetation of lines into individual words
    for i,line in enumerate(lines):
        words = WS(line)

        # segmentation of words into single characters
        for j,word in enumerate(words):
            chrs = CS(word)
            for k,ch in enumerate(chrs):
                text += predict(ch)
            text +="\u0020"
        text +="\u000d"


    return text

    # document = Document()
    # p = document.add_paragraph(text)
    # document.save('demo.docx')




    
