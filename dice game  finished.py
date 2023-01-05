## Program to play 2 player dice game ##
## IMPORTS ##
import os
import sys
import random
import time
from time import sleep
import csv
from tkinter import *
## dice to show off##
from random import randrange
def get_dice_rolls(dice_size, number_of_rolls):
    """Returns list with number_of_rolls from a dice_size-sided dice."""

    return [randrange(1, dice_size+1) for _ in range(number_of_rolls)]


def get_single_dice_face(dice_size, dice_roll, zero_based=False, eye='o '):
    """Return the full face of the roll for a dice-size sided dice."""

    # Shorten roll variable, and account for zero_basing rolls
    r = dice_roll if zero_based else dice_roll - 1

    # Build a proper dice_str according to dice_size and roll
    if dice_size > 12:
        dice_str ='---------\n|' \
            +  eye[r<1] + ' ' + eye[r<5]  + ' ' +  eye[r<7] + ' ' +  eye[r<3] + '|\n|' \
            +  eye[r<9] + ' ' + eye[r<13] + ' ' + eye[r<15] + ' ' + eye[r<11] + '|\n|' \
            + eye[r<17] + ' ' + eye[r<19  ]

    elif dice_size > 6:
          dice_str = ' ------- \n|{} {} {} {}|\n|{} {}'.format(*(eye[r<i] 
                                                               for i in [1, 5, 7, 3, 9, 11]))

    else:
        dice_str = '+-----+\n| {0} {1} |\n| {2}'.format(eye[r<1], eye[r<3], eye[r<5])

    # Return mirrored dice string with changing middle to get a full face
    return dice_str + eye[r&1] + dice_str[::-1]


def print_dice_rolls(dice_size, dice_rolls, zero_based=False,  max_width=72, eye='o '):
    """Pretty print all dice_rolls using dice_size-sided dice(s)."""

    # Verify parameters 
    if dice_size > 20 :
        raise ValueError('Support only up to 20 sided dices')

    if any(roll > dice_size for roll in dice_rolls):
        raise ValueError('Roll is higher than dice size')

    if len(eye) != 2:
        raise ValueError('Excpected two choice for eye parameter')

    # Set up some default values
    dice_width = 7 if dice_size > 6 else 5
    dice_lines = 7 if dice_size > 12 else 5


    # Will try to collate output of multiple dice rolls into lines
    # of up to max_width length
    output_buffer = [''] * dice_lines

    # Debug print for test purposes...
    print('\n{}-sided dice{}: {}'.format(dice_size, ', zero-based' if zero_based else '', dice_rolls))

    # Output the dice rolls using output_buffer
    for roll in dice_rolls:

        # Build a proper dice_str according to dice_size and roll
        current_dice = get_single_dice_face(dice_size, roll, zero_based, eye)

        # Check width of output_buffer against max_width,
        # and if next line go over, then print and reset buffer
        if len(output_buffer[0]) + dice_width >= 72:
            for idx, line in enumerate(output_buffer):
                print(line)
                output_buffer[idx] = ''

        # Append dice to output_buffer
        for idx, line in enumerate(current_dice.split('\n')):
            output_buffer[idx] += line + '  '


    # Print remaining dices in output_buffer
    if len(output_buffer[0]) > 0:
        for line in output_buffer:
            print(line)



if __name__ == '__main__':
    print_dice_rolls(6, [1, 2, 3, 4, 5, 6])
         
## score pre show ##
text_file = open("highscores.txt", "r")
whole_thing = text_file.read()
print (whole_thing)
text_file.close()
###LOGIN SECTION ###

print("Welcome...")
welcome = input("Do you have an acount User1? y/n: ")
if welcome == "n":
    while True:
        username  = input("Enter a username:")
        password  = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "y"
            break
        print("Passwords do NOT match!")

if welcome == "y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome User1")
            break

print("Welcome...")
welcome = input("Do you have an acount User2? y/n: ")
if welcome == "n":
    while True:
        username  = input("Enter a username:")
        password  = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "y"
            break
        print("Passwords do not match!")

if welcome == "y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome User2")
            break

else:
    print(" sorry you can't play this game")
    exit()

### option pick ###
print("pick options 1 to 3")

def menuChoice():
  print('1.The rules ')
  print('2.Start new games ')
  print('3.Quit ')
  choice= int(input('What would you like to do?'))
  while int(choice) < 1 or int(choice) > 3:
    print('That is not a valid option.')
    print('Please enter a number 1 2 or 3:')
    choice=input()
  return choice
  
### display rules for the game ###
def displayRules():
  print('The rules of the game are :')
  print('Players will have a turn to throw two dice.')
  print("If the throw is a 'double', example two 2s, two 3s, etc,")
  print("player's score reverts to zero and their turn ends")
  print('(etc,)')
#Subroutine for each player to take a turn
import random
def playerTurn(player,score):
  print('Your turn, ',player)
  anotherGo = 'Y'
  scoreThisTurn = 0
  while anotherGo == 'Y' or anotherGo == 'y':
    die1 = random.randint(1,8)
    die2 = random.randint(1,8)
    print('You rolled ',die1, ' and',die2)
    if die1 == die2:
      scoreThisTurn= 0
      cumulativeScore = 0
      print('Bad luck! Press any key to continue')
      anyKey= input()
      anotherGo= 'n'
    else:
      scoreThisTurn = scoreThisTurn + die1 +die2
      cumulativeScore = score + scoreThisTurn
      print('Your score after this turn is',scoreThisTurn)
      print('Your total score is ',cumulativeScore)
      if cumulativeScore>= 50:
        anotherGo = 'n'
      else:
        print('Another go? (answer Y or n)')
        anotherGo = input()
  return cumulativeScore
#Subroutine to play game
def playGame():
  score1 = 0
  score2 = 0
  player1 = input("Enter Player1's name: ")
  player2 = input("Enter Player2's name: ")
  while score1 <50 and score2 <50:
    score1 = playerTurn(player1,score1)
    if score1 >=50:
      print('You win!')
    else:
      score2 = playerTurn(player2,score2)
      if score2 >= 50:
        print('You win!')
#main program starts here
option = menuChoice()
print(option)
while option != 3:
  if option == 1:
    displayRules()
    print()
  else:
    playGame()
    menuChoice()
  option = menuChoice()
print('Gooooodbye!')

## score ##
print ("please enter the score for the winner")
save_name = input('Enter your name. ').title()
save_score = input('Enter your score. ')

text_file = open("highscores.txt", "a")
text_file.write("" + save_name + ' ' + save_score + "\n")
text_file.close()

exit()
