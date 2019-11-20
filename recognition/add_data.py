import os
import shutil

def add_to_database(path,theclass,subclass):

    if theclass in os.listdir("P" ):
        if subclass in os.listdir("P/"+ theclass):
            shutil.copy2(path, "P/"+theclass +"/"+ subclass +"/"+ path)
        else:
            os.makedirs("P/"+theclass + "/" + subclass)
            shutil.copy2(path, "P/"+theclass +"/"+ subclass +"/"+ path)


    else:
        os.makedirs("P/"+theclass)
        os.makedirs("P/"+theclass + "/" + subclass)
        shutil.copy2(path, "P/"+theclass +"/"+ subclass +"/"+ path)
