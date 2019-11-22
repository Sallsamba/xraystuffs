from recognition.predict import predict
from recognition.predict import decode
from credit.credit import credit
from scraping.extract import extract
import tkinter as tk
import tkinter.filedialog


cour = "{courier new} 12 bold "
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
final_prop = tk.StringVar()

def format_features(path):
    try:
        Category,Version, Price = extract(decode(predict(path)))

        final_str.set("Votre objet a été reconnu !\n\n Il s'agit d'un(e) {}.\n\n {} \n\nPrix (en €) : {}".format(Category, Version, Price))

    except:
        final_str.set('objet non reconnu :-(')
    
    
    

def format_image(path):
    imname = decode(predict(path))
    final_img = tk.PhotoImage(file  = "dbutils/"+str(imname)+".png")
    
    image_label.configure(image = final_img)
    image_label.image =final_img

def format_prop(path):
    try:
        Price = extract(decode(predict(path)))[2]
        if credit(int(Price)) != False:

            final_prop.set("Pour acheter cet objet, la BNP Paribas vous propose de payer en plusieurs fois!\n"+credit(int(Price)))
    except:
        final_prop.set("Cet objet est peut-être un peu trop cher pour votre budget.")

    

def format_total(path):
    format_image(path)
    format_features(path)
    format_prop(path)


#canvas for my whole window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='GUI/landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


#frame to for the Entry and the Buttons
frame = tk.Frame(root, bg='green', bd=5)
frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.05)

entry = tk.Entry(frame, font = cour, textvariable = entryText)
entry.place(relwidth=0.55, relheight=1)

browse = tk.Button(frame, text="Browse", font = cour, command=lambda: browsefunc())
browse.place(relx=0.61, relheight=1, relwidth=0.1)

button = tk.Button(frame, text="Enter", font = cour, command=lambda: format_total(entry.get()))
button.place(relx=0.72, relheight=1, relwidth=0.28)
#end of the frame

#frame for the image
image_frame = tk.Frame(root, bg='green', bd=2)
image_frame.place(relx=0.05, rely=0.25, relwidth=0.5, relheight=0.5)

image_label = tk.Label(image_frame)
image_label.place(relwidth=1, relheight=1)
#end of the frame

#frame for the prediction and features of the object
pred_frame = tk.Frame(root, bg='green', bd=2)
pred_frame.place(relx=0.57, rely=0.4, relwidth=0.38, relheight=0.2)

pred_label = tk.Label(pred_frame, textvariable = final_str, font = cour)
pred_label.place(relwidth=1, relheight=1)
#end of the frame


#frame for the financial proposal
fin_frame = tk.Frame(root, bg='green', bd=2)
fin_frame.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

fin_label = tk.Label(fin_frame, textvariable = final_prop, font = cour)
fin_label.place(relwidth=1, relheight=1)
#end of the frame

root.mainloop()