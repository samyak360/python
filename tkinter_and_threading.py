# This is the implementation of the tkinter and the threading 

from tkinter import *
import time
import tkinter.messagebox
root=Tk()
import threading
def f():
       i=70
       for i in range(550):
              l.place(x=i ,y=70)
              time.sleep(0.04)
def counter_label():
       l2.config(text=time.ctime())
       l2.after(1000,counter_label)


root.geometry("550x550")
b=Button(root, text="Click me", width=7,height=2,bg='black',fg='white', command=lambda:print("Hello"), font=('arial', 10,'italic'),bd=2)
b.place(x=350, y=10)

# This is the image which will move via threading
img= PhotoImage(file="design.png")
l=Label(root,text="User Name" ,bg="pink", fg="red", font=("calibri",15,"bold"),width=320, height=390, image=img)
l.place(x=70, y=70)
l2=Label(root,bg="yellow", fg="green", font=("aril",10,"bold"),width=20,height=2)
l2.place(x=150, y=10)
counter_label()
b2=Button(root, bg="Black", fg="white", font=("arial", 10,"bold"),command=lambda: l2.destroy(),bd=2,text="Remove timer", width=11, height=2)
b2.place(x=5,y=10)

# This is the message box which pops up to take answer

tkinter.messagebox.showinfo("Window Title","I love to play guitar")
ans=tkinter.messagebox.askquestion("Question"," Do you like to code on animations")
if ans=='yes':
       print("good")
       t=threading.Thread(target=f)
       t.start()
root.mainloop()
