from tkinter import *

def doSomething(event):

    #print("You pressed: " + event.keysym)
    #print("Mouse coordinates: " + str(event.x)+","str(event.y))

    label.config(text=event.keysym)

window = Tk()

#window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething) #left mouse click
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<"Leave>,doSomething) #leave the window
#window.bind("<Motion>",doSomething) #where the mouse moved

window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica", 100))
label.pack()

window.mainloop()
