import tkinter as tk
from nltk.corpus import wordnet 
    
h=500
w=600
root = tk.Tk()
# syns = wordnet.synsets(entry.get())
# def test_function():
#     # syns = wordnet.synsets(entry.get())
#     # print(syns[0].name())
#     print(syns[0].lemmas()[0].name())
#     print(syns[0].definition())
    
# def click():
#     entered_text=entry.get()
    
canvas = tk.Canvas(root,height=h,width=w)
canvas.pack()

background_image = tk.PhotoImage(file='library.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='gray',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

# syns = wordnet.synsets(entry.get())
def test_function():
    syns = wordnet.synsets(entry.get())
    # print(syns[0].name())
    print(syns.name())
    # print(syns[0].definition())
    
button = tk.Button(frame, text="Enter",font=40,command=test_function())
button.place(relx=0.7,relheight=1,relwidth=0.3)  
               
# button = tk.Button(frame,text="enter",width=6,command=click()) 




lower_frame = tk.Frame(root,bg='grey',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame,bg='gray')
label.place(relwidth=1,relheight=1)

root.mainloop()
