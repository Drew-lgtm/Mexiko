from tkinter import *
import Mexiko

def single():
    global sp
    sp = Toplevel(root)
    sp.title("Single Player")
    sp.geometry("400x500")

                
def multi():
    global MP
    mp = Toplevel(root)
    mp.title("Multi Player")
    mp.geometry("400x500")

    Label(mp).grid(row = 0, column = 0)
    Label(mp, text = " ", width = 10).grid(row = 1, column = 0)
    Label(mp, text = "Human", height = 10).grid(row = 1, column = 1)
    Label(mp, text = " ", width = 20).grid(row = 1, column = 2)
    Label(mp, text = "Computer").grid(row = 1, column = 3)
    Label(mp, text = "").grid(row = 2)

    Textbox(mp).grid(row = 3, column = 1) 


def end():
    quit()



root = Tk()
root.title("Welcome to MEXIKO")
root.geometry("400x447")

photo = PhotoImage(file = "mexiko.gif")
Label(root, image = photo, bg = "pink").grid(row = 0, column = 0, sticky = E)

Button(root, text = "Single Player", width = 28, height = 6, bg = "lightblue", fg = "navy", command = single).grid(row = 3, column = 0, sticky = W)
Button(root, text = "Multi Player", width = 27, height = 6, bg = "pink", fg = "navy", command = multi).grid(row = 3, column = 0, sticky = E)
Button(root, text = "Quit", width = 56, height = 2, bg = "black", fg = "white", command = end).grid(row = 4, column = 0, sticky = W)


mainloop()
