from recognition.embeddings import embeddings
from recognition.embeddings import preproc
import tensorflow as tf

model = tf.keras.models.load_model("model.h5")

def predict(path):
    image= preproc(path)
    image = embeddings(image)
    return model.predict(image)