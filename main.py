import random

while True:
 possible_actions = ["Rock", "Paper", "Scissors"]
 user_action = input("Make a choice : \n R for Rock, \n P for Paper, and \n S for Scissors \n Your Choice: ")
 computer_action = random.choice(possible_actions)
 if user_action == 'R':
        users_choice = possible_actions[0]
        print(f"\nPlayer ({users_choice}) : CPU ({computer_action})\n") 
 elif user_action == 'P':
        users_choice = possible_actions[1]
        print(f"\nPlayer ({users_choice}) : CPU ({computer_action})\n")
 elif user_action == 'S':
        users_choice = possible_actions[2]
        print(f"\nPlayer ({users_choice}) : CPU ({computer_action})\n")
 elif user_action != "R" or user_action != "Paper" or user_action != "Scissors":
        print('Invalid input')
        user_action = input("Make a choice : \n R for Rock, \n P for Paper, and \n S for Scissors \n Your Choice: ")
 if users_choice == computer_action:
    print(f"Both players selected {users_choice}. It's a draw!\n")
 elif users_choice == "Rock":
    if computer_action == "Scissors":
        print("Rock smashes scissors! You win!\n")
    else:
        print("Paper covers rock! You lose.\n")
    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        print("\nThanks for playing") 
        break 
      
 elif users_choice == "Paper":
    if computer_action == "Rock":
        print("Paper covers rock! You win!\n")
    else:
        print("Scissors cuts paper! You lose.\n")

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        print("\nThanks for playing")
        break
    

 elif users_choice == "Scissors":
    if computer_action == "Paper":
        print("Scissors cuts paper! You win!\n")
    else:
        print("Rock smashes scissors! You lose.\n")
        

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != "y":
        print("\nThanks for playing")
        break
    