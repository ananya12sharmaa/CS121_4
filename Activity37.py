import time, random, os

room_items_dictionary = {"1": "key", "2": "candle"}
inventory_list = []
items_list = ["key", "candle"]

def main():
    choice = play_game()
    start_time=time.time()
    while True:
        get_time(start_time, time.ctime())
        if choice == "1":
            choice = enter_porch()
        elif choice == "2":
            choice = enter_entryway()
        elif choice == "3":
            choice = enter_kitchen()
        elif choice == "4":
            choice = enter_diningroom()
        elif choice == "5":
            choice = enter_livingroom()
        else:
            break
    print("Thanks for playing!\nGOODBYE!")

def play_game():
    # use triple quotes for multiline strings
    print("""
    Hello and welcome to the Adventure House!
    In each room, you will be told which directions you can go.
    You can move N (north), S (south), E (east), or W (west) by
    typing the upper or lower case letter.
    Type 'Q' to end the program.
    Type 'S' to start the game!""")
    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["S", "Q"]:
            break
        else:
            print("Please enter a valid choice: 'S' or 'Q'\n")
    if choice == "S":
        return "1"
    else:
        return "Q"

def print_room_header(room):
    line = '=' * 25
    print(f"\n{line}{room}{line}")

def check_inventory():
    global inventory_list, items_list
    if set(inventory_list) == set(items_list):
        print("\n\nCongratulations! You've found all the items! YOU WIN!")
        os._exit(0)

def enter_porch():
    global room_items_dictionary, inventory_list
    print_room_header("Porch")
    print("""
    You are on the porch of a frightening looking house.
    The windows are broken. It's a dark and stormy night.
    You can go N into the house. If you dare.\n
    Your options:
    Press 'N' to enter the house
    Press 'Q' to qus
    it the game\n""")
    option = input('Select "L" to leave or "S" to search the room.\n>> ').upper()
    if option == "S":
        if "1" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("1")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["1"]
                check_inventory()
            else:
                print("You didn't find any items.")
        else:
            print("""No items in the room.
                  Where do u wanna do now? """)
    elif option == "L":
        print("You decide not to search the porch.")
    else:
        print("Invalid option. Please select 'L' to leave or 'S' to search.\n")

    while True:
        choice = input("""Enter your choice-\nYou can either go north(N) or quit(Q)\n>> """).upper()
        if choice in ["N","Q"]:
            break
        else:
            print("Please enter a valid choice\n")
    if choice == "N":
        return "2"
    else:
        return "Q"

def enter_entryway():
    global room_items_dictionary, inventory_list
    print_room_header("Entryway")
    print("""
    You are in the entryway of the house. There are cobwebs in the corner.
    You feel a sense of dread.
    There is a passageway to the N and another to the E.
    The porch is behind you to the S.\n""")
    option = input('Select "L" to leave or "S" to search the room.\n>> ').upper()
    if option == "S":
        if "2" in room_items_dictionary:
            print("Searching room...")
            time.sleep(2)
            if random.randint(1, 2) == 1:
                item = room_items_dictionary.get("2")
                print(f"You found a {item}")
                inventory_list.append(item)
                del room_items_dictionary["2"]
                check_inventory()
            else:
                print("You didn't find any items")
        else:
            print("No items in the room.")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "N", "S", "E"]:
            if choice == "N":
                print("The door is locked...")
                time.sleep(2)
                if "key" in inventory_list:
                    print("You use the key to unlock the door")
                    time.sleep(2)
                    break
                else:
                    print("You can't open the door")
            elif choice == "E":
                print('The door is locked.\nSuddenly a voice speaks:\n\
                "To proceed you must answer this riddle..."')
                time.sleep(2)
                print('"The room contains a match, a kerosene lamp, a candle, and a fireplace.\n\
                What would you light first?"')
                answer = input("Your answer:\n>> ").lower()
                if answer in ["match", "the match", "a match", "matches"]:
                    print('The voice says: "Correct. You may proceed!"\n')
                    print("You open the door and enter the next room...")
                    time.sleep(2)
                    break
                else:
                    print('The voice says: "Incorrect. You may not pass".\n')
                    time.sleep(2)
            else:
                break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "3"
    elif choice == "S":
        return "1"
    elif choice == "E":
        return "5"
    else:
        return "Q"

def enter_kitchen():
    print_room_header("Kitchen")
    print("""
    You are in the kitchen.
    All the surfaces are covered with pots, pans, pieces of food, and pools of blood.
    You think you hear something up the stairs that go up the west side of the room.
    It's like a scraping noise, like something being dragged along the floor.
    You can go to the S or to the E.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "S","E"]:
            if choice == "E":
                print('The door is locked. Suddenly, a voice speaks:')
                print('"To proceed, you must answer this riddle..."')
                time.sleep(2)
                print("""
                I’m tall when I’m young, and I’m short when I’m old.
                What am I?
                """)
                answer = input("Your answer:\n>> ").strip().lower()
                if answer in ["candle", "a candle", "the candle"]:
                    print('The voice says: "Correct. You may proceed."')
                    print("You open the door and step forward...")
                    time.sleep(2)
                    break
                else:
                    print('The voice says: "Incorrect. You may not pass."')
            else:
                break
        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "2"
    elif choice == "E":
        return "4"
    else:
        return "Q"

def enter_diningroom():
    print_room_header("Dining Room")
    print("""
    You are in the dining room.
    There are couches, chairs, and small tables.
    There are remains of a meal on the table.
    You can't tell what it is and maybe don't want to.
    Was that a thump to the west?
    You can go S or W.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "S", "W"]:
            if choice == "S":
                print('The door is locked. Suddenly, a voice speaks:')
                print('"To proceed, you must answer this riddle..."')
                time.sleep(2)
                print("""
                What has keys but can't open locks?
                """)
                answer = input("Your answer:\n>> ").lower()
                if answer in ["piano", "a piano", "the piano"]:
                    print('The voice says: "Correct. You may proceed."')
                    print("You open the door and step forward...")
                    time.sleep(2)
                    break
                else:
                    print('The voice says: "Incorrect. You may not pass."')
            else:
                break

        else:
            print("You can't go that way.\n")
    if choice == "S":
        return "5"
    elif choice == "W":
        return "3"
    else:
        return "Q"

def enter_livingroom():
    print_room_header("Living Room")
    print("""
    You are in a living room. There are couches, chairs, and small tables.
    Everything is covered in dust and spider webs.
    You hear a crashing noise in another room.
    You can go N or W.\n""")
    while True:
        choice = input("Which direction?\n>> ").upper()
        if choice in ["Q", "N", "W"]:
            break
        else:
            print("You can't go that way.\n")
    if choice == "N":
        return "4"
    elif choice == "W":
        return "2"
    else:
        return "Q"

def get_time(start_time, current_time):
    minutes=1
    time_allowed=minutes*60
    if current_time>= start_time + time_allowed:
        print("\nSorry, out of time\nGame over\nYou lose")
        os.exit(0)
    seconds_left=int(time_allowed-(time.time()- start_time)) % 60 
    minutes = seconds_left // 60
    seconds = seconds_left % 60
    print(f"Time remaining: {minutes:02}:{seconds:02}")

main()