import tkinter as tk
from nltk.corpus import wordnet 
    
window = tk.Tk()
window.title("Dictionary")

canvas1 = tk.Canvas(window, height = 1000, width = 1000)
canvas1.pack()

# background_image = tk.PhotoImage(file='library.png')
# background_label = tk.Label(root,image=background_image)
# background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(window,bg='gray',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry1 = tk.Entry(window,height=20,width=30)
canvas1.create_window(200, 300, window = entry1)

def get_word():
    global label1,label2,label3
    
    x1 = entry1.get()
    syns = wordnet.synsets(x1)
    
    label1 = tk.Label(window ,bg='pink', text= syns[0].lemmas()[0].name()) 
    label2 = tk.Label(window, text = syns[0].definition())
    
    label3 = tk.Label(window, text = syns[0].examples())
    canvas1.create_window(250,170,window = label1)
    canvas1.create_window(250,210,window = label2)
    canvas1.create_window(250,190,window = label3)
    
def delete():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    


button = tk.Button(text="Enter",font = 40, command = get_word)
canvas1.create_window(200, 230, window = button) 
               
deletebutton = tk.Button(window, text="Delete text", command = delete)
deletebutton.pack()


# lower_frame = tk.Frame(root,bg='grey',bd=10)
# lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

# label = tk.Label(frame,bg='green')
# label.place(relheight= 500,relwidth=100)

window.mainloop()
