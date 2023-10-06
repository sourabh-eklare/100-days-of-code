print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

cross_road = input('You\'re at a cross road. Where do you want to go? "left" or "right". ').lower()

if cross_road == "left":
    lake = input('You come at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if lake == "wait":
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
        if door == "yellow":
            print("Congratulations! You found the Treasure. You win.")
        elif door == "blue":
            print("You enter a room of beast. Game over.")
        else:
            print("You enter room of fire. Game over.")
    else:
        print("You did not make it across the lake. Game Over.")
else:
    print("You chose the wrong path. Game Over.")