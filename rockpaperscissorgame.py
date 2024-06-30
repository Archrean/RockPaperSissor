# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
def computerChoice():
    choice = random.randint(1,6)
    if choice == 1 or choice ==2:
        return "rock"
    elif choice == 3 or choice==4:
        return "paper"
    elif choice == 5 or choice == 6:
        return "scissor"

def determineWinner(player,computer):
         if player==computer:
             print("It is a tie\n")
             player = input("Please enter rock paper or scissor again:  ")
             computer= computerChoice()
             determineWinner(player,computer)
         elif player=="rock" and computer=="scissor":
             print("You win.rock beats Scissor")
         elif player == "paper" and computer == "rock":
             print("You win.paper beats rock")
         elif player == "scissor" and computer == "paper":
             print("You win. scissor beats paper")
         else:
             print(f"You lose.{computer} beats {player}")


def main():
    print("Lets play Rock Paper Scissor\n")
    play = True
    while play==True:
        player_choice = input("Please input rock paper or scissors: ")
        computer_choice = computerChoice()
        determineWinner(player_choice,computer_choice)
        again = input("Do you want to play again yes or no: ")
        if again=="no":
            play = False
    print("Thank you for playing")
main()
