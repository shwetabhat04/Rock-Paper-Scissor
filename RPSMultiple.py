
import random

# Available objects
options = ["rock","paper","scissor"]

valid_number = True
while valid_number : 
    game_count = input("\n\nEnter No.of games to be played : ")
    try :
        game_count =  int(game_count)
        valid_number = False
    except:
        print("\nPlease enter valid numerical value")

# playing = True
#while playing:

player1_count = 0
player2_count = 0

for i in range(game_count):

    # Take input from user 
    print(f"\n\n \t Playing {i+1}/{game_count}")
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
            player2_count+=1
        else:
            print("Player 1 wins the Game")
            player1_count+=1
        
    # Paper Part 
    elif player1_input == "paper" :
        if system_player == "rock":
            print(" Player 1 Wins the Game ")
            player1_count+=1
        else :
            print("Player 2 wins the Game")
            player2_count+=1

        
    # Scissor Part 
    elif player1_input == "scissor" :
        if system_player == "rock":
            print(" Player 2 Wins the Game ")
            player2_count+=1
        else:
            print("Player 1 wins the Game")
            player1_count+=1
    
    # Otherwise
    else:
        print(f"You have not selected valid option: \n Your selected option is {player1_input} but available options are {options}")



print("***************************  Player Scores    *******************************")
print(f"\t Player1 Score - {player1_count}")
print(f"\t Player2 Score - {player2_count}")
if player1_count>player2_count:
    print("\n Congrats Final winner is Player1")
elif player1_count == player2_count:
    print("\n Both payers have own same number of games")
else:
    print("\n Congrats Final winner is Player2")

print("***** Thank you for playing game **********")

    