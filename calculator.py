from tkinter import *
def click(event):
    global screen
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if screen.get().isdigit():
            value=int(screen.get())
        else:
            value=eval(screens.get())
        screen.set(value)
        screen.update()

    elif text=="C":
        screen.set("")
        screen.update()

    else:
        screen.set(screen.get() + text)
        screens.update()

root = Tk()
root.geometry("300x600")
root.title("calculator")
screen=StringVar()
screen.set("")


screens=Entry(root, textvar=screen,font="lucide 30 bold")
screens.pack(fill=X,padx=10,pady=10)

f=Frame(root)
b=Button(f,text="9",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
 
b=Button(f,text="7",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root)
b=Button(f,text="6",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
 
b=Button(f,text="4",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root)
b=Button(f,text="3",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
 
b=Button(f,text="1",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root)
b=Button(f,text="0",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
 
b=Button(f,text="-",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root)
b=Button(f,text="*",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="/",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
 
b=Button(f,text="=",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root)
b=Button(f,text="%",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text=".",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
 
b=Button(f,text="C",font="lucida 25 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()



root=mainloop()