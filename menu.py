import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pygame
from tkinter import font

root = tk.Tk()
root.title("Quiz App")
root.geometry('800x600')

myLabel = ttk.Label(root , text='Welcome to Quiz App!')
myLabel.pack()


#sound

pygame.mixer.init()

def play():
    pygame.mixer.music.load("sound\quothello-therequot-158832.mp3")
    pygame.mixer.music.play(loops=0)



#frame switching
    



greet = tk.Frame(root)
order = tk.Frame(root)


def change_to_greet():
    greet.pack(fill='both' , expand= 1 )
    order.pack_forget()

font1=font.Font(family = 'Georgia' , size = '22' , )

label_greet = tk.Label(greet , text= 'Ready to play!' , foreground= 'green' , font= font1)
label_greet.pack(padx=10 , pady=20)



def change_to_order():
    greet.pack(fill='both' , expand= 1 ,)
    order.pack_forget()
    















b1 = ttk.Button(root , text= ' Play', command= change_to_greet)
b1.pack(side='left' , padx= 150 , pady= 50)

b2 = ttk.Button(root , text='Quit', command= quit)
b2.pack( side='left',padx=50 , pady= 50)


#function for our_command

def our_command():
    my_label = tk.Label(root, text='You clicked a dropdown menu').pack()



# creating a file menu
    

saya_menu = tk.Menu()
root.config(menu=saya_menu)

file_menu = tk.Menu(saya_menu)
saya_menu.add_cascade(label='File' , menu=file_menu)
file_menu.add_command(label='New' , command=our_command)
file_menu.add_separator()
file_menu.add_command(label='Exit' ,  command=root.quit)


#creating an edit menu

edit_menu = tk.Menu(saya_menu)
saya_menu.add_cascade(label='Edit' , menu=edit_menu)
edit_menu.add_command(label='Undo' , command=our_command)
edit_menu.add_command(label='Redo' , command=our_command)







root.mainloop()
