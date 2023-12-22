import numpy as np
import matplotlib.pyplot as plt 
import os
import cv2
import random
import pickle
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.datasets import mnist
from keras.utils import to_categorical

#this is the pathway to my dataset.
DATADIR = "/Users/chazbrowne/Downloads/archive/"
#list of datasets to cycle through in upcoming for loop.
CATEGORIES = ["Chameleon","Crocodile_Alligator","Frog",
              "Gecko","Iguana","Lizard","Salamander","Snake", "Toad", "Turtle_Tortoise"]
#size of the image that will be generated.
IMG_SIZE = 100

#the array where the categorization data will be uploaded. Categorizes species by number. 
training_data =[]
def create_training_data():
#this for loop goes through each "animal" folder
    for category in CATEGORIES:
        #after feeding a file path, it jumps to it, pointing to the first folder/category at that destination
        path = os.path.join(DATADIR, category) #path to reptiles and amphibians
        class_num = CATEGORIES.index(category) #indexes the value based on the section of the folder tht it was found in. 
        for img in os.listdir(path):
            try:
                img1_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                training_data.append([img_array, class_num])
            except Exception as e:
                pass

create_training_data()

image_data = keras.utils.image_dataset_from_directory(DATADIR)

#
#for sample in training_data[:50]:
#    print(sample[1])
#
#x = []
#y = []
#
#for features, label in training_data:
#    x.append(features)
#    y.append(label)
#
#x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
#
#pickle_out = open("x.pickle","wb")
#pickle.dump(x, pickle_out)
#pickle_out.close()
#
#pickle_out = open("y.pickle","wb")
#pickle.dump(y, pickle_out)
#pickle_out.close()