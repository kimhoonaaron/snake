# Aaron's First script
room1 = "Your in a room with two doors do you want to go left or right?"
room2 = "Your in a room with a monster do you want to fight or smack!"
room3 = "the cake room"
room4 = "bedroom"
room5 = "final room"
is_alive = True
health = 100
if health == 0:
    print("game over")


def get_player_input(input_string):
    player_input = input(input_string)
    player_input = player_input.lower()
    return player_input


def handle_current_room(current_room):
    print(current_room)



handle_current_room(room1)
if get_player_input("Do you want to go left or right?") == "left":
    handle_current_room(room2)
    if get_player_input("You have to run or smack them into tiny bits") == "run":
        print("There is nowhere to run")
        health = health - 20
        handle_current_room(room2)
    elif get_player_input("You have to run or smack them into tiny bits") == "smack":
        print("you find a knife and slice them into tiny bits")
        handle_current_room(room3)
    else:
        print("error error Return to Room Entrance")
        handle_current_room(room2)
elif get_player_input("Do you want to go left or right?") == "right":
    handle_current_room(room3)
else:
    print("error error Return to Room Entrance")
