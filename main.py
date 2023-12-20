questions = (
    "How old is Cyun?:",
    "When did Malaysia gain it's independence?:",
    "Which animal lays the largest eggs:",
    "How many bones are in the human body?:",
    "Which planet in the solar system is the largest?:",
    "What is the longest word in the English language?",
    "What is the name of the world’s smallest horse?",
    "What is Benedictine monk Dom Pierre Pérignon rumored to have created?",
    "Which country drinks the most amount of coffee per person?",
    "What is the collective name for a group of unicorns?",
    "What is the most common color of toilet paper in France?",
    "How many years old is the world’s oldest piece of chewing gum?",
    "How many times per day does the average American open their fridge?",
    "What color is an airplane’s famous black box?",
    "What is Bombay Duck’s main ingredient?",
    "How many tails does a Manx cat have?",
    "As of July 2023, how many episodes of South Park are there?",
    "In what decade was Madonna born?",
    "In what language is the phrase ‘Hakuna Matata’?",
    "And what is the meaning of ‘Hakuna Matata’?",
    "What is the name of a duel with three people involved?",
    "How many stars are on the United States flag?",
    "In which year was Slido founded?",
    "Who is credited with inventing the World Wide Web?",
    "What type of computer was the first laptop computer?",
    "What is the largest social media network in the world?",
    "Who is considered the founder of modern computer science?",
    "What year was the iPhone first released in?",
    "Which video game console, first released in 2006, was the first to use motion controls during gameplay?",
    "When was eBay founded?",
    "A green owl is the mascot for which app?",
    "In which year did the Berlin Wall fall?",
    "How many times has the Mona Lisa been stolen?",
    "In Ancient Rome, how many days of the week were there?",
    "What was New York’s original name?",
    "In what year did the Titanic sink?",
    "Until 1981, Greenland was a colony of which country?",
    "How many US presidents have been assassinated?",
    "Who was assassinated in New York in 1980?",
    "Who painted The Last Supper?"
)

options = (
    ("A. 12", "B. 17", "C. 18", "D. bro is eternal"),
    ("A. 1954", "B. 1970", "C. 1957", "D. 1980"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
    ("A: Antidisestablishmentarianism", "B: Hippopotomonstrosesquippedaliophobia", "C: Floccinaucinihilipilification", "D: Raziqisveryhandsome"),
    ("A: Falabella", "B: Shetland pony", "C: Miniature horse", "D: My little pony"),
    ("A: Tomato ketchup", "B: Champagne", "C: French fries", "D: Chili sauce"),
    ("A: Finland", "B: Italy", "C: Colombia", "D: Malaysia"),
    ("A: A sparkle", "B: A spell", "C: A herd", "D: A blessing"),
    ("A: Pink*", "B: White", "C: Blue", "D: Rainbow"),
    ("A: 100", "B: 2,500", "C: 4,000", "D: 5,700*"),
    ("A: 5", "B: 22", "C: 33*", "D: 50"),
    ("A: Red", "B: Orange*", "C: Black", "D: Yellow"),
    ("A: Fish*", "B: Duck", "C: Chicken", "D: Curry"),
    ("A: None*", "B: One", "C: Two", "D: Three"),
    ("A: 250", "B: 300", "C: 325*", "D: 400"),
    ("A: 1950s*", "B: 1960s", "C: 1970s", "D: 1980s"),
    ("A: Dutch", "B: Swahili*", "C: Yoruba", "D: German"),
    ("A: No worries*", "B: Goodnight", "C: Thank you", "D: Who cares?"),
    ("A: A triage", "B: A truel*", "C: A tryst", "D: A triangle"),
    ("A: 50*", "B: 51", "C: 52", "D: 53"),
    ("A: 2012*", "B: 2016", "C: 2020", "D: 2021"),
    ("A: Steve Jobs", "B: Bill Gates", "C: Tim Berners-Lee*", "D: Gay-Lussac"),
    ("A: Apple Macintosh", "B: IBM PC", "C: Osborne 1*", "D: Lenovo"),
    ("A: Twitter", "B: Facebook*", "C: Instagram", "D: TikTok"),
    ("A: Alan Turing*", "B: Steve Jobs", "C: Bill Gates", "D: Isaac Newton"),
    ("A: 2007*", "B: 2009", "C: 2010", "D: 2011"),
    ("A: Sega Megadrive", "B: Nintendo Wii*", "C: Playstation", "D: Sony"),
    ("A: 1990", "B: 1995*", "C: 1998", "D: 2001"),
    ("A: Spotify", "B: Tinder", "C: YouTube", "D: Duolingo*"),
    ("A: 1987", "B: 1989*", "C: 1990", "D: 1995"),
    ("A: One*", "B: Five", "C: Eight", "D: Ten"),
    ("A: Five", "B: Six", "C: Seven", "D: Eight*"),
    ("A: New Liverpool", "B: New Amsterdam*", "C: New Brussels", "D: New World"),
    ("A: 1900", "B: 1912*", "C: 1921", "D: 1932"),
    ("A: France", "B: Spain", "C: German", "D: Denmark*"),
    ("A: Three", "B: Four*", "C: Five", "D: Six"),
    ("A: President John F Kennedy", "B: John Lennon*", "C: Gianni Versace", "D: Abraham Lincoln"),
    ("A: Leonardo Da Vinci*", "B: Rembrandt", "C: Michelangelo", "D: Mona Lisa")
)

answers = (
    "C", "C", "D", "A", "B",
    "A", "C", "B", "A", "D",
    "A", "D", "C", "B", "A",
    "A", "C", "A", "B", "A",
    "B", "A", "A", "C", "C",
    "B", "A", "A", "B", "B",
    "D", "B", "A", "D", "B",
    "B", "D", "B", "B", "A"
)

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
