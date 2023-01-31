def hint_username(username):
    if len(username) < 3:
        print(username+ " is invalid username. Must have atleast 3 characters.")
    elif len(username) > 15:
        print(username+ " is invalid username. Must have atmost 15 characters.")
    else:
        print(username+ " is valid username")

hint_username("Yu")
hint_username("Lee")
hint_username("zen wong")
hint_username("Lavisontazeungmiyuthong")