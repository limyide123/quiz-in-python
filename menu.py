from tkinter import *

root = Tk()
root.title("Quiz App")
root.geometry('600x600')


saya_menu = Menu()
root.config(menu=saya_menu)


#function for our_command

def our_command():
    my_label = Label(root, text='You clicked a dropdown menu').pack()



# creating a file menu

file_menu = Menu(saya_menu)
saya_menu.add_cascade(label='File' , menu=file_menu)
file_menu.add_command(label='New' , command=our_command)
file_menu.add_separator()
file_menu.add_command(label='Exit' ,  command=root.quit)


#creating an edit menu

edit_menu = Menu(saya_menu)
saya_menu.add_cascade(label='Edit' , menu=edit_menu)
edit_menu.add_command(label='Undo' , command=our_command)
edit_menu.add_command(label='Redo' , command=our_command)







root.mainloop()
