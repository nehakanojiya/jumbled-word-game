import tkinter
from tkinter import *
import random
from tkinter import messagebox
answers = [ "python" , "java", "swift" , "canada" , "india" , "america" , "london" ]
words = [ "npthoy", "avja" , "tfisw" , "cdanaa" , "aidin" , "aiearcm" , "odnlon" ]
num = random.randrange(0, len(words),1 )
def default() :
    global words,answers,num
    lbl.config(text = words[num])
def res():
    global words,answers,num
    num = random.randrange(0 , len(words) , 1)
    lbl.config(text = words [num])
    e1. delete(0 , END )
def checkans() :
    global words,answers,num
    var = e1.get()
    if  var == answers[num] :
          messagebox.showinfo("sucess" , "This is a correct answer")
          res()
    else:
           messagebox.showerror("error" , "This is not correct")
           e1.delete(0 ,END)
root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("jumbbled")
root.configure(background = "#000000")

lbl = Label(
      root,
      text = "your here",
      font = ("verdana",18),
      bg = "#000000",
      fg = "#FFFFFF",
      )
lbl.pack(pady = 30,ipady = 10, ipadx = 10)
ans1 = StringVar()
e1 = Entry(
     root,
     font = ("verdana",16),
     textvariable = ans1,
     )
e1.pack(ipady=5,ipadx=5)
btncheck = Button(
    root,
    text = "Check",
    font = ("comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans,
    )
btncheck.pack(pady = 40)
btnreset = Button(
    root,
    text = "reset",
    font = ("comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = res,
    )
btnreset.pack()
default()
root.mainloop()
    
  
      
