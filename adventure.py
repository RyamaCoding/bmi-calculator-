print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
user_input = input('You\'re at a cross Road. Where do you want to go? Type "left" or "right"').lower()

if (user_input == "left"):
     lake_choice = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
     if (lake_choice == "wait"):
          door_choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?').lower()
          if (door_choice == "red"):
               print("You are burned by fire. Game over.")
          elif (door_choice == "yellow"):
                print("Congratulations. You have found the treasure!")
          elif (door_choice == "blue"):
                print("You are eaten by beasts. Game over.")
          else: print("You chose a door that doesn't exist. Game over.") 
     elif (lake_choice == "swim"):
          print("You are attacked by trout. Game over.")
     else: 
          print("You chose an option that doesn't exist and get swallowed by a hole. Game over.")
elif (user_input == "right"):
     print("You run into a river and get swallowed up by the stream. Game over.")
else: print("You chose an option that doesn't exist and get swooped by an Eagle. Game over.")
     
