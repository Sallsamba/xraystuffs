from recognition.predict import predict
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

def format_features(path):
    try:

        Category = ""
        Version = ""
        Price = ""
        final_str = 'Catégorie: %s \nVersion: %s \nPrix : %s' % (Category, Version, Price)

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str

def format_image(path):
    try:
        final_img = tk.PhotoImage(file  = path)
        final_img = ""
    except:
        return None
    return final_img


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

button = tk.Button(frame, text="Enter", font = cour, command=lambda: test_function(entry.get()))
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

pred_label = tk.Label(pred_frame)
pred_label.place(relwidth=1, relheight=1)
#end of the frame


#frame for the financial proposal
fin_frame = tk.Frame(root, bg='black', bd=10)
fin_frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

fin_label = tk.Label(fin_frame)
fin_label.place(relwidth=1, relheight=1)
#end of the frame

root.mainloop()