import csv
from quiz_data import quiz_data

user = input("Enter yout name: ")

point = 0

for i in range(len(quiz_data)):
    ans = input("Enter your answer: ")

    if ans == "a":
        point += 1
    else:
        point = point


def achievement():
    if point == 0:
        return "Keep trying! You are the best!"
    elif 1 <= point <= 2:
        return "Good!"
    elif 3 <= point <= 4:
        return "Excellent!!"
    else:
        return "Perfect!"


x = achievement()


with open("scoreboard.csv",'a', newline="") as scoreboard:
    scoreboardlist = csv.writer(scoreboard)
    scoreboardlist.writerow([f"{user}"])
    scoreboardlist.writerow([f"{user}, your final score is {point}"])
    scoreboardlist.writerow([f"Achievement: {x}"])
