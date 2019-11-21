from recognition.predict import predict
from recognition.predict import decode
#from scraping.extract import *
import tkinter as tk
import tkinter.filedialog

cour = "{courier new} 14 bold italic"
HEIGHT = 1000
WIDTH = 1000



def test_function(entry):
    print("This is the entry:", entry)

def browsefunc():
    filename = tkinter.filedialog.askopenfilename()
    entryText.set (filename)

root = tk.Tk()
root.title ("BNP Object Recognition")
root.resizable(0,0)
entryText = tk.StringVar()  
final_str = tk.StringVar()

def format_features(path):
    try:
        #Name,Category, Version, Price = extract(decode(predict(path)))
        Name = "Name"
        Category = "Catégorie"
        Version = "Version"
        Price = "Price"

        final_str.set("Votre objet a été reconnu !\n Il s'agit d'un {}.\nCatégorie: {} \nVersion: {} \nPrix : {}".format(Name, Category, Version, Price))

    except:
        final_str.set('There was a problem retrieving the informations')
    
    pred_label.configure (textvariable = final_str)
    print(final_str)

def format_image(path):
    imname = decode(predict(path))
    final_img = tk.PhotoImage(file  = "dbutils/"+str(imname)+".png")
    
    image_label.configure(image = final_img)
    image_label.image =final_img
    

def format_total(path):
    format_image(path)
    format_features(path)


#canvas for my whole window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='GUI/landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


#frame to for the Entry and the Buttons
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.05)

entry = tk.Entry(frame, font = cour, textvariable = entryText)
entry.place(relwidth=0.55, relheight=1)

browse = tk.Button(frame, text="Browse", font = cour, command=lambda: browsefunc())
browse.place(relx=0.61, relheight=1, relwidth=0.1)

button = tk.Button(frame, text="Enter", font = cour, command=lambda: format_total(entry.get()))
button.place(relx=0.72, relheight=1, relwidth=0.28)
#end of the frame

#frame for the image
image_frame = tk.Frame(root, bg='gray', bd=10)
image_frame.place(relx=0.05, rely=0.25, relwidth=0.5, relheight=0.5)

image_label = tk.Label(image_frame)
image_label.place(relwidth=1, relheight=1)
#end of the frame

#frame for the prediction and features of the object
pred_frame = tk.Frame(root, bg='blue', bd=10)
pred_frame.place(relx=0.6, rely=0.25, relwidth=0.35, relheight=0.5)

pred_label = tk.Label(pred_frame, textvariable = final_str, font = cour)
pred_label.place(relwidth=1, relheight=1)
#end of the frame


#frame for the financial proposal
fin_frame = tk.Frame(root, bg='black', bd=10)
fin_frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

fin_label = tk.Label(fin_frame)
fin_label.place(relwidth=1, relheight=1)
#end of the frame

root.mainloop()