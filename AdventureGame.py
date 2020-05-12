import time
import random

#global var
enemies = ["monster", "vampire", "big python", "lion", "puma", "dragon"]
directions = ["placeholder", "turn right", "turn left", "go straight"]
items = ["sword", "pistol", "stick", "shield", "bow"]
numbers = ["one", "two", "three"]
got_item = False
decisions = []
ways = 0

def print_delay(message):
    print(message)
    time.sleep(2)


def intro():
    print_delay("You wake up confused and alone in a cave. ")
    print_delay("It's dark and nothing is around you. You ask yourself:")
    print_delay("How did i end up here?")
    print_delay("But it's too late now.")


def choice(count):
    if count == 2:
        var = input("Please enter 1 or 2.\n")
        while var != '1' and var != '2':
            var = input("Please enter 1 or 2.\n")

    elif count == 3:
        var = input("Please enter 1 , 2 or 3.\n")
        while var != "1" and var != '2' and var != '3':
            var = input("Please enter 1 , 2 or 3.\n")
    return var


def direction(count):
    print_delay("Which way do you want to go?")
    print_delay("You can either\n")
    if count == 3:
        print_delay(f"1. {directions[1]}")
        print_delay(f"2. {directions[2]}")
        print_delay(f"3. {directions[3]}\n")
    elif count == 2:
        print_delay(f"1. {directions[1]}")
        print_delay(f"2. {directions[2]}\n")


def first_stage(ways):
    if ways == 0:
        print_delay("You want to find the way out of the cave.")
        print_delay("But there are three ways.")
        print_delay("You have to decide.")
        direction(3)

    elif ways == 1:
        print_delay(f"There are two ways left")
        direction(2)
    user_input = int(choice(len(directions)-1))
    check_input = directions[user_input]
    if check_input == "turn right":
        chest_room()

    if check_input == "go straight":
        monster_room()

    if check_input == "turn left":
        lucky_room()


def lucky_room():
    print_delay("You walk through")
    print_delay("It takes forever")
    print_delay("But after 40 minutes of walking, you reach an end")
    print_delay("There is a door")
    last()


def monster_room():
    print_delay(f"So you dediced to go straight")
    directions.remove("go straight")
    print_delay("There is another big room")
    print_delay("You look around, but it's dark")
    print_delay("Suddenly, you hear some noises")
    print_delay("What could it be...")
    sel_enemy = random.choice(enemies)
    print_delay("The noises come closer")
    print_delay("You turn around")
    print_delay(f"There is {sel_enemy} standing in front of you")
    fight(sel_enemy)


def fight(sel_enemy):
    print_delay("You are scared.")
    print_delay("You're shaking")
    global got_item
    global ways
    if got_item is True:
        print_delay("But then you remember.")
        print_delay("You got something to defend yourself")
        ways += 1
        for x in items:
            if x in decisions:
                print_delay(f"You picked up your {x} from your inventory")
                print_delay(f"It's a hard fight but you're\
                            able to defeat the {sel_enemy}")
                print_delay("You are exhausted.")
                print_delay("Blood dripping down your face.")
                print_delay("But you survived")
                print_delay("You look around.")
                print_delay("The whole room suddenly illuminate")
                print_delay("There is a door in the end of the room")
                print_delay("You walk to the door")
                last()
                break

    elif got_item is False:
        print_delay("You can't run away")
        print_delay("There is no escpae")
        print_delay(f"You have to fight the {sel_enemy} with your bare hands")
        print_delay("It's a long and hard fight.")
        print_delay("You tried everything to survive")
        print_delay(f"But the {sel_enemy} is just too strong")
        print_delay(f"You lose")
        print_delay(f"You got DEFEATED")
        end()


def last():
    print_delay("You open the door")
    print_delay("Sunrays are illuminating your face.")
    print_delay("You feel the fresh air")
    print_delay("You found the exit")
    print_delay("GRATULATION")
    end()


def chest_room():
    print_delay(f"So you dediced to turn right")
    directions.remove("turn right")
    print_delay("You find yourself in the middle of a room")
    print_delay("There is a treasure chest")
    print_delay("Do you want to open it?")
    user_input = int(choice(2))
    chest(user_input)


def chest(user_input):
    global ways
    ways += 1
    if user_input == 1:
        print_delay("You open the chest")
        sel_item = random.choice(items)
        decisions.append(sel_item)
        if sel_item != "stick":
            print_delay(f"You got lucky. You find a {sel_item}")
            print_delay("Maybe it can help you through the cave")
            print_delay("There is nothing more to find here")
            print_delay("You decide to turn back ")
            global got_item
            got_item = True

        else:
            print_delay(f"You got unlucky. You find just a stick")
            print_delay("There is nothing more to find here")
            print_delay("You decided to turn back ")

    elif user_input == 2:
        print_delay("You don't want to open the chest")
        print_delay("Maybe it's a trap")
        print_delay("You want to be careful, everything can happend")
        print_delay("There is nothing more to find here")
        print_delay("So you decide to turn back ")

    first_stage(ways)


def play_game():
    intro()
    first_stage(0)


def end():
    print("You want to play the game again?")
    replay = input("Press Y for yes or N for No\n")
    if replay.lower() == "y":
        global directions
        global items
        global numbers
        global ways
        global decisions
        global got_item
        directions.clear()
        directions = ["placeholder", "turn right", "turn left", "go straight"]
        items = ["sword", "pistol", "stick", "shield", "bow"]
        numbers = ["one", "two", "three"]
        got_item = False
        decisions = []
        ways = 0
        play_game()
    elif replay.lower() == "n":
        print("Game will close now")
    else:
        end()


play_game()
