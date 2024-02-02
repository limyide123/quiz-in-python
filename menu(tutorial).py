import tkinter as tk


def switch_page(lb ,page):
    lb.configure(bg='#158aff')
    delete_pages()
    page()



def home_page():
    
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame , text= 'this is page one')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    b1 = ttk.Button(menu_frame , text= 'go' , bootstyle = 'success' , command=lambda:(play_page))
    b1.pack()
    menu_frame.pack()


def play_page():

  play_frame = tk.Frame(main_frame)
  lb = tk.Label(play_page , text= 'this is page two')
  lb.place(x=20 , y = 10)
  lb.pack()
  b1 = ttk.Button(menu_frame , text= 'back' , bootstyle = 'success' , command=lambda:(home_page))
  b1.pack()
  play_frame.pack()
 

 
 

 play_frame.pack()






def delete_pages():
   for widget in main_frame.winfo_children():
       widget.destroy()

root.title("switch frames")
root.geometry('800x600')
options_frame = tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(height='800' , width='100')


main_frame = tk.Frame(root , highlightbackground='black' ,highlightthickness='2')
main_frame.pack(side=LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height='800' ,width='600')
menu_button = ttk.Button(options_frame , text= 'Home (h)' , command=lambda:(home_page))
menu_button.place(x=20 , y= 20)


play_button = ttk.Button(options_frame , text= ' Play (p)' , command=lambda:(play_page))
play_button.place(x=20 , y=80)

root.mainloop()
