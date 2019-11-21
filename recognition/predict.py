#Predict the class of an image. 
#Input : the path of the image. 
#Output : An array P of probabilities. P[i] is the probability that the image is an "i"

from recognition.embeddings import embeddings
from recognition.embeddings import preproc
import tensorflow as tf

dic = {'ferrari_portofino':6,'jeep_wrangler':7,'renault_clio':8,
'huawei_p30_pro':3,'iphone_6':4,'iphone_11_pro':5,'canapé_d_angle':0,'canapé_droit':1,'fauteuil':2,}

dico = {0:"Canapé d'angle", 1:"Canapé droit", 2:"Fauteuil", 3:"Huawei P30 Pro", 4:"Iphone 6",5:"Iphone 11 Pro", 6:"Ferrari Portofino",
7:"Jeep Wrangler", 8:"Renault Clio"}

model = tf.keras.models.load_model("model.h5")

def predict(path):
    image= preproc(path)
    image = embeddings(image)
    return model.predict(image)

def decode(prediction):
    for i in range(len(prediction[0])):
        if prediction[0][i] > 0.9:
            return i
    
    return False