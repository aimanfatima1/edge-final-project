import tkinter as tk
from nltk.corpus import wordnet 
    
window = tk.Tk()
window.title("Dictionary")

canvas1 = tk.Canvas(window, height = 300, width = 400)
canvas1.pack()

# background_image = tk.PhotoImage(file='library.png')
# background_label = tk.Label(root,image=background_image)
# background_label.place(relwidth=1,relheight=1)

# frame = tk.Frame(window,bg='gray',bd=5)
# frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry1 = tk.Entry(window)
canvas1.create_window(200, 140, window = entry1)

def get_word():
    x1 = entry1.get()
    syns = wordnet.synsets(x1)
    
    label1 = tk.Label(window , text= syns[0].lemmas()[0].name()) 
    label2 = tk.Label(window, text = syns[0].definition())
    label3 = tk.Label(window, text = syns[0].examples())
    canvas1.create_window(200,170,window = label1)
    canvas1.create_window(200,210,window = label2)
    canvas1.create_window(200,190,window = label3)
    
button = tk.Button(text="Enter",font = 40, command = get_word)
canvas1.create_window(200, 230, window = button) 
               



# lower_frame = tk.Frame(root,bg='grey',bd=10)
# lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

# label = tk.Label(lower_frame,bg='gray')
# label.place(relwidth=1,relheight=1)

window.mainloop()
