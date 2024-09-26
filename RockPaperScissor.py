
import random

# Available objects
options = ["rock","paper","scissor"]

playing = True

while playing:

    # Take input from user 
    player1_input = input(" Select your object :\n - rock \n - paper \n - scissor \n :  ")

    # Select input for susytem 
    system_player = random.choice(options)

    # Show both selections
    print(f" \n {player1_input=}, \n {system_player=} \n")

    if system_player == player1_input:
        print("Both have selected same object. No one Wins !!")


    # Rock Part 
    elif player1_input == "rock":
        if system_player == "paper":
            print(" Player 2 Wins the Game ")
        else:
            print("Player 1 wins the Game")
        
    # Paper Part 
    elif player1_input == "paper" :
        if system_player == "rock":
            print(" Player 1 Wins the Game ")
        else :
            print("Player 2 wins the Game")

        
    # Scissor Part 
    elif player1_input == "scissor" :
        if system_player == "rock":
            print(" Player 2 Wins the Game ")
        else:
            print("Player 1 wins the Game")
    
    # Otherwise
    else:
        print(f"You have not selected valid option: \n Your selected option is {player1_input} but available options are {options}")

    print("\n\n")
    next_game = input("Do you want to play one more game ? y/n : ")
    if next_game !="y":
        playing = False
        print("***** Thank you for playing game **********")

    