#to modify
import os
import numpy as np
from recognition.embeddings import embeddings
from recognition.embeddings import preproc
from sklearn.model_selection import train_test_split


dic = {'ferrari_portofino':6,'jeep_wrangler':7,'renault_clio':8,
'huawei_p30_pro':3,'iphone_6':4,'iphone_11_pro':5,'canapé_d_angle':0,'canapé_droit':1,'fauteuil':2,}

def load_datac():
    L = os.listdir("P")
    path = 'P/canapé/canapé_d_angle/1.jpg'
    em = embeddings(preproc(path))
    data = np.concatenate((em, np.array([[0]])), axis = 1)

    for classname in L:
        S = os.listdir("P/"+classname)
        for subclass in S:
            for image in os.listdir("P/"+classname+"/"+subclass):
                image = preproc("P/"+classname+"/"+subclass+"/"+image)
                emb = embeddings(image)
                res = np.array([  [dic[subclass]]   ])
                line = np.concatenate((emb, res),axis =1)
                data = np.concatenate ((data, line), axis = 0)
                print("ok")
    return data

def dataset():
    data = np.load("data.npy")
    features = data[:,:-1]
    labels = data[:,len(data[0])-1]
    return train_test_split(features, labels, test_size = 0.1, random_state = 42, shuffle = True)


    