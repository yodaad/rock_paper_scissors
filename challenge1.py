import random

options = ("rock", "paper", "scissors")

computer_victories = 0
user_victories = 0
rounds = 1

while True:
    
    print("-" * 10)
    print("ROUND", rounds)
    print("-" * 10)
    print("Computer victories: ", computer_victories)
    print("User victories: ", user_victories)
    
    user_option = input("Choose rock, paper or scissors: ").lower()
    rounds += 1

    if not user_option in options:
        print("That is not a valid choice, try again!")
        continue
        
        
    computer_option = random.choice(options)

    if user_option == computer_option:
        print(f"It is a tie because the computer chose {computer_option}")
    elif user_option == "rock":
        if computer_option == "scissors":
            print(f"You won because the computer chose {computer_option}")
            user_victories += 1
        else:
            print(f"You lost because the computer chose {computer_option}")
            computer_victories += 1
    elif user_option == "paper":
        if computer_option == "rock":
            print(f"You won because the computer chose {computer_option}")
            user_victories += 1
        else:
            print(f"You lost because the computer chose {computer_option}")
            computer_victories += 1
    elif user_option == "scissors":
        if computer_option == "paper":
            print(f"You won because the computer chose {computer_option}")
            user_victories += 1
        else:
            print(f"You lost because the computer chose {computer_option}")
            computer_victories += 1
            
    if computer_victories == 2:
        print("THE COMPUTER WON WITH A SCORE OF: ", computer_victories, " ", user_victories)
        break
    
    if user_victories == 2:
        print("THE USER WON WITH A SCORE OF: ", user_victories, " ", computer_victories)
        break
    
    
   