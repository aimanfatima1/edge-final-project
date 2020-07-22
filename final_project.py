import tkinter as tk
# from tkinter import font
from nltk.corpus import wordnet 

window = tk.Tk()
window.title("Dictionary")

canvas1 = tk.Canvas(window, height = 600, width = 800)
canvas1.pack()


# background_image = tk.PhotoImage(file='library.png')
# background_label = tk.Label(window,image=background_image)
# background_label.place(relwidth=1,relheight=1)

# frame = tk.Frame(window,bg='gray',bd=5)
# frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

# tex = tk.Label(bg = 'pink',text="Dictionary and Thesaurus",font = ('Copperplate',40))
# canvas1.create_window(500, 50,window = tex)
#print(tk.font.families())

entry1 = tk.Entry(window)
canvas1.create_window(400, 200, window = entry1)


photo = tk.PhotoImage(file = "text.gif")
label = tk.Label(image = photo)
label.pack()
canvas1.create_window(400, 50, window=label)

word = tk.PhotoImage(file = "word.gif")
labelw = tk.Label(image = word)
labelw.pack()
canvas1.create_window(400, 160, window = labelw)

def get_word():
    global label1,label2,label3,label4,label5
    
    x1 = entry1.get()
    syns = wordnet.synsets(x1)
    
    synonyms = [] 
    antonyms = [] 
  
    for syn in wordnet.synsets(x1): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
                
    label1 = tk.Label(window , text= syns[0].lemmas()[0].name()) 
    label2 = tk.Label(window, text = syns[0].definition())
    label3 = tk.Label(window, text = syns[0].examples())
    label4 = tk.Label(window, text=set(synonyms))
    label5 = tk.Label(window,text=set(antonyms))
    
    canvas1.create_window(400,250,window = label1)
    canvas1.create_window(400,300,window = label2)
    canvas1.create_window(400,350,window = label3)
    canvas1.create_window(400,400,window = label4)
    canvas1.create_window(400,450,window = label5)
  
  
    
def delete():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    
button1 = tk.Button(text="Enter",font = 40, command = get_word)
canvas1.create_window(400, 500, window = button1) 
               
deletebutton = tk.Button(text="Delete text", command = delete)
deletebutton.pack()
canvas1.create_window(400, 550,window = deletebutton)

# lower_frame = tk.Frame(root,bg='grey',bd=10)
# lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

# label = tk.Label(frame,bg='green')
# label.place(relheight= 500,relwidth=100)

window.mainloop()
