#This file contains the function responsible for testing the model using a non filtered wav file to detect the speech emotion

import os
import wave
import pickle
from sys import byteorder
from array import array
from struct import pack
from sklearn.neural_network import MLPClassifier

from utils import extract_feature
import speech_recognition as sr

def result(Id,filename):
    # load the saved model (after training)
    model = pickle.load(open("C:\\Users\\user\\python\\result_test\\mlp_classifier.model", "rb"))
    # extract features and reshape it
    features = extract_feature(filename, mfcc=True, chroma=True, mel=True).reshape(1, -1)
    # predict
    result = model.predict(features)[0]
    # show the result !
    print("id:", Id)
    print("result:", result)
    return result