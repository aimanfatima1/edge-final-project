import tkinter as tk

h=500
w=600
root = tk.Tk()

def test_function():
    print("Button clicker")
    
canvas = tk.Canvas(root,height=h,width=w)
canvas.pack()

background_image = tk.PhotoImage(file='library.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)
