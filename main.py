questions = ("How old is Cyun?:",
             "When did Malaysia gain it's independence?:",
             "Which animal lays the largest eggs:",
             "How many bones are in the human body?:",
             "Which planet in the solar system is the largest?:",
             "What is the first name of Hitler?",
             )

options = (("A. 12" , "B. 17" , "C. 18" , "D. bro is eternal") , 
           ("A. 1954" , "B. 1970" , "C. 1957" , "D. 1980") ,
           ("A. Whale" , "B. Crocodile" , "C. Elephant" , "D. Ostrich") , 
           ("A. 206" , "B. 207" , "C. 208" , "D. 209"),
           ("A. Earth" , "B. Jupiter" , "C. Saturn" , "D. Mars"))

answers = ("C" , "C" , "D" , "A" , "B")

guesses = []

score = 0

question_nums = 0


for question in questions:
    print("------------------------")
    print(question)

    for option in options[question_nums]:
        print(option )
      
    guess = input("Enter answer (A/B/C/D): ").upper()
    guesses.append(guess)

    if guess == answers[question_nums]:
      score += 1  
      print("CORRECT!")
    
    else:
      print("INCORRECT!")
      print(f"{answers[question_nums]} is the correct answer")
    
   
   
     
     
    question_nums +=1


print("------------------")
print("     RESULTS      ")
print("------------------")
    

print("answers:   " , end="")
for answer in answers:
 print(answer , end=" ")
print()

print("guesses:   " , end="")
for guess in guesses:
       print(guess , end=" ")
print()



score = (score / len(questions) * 100)
print(f"Your score is : {score}% ")
