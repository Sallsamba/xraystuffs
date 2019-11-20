#define_model() name is self-explanatory. It's only used once, then the model is saved in the main directory
#score() is a simple evaluation function

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from recognition.data import dataset

#number of classes
n = 10
#load the data
data, test_data, labels, test_labels = dataset()

def define_model():

    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape = (512,)),
        keras.layers.Dense(n, activation='softmax')
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    model.fit(data, labels, epochs = 20, batch_size = 32)

    return model

def score (model):
   return model.evaluate (test_data, test_labels, batch_size = 128)





