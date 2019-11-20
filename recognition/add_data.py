import os
import shutil

def add_to_database(path,theclass,subclass):

    if theclass in os.listdir("database" ):
        if subclass in os.listdir("database/"+ theclass):
            shutil.copy2(path, "database/"+theclass +"/"+ subclass +"/"+ path)
        else:
            os.makedirs("database/"+theclass + "/" + subclass)
            shutil.copy2(path, "database/"+theclass +"/"+ subclass +"/"+ path)


    else:
        os.makedirs("database/"+theclass)
        os.makedirs("database/"+theclass + "/" + subclass)
        shutil.copy2(path, "database/"+theclass +"/"+ subclass +"/"+ path)
