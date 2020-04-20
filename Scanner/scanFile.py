import argparse
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
import csv
import operator
from keras.models import load_model

from .functions import clean, read_transparent_png

from .classesFile import classes

        
model = load_model("./Scanner/model.h5")
    
def predict(img):
    image_data = clean(img)
    dataset = np.asarray(image_data)
    dataset = dataset.reshape((-1, 32, 32, 1)).astype(np.float32)
    a = model.predict_classes(dataset)
    return classes[int(a)]







