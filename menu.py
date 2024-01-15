import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pygame
from tkinter import font
from ttkbootstrap import Style
from quiz_data import quiz_data

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
  

    menu_frame.pack()



def play_page():
 play_frame = tk.Frame(main_frame)
 
 def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
 def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Cancel the timer when an answer is selected
    if timer_id is not None:
        root.after_cancel(timer_id)

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")
    reset_timer()

# Function to move to the next question
 def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        reset_timer(new_question=True)  # Reset the timer for a new question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()


 initial_timer_seconds = 10
 timer_seconds = initial_timer_seconds
 timer_id = None  


 def start_timer():
    global timer_id
    global timer_seconds
    timer_seconds = initial_timer_seconds
    update_timer_label()

    if timer_id is not None:
        root.after_cancel(timer_id)

    
    timer_id = root.after(1000, update_timer)


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
        timer_id = root.after(1000, update_timer)
    else:
        check_answer_timeout()


 def check_answer_timeout():
    feedback_label_timer.config(text="Time's up!", foreground="red")
    for button in choice_btns:
        button.config(state="disabled")
        
    next_btn.config(state=tk.NORMAL)
    messagebox.showinfo("Timeout", "Time's up! Please move to the nex question.")


 def reset_timer(new_question=False):
    global timer_id
    global timer_seconds

    if new_question:
        timer_seconds = initial_timer_seconds
        update_timer_label()
        feedback_label_timer.config(text="")  
        next_btn.config(state=tk.NORMAL)  

        
        if timer_id is not None:
            root.after_cancel(timer_id)


        start_timer()



 qs_label = ttk.Label(play_frame,anchor="center",wraplength=500,padding=10)
 qs_label.pack(pady=10)


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


 score = 0


 score_label = ttk.Label(play_frame,text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=10)
 score_label.pack(pady=10)


 next_btn = ttk.Button(play_frame,text="Next",command=next_question, state="normal")
 next_btn.pack(pady=10)


 current_question = 0
 start_timer()
 show_question()


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
    







    







    







