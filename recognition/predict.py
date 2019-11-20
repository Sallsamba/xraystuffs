#Predict the class of an image. 
#Input : the path of the image. 
#Output : An array P of probabilities. P[i] is the probabilty that the image is an "i"

from recognition.embeddings import embeddings
from recognition.embeddings import preproc
import tensorflow as tf

model = tf.keras.models.load_model("model.h5")

def predict(path):
    image= preproc(path)
    image = embeddings(image)
    return model.predict(image)