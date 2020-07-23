import tkinter as tk
from nltk.corpus import wordnet 

window = tk.Tk()
window.title("Dictionary")

canvas1 = tk.Canvas(window, height = 700, width = 900)
canvas1.pack()

background_image = tk.PhotoImage(file='jp.png')
background_label = tk.Label(window,image=background_image, bg="black")
background_label.place(relwidth=1,relheight=1)

entry1 = tk.Entry(window,bd=5)
canvas1.create_window(450, 165, window = entry1)

photo = tk.PhotoImage(file = "header.png")
label = tk.Label(image = photo, bg = '#aae0fc')
label.pack()
canvas1.create_window(450, 50, window=label)

labelw = tk.Label(text = "Enter your word below:", font = ("Apple Chancery",30) , bg="#abe5fb")
labelw.pack()
canvas1.create_window(450, 120, window = labelw)

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
                
    label1 = tk.Label(window , text= syns[0].lemmas()[0].name(), bg="#9eeaf8", font=("Arial",14) , fg="black") 
    label2 = tk.Label(window, text = syns[0].definition(),bg = "#9cf7ee", font =("Arial",14) , fg="black")
    label3 = tk.Label(window, text = syns[0].examples(),bg="#a3edfa",font =("Arial",14) , fg="black")
    label4 = tk.Label(window, text=set(synonyms),bg = "#a4f3fa",font =("Arial",14) , fg="black")
    label5 = tk.Label(window,text=antonyms,bg = "#a2f8f7",font =("Arial",14) , fg="black")
    
    canvas1.create_window(450,245,window = label1)
    canvas1.create_window(450,330,window = label2)
    canvas1.create_window(450,415,window = label3)
    canvas1.create_window(450,505,window = label4)
    canvas1.create_window(450,590,window = label5)
  
    
def delete():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    
btn = tk.PhotoImage(file="ent.png")

wordlabel = tk.Label(window,text = "Word", font =('Bodoni 72',24), bg="#9eeaf8",fg = "black" )
canvas1.create_window(450,205,window = wordlabel) 

deflabel = tk.Label(window, text = "Definition", font =('Bodoni 72',24), bg="#9eeaf8",fg = "black" )
canvas1.create_window(450,290,window = deflabel)

exlabel = tk.Label(window,text = "Examples", font =('Bodoni 72',24),bg="#a3edfa",fg = "black")
canvas1.create_window(450,375,window = exlabel)

synlabel = tk.Label(window,text = "Synonyms", font =('Bodoni 72',24),bg="#a4f3fa",fg = "black")
canvas1.create_window(450,460,window = synlabel)

antlabel = tk.Label(window,text = "Antonyms",font =('Bodoni 72',24),bg="#a2f8f7",fg = "black")
canvas1.create_window(450,550,window = antlabel)

button1 = tk.Button(image=btn,font = 40, command = get_word,bd=3)
canvas1.create_window(620, 165, window = button1) 

delete1 = tk.PhotoImage(file ="delt.png")

deletebutton = tk.Button(text="Delete text",image = delete1,command = delete, bd=3)
deletebutton.pack()
canvas1.create_window(450, 630,window = deletebutton)



window.mainloop()
