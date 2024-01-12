import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pygame
from tkinter import font
from ttkbootstrap import Style

root = tk.Tk()
root.title("Quiz App")
root.geometry('800x600')

options_frame = tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height='800' , width='100')


main_frame = tk.Frame(root , highlightbackground='black' ,highlightthickness='2')
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height='800' ,width='700')



def indicate(lb ,page):
    lb.configure(bg='#158aff')
    root.after(1, lambda: delete_pages())
    root.after(2, lambda: page())  



def delete_pages():
   for widget in main_frame.winfo_children():
       widget.destroy()



def home_page():
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame , text= ' Welcome to our quiz!')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    b1 = ttk.Button(menu_frame , text= 'Play' , bootstyle= 'success' , command=lambda:indicate(play_page())) 
    b1.pack()

    menu_frame.pack()



def play_page():
    play_frame = tk.Frame(main_frame)
    lb = tk.Label(play_frame , text= ' Welcome to our play!')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    b11 = ttk.Button(play_frame, text='quit' , bootstyle= 'danger'  , command=exit)
    b11.pack()
    play_frame.pack()






    





menu_button = ttk.Button(options_frame , text= 'Home' , command=lambda:indicate(home_page()))
menu_button.place(x=20 , y= 20)


play_button = ttk.Button(options_frame , text= ' Play' , command=lambda:indicate(play_page()))
play_button.place(x=20 , y=80)

scoreboard_button = ttk.Button(options_frame , text= ' Scoreboard')
scoreboard_button.place(x=20 , y=140)

#sound

pygame.mixer.init()

def play():
    pygame.mixer.music.load("sound\quothello-therequot-158832.mp3")
    pygame.mixer.music.play(loops=0)



def our_command():
    pass









root.mainloop()

#frame switching
    







