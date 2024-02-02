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
