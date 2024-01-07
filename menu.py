import tkinter as tk
import ttkbootstrap as ttk


root = tk.Tk()
root.title("Quiz App")
root.geometry('600x600')



saya_menu = tk.Menu()
root.config(menu=saya_menu)


b1 = ttk.Button(root , text= ' Play' )
b1.pack(side='left' , padx= 150 , pady= 50)

b2 = ttk.Button(root , text='Quit')
b2.pack( side='left',padx=50 , pady= 50)


#function for our_command

def our_command():
    my_label = tk.Label(root, text='You clicked a dropdown menu').pack()



# creating a file menu

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