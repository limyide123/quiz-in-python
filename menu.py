import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pygame
from tkinter import font
from ttkbootstrap import Style
from quiz_data import quiz_data
import json
import os

point = 0
current_question = 0
score = 0
timer_id = None
initial_timer_seconds = 10
timer_seconds = initial_timer_seconds
user_name = False
menu_frame = None
play_frame = None

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
main_frame.configure(height='800' ,width='600')



def hide_switch_page():
    menu_switch_page.config(bg='#c3c3c3')
    play_switch_page.config(bg='#c3c3c3')
    scoreboard_switch_page.config(bg='#c3c3c3')


def switch_page(lb ,page):
    hide_switch_page()
    lb.configure(bg='#158aff')
    play_sound_button()
    delete_pages()
    page()



def delete_pages():
   for widget in main_frame.winfo_children():
       widget.destroy()



def home_page():
    global name_list
    menu_frame = tk.Frame(main_frame)
    lb = tk.Label(menu_frame , text= ' Welcome to our quiz!')
    lb.place(x=20 , y = 10)
    lb.pack(padx=10 ,pady=20)
    name_list = []
    def get_name():
        name = user_name.get()
        name_list.append(name)
    user_label = tk.Label(menu_frame, text="Enter your name: ")
    user_label.pack()
    global user_name
    user_name = tk.Entry(menu_frame)
    user_name.pack()
    okbutton = ttk.Button(menu_frame, text="OK", command=get_name)
    okbutton.bind('<Button-1>', lambda event: play_sound_button())
    okbutton.pack()
    b1 = ttk.Button(menu_frame , text= ' play (p)' , bootstyle = 'success' , command=lambda:switch_page(play_switch_page,play_page))
    b1.pack()
    b1.bind('<Button-1>', lambda event: play_sound_button())
    menu_frame.pack()


def check_answer_timeout():
   feedback_label_timer.config(text="Time's up!", foreground="red")
   for button in choice_btns:
       button.config(state="disabled")
        
   next_btn.config(state=tk.NORMAL)
   play_sound_times_up()
   messagebox.showinfo("Timeout", "Time's up! Please move to the next question.")


def update_timer_label():
   timer_label.config(text="Time: {}s".format(timer_seconds))


def update_timer():
   global timer_id
   global timer_seconds
   timer_seconds -= 1
  
   if timer_seconds < 0:
       timer_seconds = 0

   update_timer_label()
  
   if timer_seconds > 0:
       timer_id = play_frame.after(1000, update_timer)
   else:
       check_answer_timeout()


def start_timer():
   global timer_id
   global timer_seconds
   timer_seconds = initial_timer_seconds
   update_timer_label()

   if timer_id is not None:
       play_frame.after_cancel(timer_id)
    
   timer_id = play_frame.after(1000, update_timer)


def reset_timer(new_question=False):
    global timer_id
    global timer_seconds

    if new_question:
        timer_seconds = initial_timer_seconds
        update_timer_label()
        feedback_label_timer.config(text="")  
        next_btn.config(state=tk.NORMAL)  

        
        if timer_id is not None:
            play_frame.after_cancel(timer_id)


        start_timer()


def show_question():
   question = quiz_data[current_question]
   qs_label.config(text=question["question"])

   choices = question["choices"]
   for i in range(4):
       choice_btns[i].config(text=choices[i], state="normal") 

   feedback_label.config(text="")
   next_btn.config(state="disabled")


def check_answer(choice):
    global score
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if(os.path.exists("endtest.txt")):
        score = 0
        os.remove("endtest.txt")

    if timer_id is not None:
        play_frame.after_cancel(timer_id)

    if selected_choice == question["answer"]:
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
        play_sound_correct()
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
        play_sound_wrong()
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")
    reset_timer()


def next_question():
   global current_question
   current_question += 1

   if current_question < len(quiz_data):
       reset_timer(new_question=True) 
       show_question()
   else:
       current_question = 0
       messagebox.showinfo("Quiz Completed",
                           f"Quiz Completed! {','.join(name_list)}, your final score is {score}/{len(quiz_data)}")
       play_frame.destroy()
       update_scoreboard()
       with open("endtest.txt", mode='a'): pass
       #score = 0



def play_page():
 global play_frame
 global feedback_label
 global feedback_label_timer
 global score_label
 global timer_label
 global qs_label

 play_frame = tk.Frame(main_frame)


 qs_label = ttk.Label(play_frame,anchor="center",wraplength=500,padding=10)
 qs_label.pack(pady=10)

 global choice_btns
 choice_btns = []
 for i in range(4):
    button = ttk.Button(play_frame,command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    choice_btns.append(button)


 feedback_label = ttk.Label(play_frame,anchor="center",padding=10)
 feedback_label.pack(pady=10)


 feedback_label_timer = ttk.Label(play_frame,text="",foreground="red",font=("Helvetica", 16))
 feedback_label_timer.pack(pady=10)


 timer_label = ttk.Label(play_frame,text="Time: {}s".format(initial_timer_seconds),anchor="center",padding=10)
 timer_label.pack(pady=10)



 score_label = ttk.Label(play_frame,text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10)
 score_label.pack(pady=10)

 global next_btn
 next_btn = ttk.Button(play_frame,text="Next (n)",command=lambda:next_question(), state="normal")
 next_btn.pack(pady=10)
 next_btn.bind('<Button-1>', lambda event: play_sound_button())



 start_timer()
 
 show_question()
 

 play_frame.pack()


 
def scoreboard_page():
    scoreboard_frame = tk.Frame(main_frame)
    scoreboard_label = tk.Label(scoreboard_frame, text = "This is a scoreboard" , font=("Helvetica", 16,'bold'))
    scoreboard_label.place(x=20 , y = 10)
    scoreboard_label.pack(padx=10 ,pady=(80,40))
    try:
        with open("scoreboard.json", "r") as json_file:
            data = json.load(json_file)
            for user in data['user']:
                message = "User name: " + user['name'] + "\t\t" + "Score: " + str(user['score']) + "\t\t" + "Achievement: " + user['achievement']
                scoreboard_label_2 = tk.Label(scoreboard_frame, text=message, anchor='w', width=600 )                  
                scoreboard_label_2.pack(padx=(80,0))
    except FileNotFoundError:
        scoreboard_label_2 = tk.Label(scoreboard_frame, text="Scoreboard data not found.")
        scoreboard_label_2.pack()
    scoreboard_frame.pack()
 


menu_button = ttk.Button(options_frame , text= 'Home (h)' , command=lambda:switch_page(menu_switch_page,home_page))
menu_button.place(x=20 , y= 20)
menu_button.bind('<Button-1>', lambda event: play_sound_button())
menu_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
menu_switch_page.place(x=3, y=20, width=5, height =40)

play_button = ttk.Button(options_frame , text= ' Play (p)' , command=lambda:switch_page(play_switch_page,play_page))
play_button.place(x=20 , y=80)
play_button.bind('<Button-1>', lambda event: play_sound_button())
play_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
play_switch_page.place(x=3, y=80, width=5, height =40)

scoreboard_button = ttk.Button(options_frame , text= ' Scoreboard (s)' , command=lambda:switch_page(scoreboard_switch_page,scoreboard_page))
scoreboard_button.place(x=20 , y=140)
scoreboard_button.bind('<Button-1>', lambda event: play_sound_button())
scoreboard_switch_page = tk.Label(options_frame, text='', bg='#c3c3c3')
scoreboard_switch_page.place(x=3, y=140, width=5, height =40)


#keyboard shorcut

def key_h(event):
    if root.focus_get() != user_name:
        play_sound_button()
        switch_page(menu_switch_page,home_page)

root.bind("h" , key_h)
root.bind("H", key_h)

def key_p(event):
    if root.focus_get() != user_name:
        play_sound_button()
        switch_page(play_switch_page,play_page)

root.bind("p" , key_p)
root.bind("P", key_p)

def key_s(event):
    if root.focus_get() != user_name:
        play_sound_button()
        switch_page(scoreboard_switch_page,scoreboard_page)

root.bind("s" , key_s)
root.bind("S", key_s)

def key_a(event):
    if choice_btns[0].instate(['!disabled']):
        check_answer(0)
    
root.bind("a", key_a)
root.bind("A", key_a)

def key_b(event):
    if choice_btns[1].instate(['!disabled']):
        check_answer(1)
    
root.bind("b", key_b)
root.bind("B", key_b)

def key_c(event):
    if choice_btns[2].instate(['!disabled']):
        check_answer(2)

root.bind("c", key_c)
root.bind("C", key_c)

def key_d(event):
    if choice_btns[3].instate(['!disabled']):
        check_answer(3)

root.bind("d", key_d)
root.bind("D", key_d)

def key_n(event):
    if next_btn.instate(['!disabled']):
        play_sound_button()
        next_question()

root.bind("n", key_n)
root.bind("N", key_n)

 
#sound#

pygame.mixer.init()

def play_sound_button():
    pygame.mixer.music.load("Button.mp3")
    pygame.mixer.music.play(loops=0)

def play_sound_correct():
    pygame.mixer.music.load("Raziq_correct.mp3")
    pygame.mixer.music.play(loops=0)

def play_sound_wrong():
    pygame.mixer.music.load("Raziq_wrong.mp3")
    pygame.mixer.music.play(loops=0)

def play_sound_times_up():
    pygame.mixer.music.load("Eden_times_up.mp3")
    pygame.mixer.music.play(loops=0)

def update_scoreboard():
    user_exist = False
    if score == 0:
        achievement = "Keep trying! You are the best!"
    elif 10 <= score <= 20:
        achievement = "Good!"
    elif 21 <= score <= 30:
        achievement = "Excellent!!"
    else:
        achievement = "Perfect!"

    
    if(not os.path.exists("scoreboard.json")):
        print("file not exist")
        user_record = {
            "name": name_list[0],
            "score": score,
            "achievement": achievement,
        }
        with open("scoreboard.json", "w") as scoreboard_file:
            scoreboard_file.write("{\n")
            scoreboard_file.write('\"user\": [\n')
            json.dump(user_record, scoreboard_file, indent=4)
            scoreboard_file.write(']\n')
            scoreboard_file.write("}\n")

    else:
        with open("scoreboard.json", "r") as update_file:
            data1 = json.load(update_file)
        for user in data1['user']:
            if name_list[0] == user['name']:
                user_exist = True
                user['score'] = score
                user['achievement'] = achievement
                with open("scoreboard.json", "w") as update_file:
                    json.dump(data1, update_file, indent=4)
        
        if user_exist == False:
            print("file already exists, adding new user")
            new_user = {"name": name_list[0], "score": score, "achievement": achievement}
            with open("scoreboard.json", "r") as bac_file:
                data = json.load(bac_file)
                temp = data["user"]
                temp.append(new_user)
            with open("scoreboard.json", "w") as new_file:
                json.dump(data, new_file, indent=4)
    

#run#

root.mainloop()
