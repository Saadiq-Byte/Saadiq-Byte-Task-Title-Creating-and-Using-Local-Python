import random


while True:
    
    
    outcomes = {"R": "rock","P":"paper", "S":"scissors"}
    computer_input = ["R", "S", "P"]
    user_choice = input("Enter your choice(R for rock, P for paper, S for scissors) : \n")
    

    computer_choice = random.choice(computer_input)
    try:
        print(f"player ({outcomes[user_choice]}) : computer ({outcomes[computer_choice]})")
        if user_choice == computer_choice:
            print("It is a tie! ")
        elif user_choice == "R":
            if computer_choice == "P":
                print("Computer WINS \n")
            elif computer_choice == "S":
                print("You WIN\n")
        elif user_choice == "P":
            if computer_choice == "S":
                print("Computer WINS\n")
            elif computer_choice == "P":
                print("You WIN\n")
        elif user_choice == "S":
            if computer_choice == "R":
                print("Computer WINS\n")
            elif computer_choice == "P":
                    print("You WIN\n")                         
    except KeyError:
        print("Wrong Input, Please input P, R, S \n")
    

    
    # else:
    #     print("Wrong Input, Please input P, R, S \n")
    #     continue
    
    next_round = input("Do you want to play again y/N: \n")
    if next_round == "N":
        break