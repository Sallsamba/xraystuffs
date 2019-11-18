#Every needed function to calculate the features describing an image
#embeddings return a 512-length array

from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import decode_predictions

model = VGG16(include_top=False, input_shape=(224, 224, 3), pooling='avg')

def preproc (path):
    image = load_img(path, target_size= (224,224))
    image = img_to_array(image)
    image = preprocess_input(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    return image

def embeddings(image):
    return model.predict(image)