import random
import sys
 
 
 
def Game():
    while True:
 
        comp = random.randint(1,3)
        win = "\nYou WIN!!!"
        lost = "\nYou lost."
        draw = "\nIt's a draw."
 
#Beginning statement#
        print("\nWelcome to Rock, Paper, Scissors!\nYour opponent is me, the computer!\n")
        choice = int(input("Please choose a number!\n1. Rock\n2. Paper\n3. Scissors\n"))
 
        list = [comp,choice]
        wr = 0
        lr = 0
        dr = 0
 
 
#Win/Loss/Draw if statement#
        if list == [1,2]:
            print(win)
            wr = wr + 1
        elif list == [1,3]:
            print(lost)
            lr += 1
        elif list == [1,1]:
            print(draw)
            dr += 1
        elif list == [2,1]:
            print(lost)
            lr += 1
        elif list == [2,2]:
            print(draw)
            dr += 1
        elif list == [2,3]:
            print(win)
            wr = wr + 1
        elif list == [3,1]:
            print(win)
            wr = wr + 1
        elif list == [3,2]:
            print(lost)
            lr += 1
        elif list == [3,3]:
            print(draw)
            dr += 1
        else:
            print("Please choose a listed number.")
            continue
         
#Score shown#
        print("\nWins =", wr)
        print("Losses =", lr)
        print("Draws =", dr, "\n")
 
#Player's choice shown#
        if choice == 1:
            playerChoice = "Rock"
            print("\nYou chose", playerChoice)
        if choice == 2:
            playerChoice = "Paper"
            print("\nYou chose", playerChoice)
        if choice == 3:
            playerChoice = "Scissors"
            print("\nYou chose", playerChoice)
 
 
#Computer's choice shown#
        if comp == 1:
            compChoice = "Rock"
            print("\nI chose", compChoice)
        if comp == 2:
            compChoice = "Paper"
            print("\nI chose", compChoice)
        if comp == 3:
            compChoice = "Scissors"
            print("\nI chose", compChoice)
 
         
#Play Again#
        again = input("\nPlay again? Y/N\n")
        if again.upper() == "Y":
            continue
        else:
            print("\nThanks for playing!!")
            break
            sys.exit
 
         
Game()
