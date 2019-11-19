import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from recognition.data import dataset

#add all used classes, with the order corresponding to the mapping
class_names = ["ferrari", "jeep", "renault clio" ]
n = 10
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





