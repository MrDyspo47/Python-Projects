
LOGO = """

$$$$$$$\                                          
$$  __$$\                                         
$$ |  $$ |$$\   $$\  $$$$$$$\  $$$$$$\   $$$$$$\  
$$ |  $$ |$$ |  $$ |$$  _____|$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ |\$$$$$$\  $$ /  $$ |$$ /  $$ |
$$ |  $$ |$$ |  $$ | \____$$\ $$ |  $$ |$$ |  $$ |
$$$$$$$  |\$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$$  |
\_______/  \____$$ |\_______/ $$  ____/  \______/ 
          $$\   $$ |          $$ |                
          \$$$$$$  |          $$ |                
           \______/           \__|                
"""

print(LOGO)

import random

Things = ["Rock","Paper","Scissors"]

userin = input("\n\n\n\n\nChoose Rock\
\Paper\\Scissors ? : ")

comp_choice = random.choice(Things)



def rps():

  #If user input is ROCK
  
  if userin.upper() == "ROCK" and comp_choice == "Scissors":
    print("The computers input is {comp_choice}".format(comp_choice=comp_choice))
    print("You Won !")
  elif userin.upper() == "ROCK" and comp_choice == "Paper":
    print("The computers input is {comp_choice}".format(comp_choice=comp_choice))
    print("The Computer Wins !")
  elif userin.upper() == "ROCK" and comp_choice.upper() == "ROCK":
    print("The computers input is also {comp_choice}".format(comp_choice=comp_choice))
    print("Its a Tie !")
  
  
  
  
  
  # If user input is PAPER
  
  if userin.upper() == "paper".upper() and comp_choice == "Rock":
    print("The computers input is {comp_choice}".format(comp_choice=comp_choice))
    print("You Won !") 
  elif userin.upper() == "paper".upper() and comp_choice.upper() == "PAPER":
    print("The computers input is also {comp_choice}".format(comp_choice=comp_choice))
    print("Its a Tie !")
    
  elif userin.upper() == "paper".upper() and comp_choice.upper() == "SCISSORS":
    print("The computers input is {comp_choice}".format(comp_choice=comp_choice))
    print("The Computer Wins !")
  
  #If user input is SCISSORS
  
  
  if userin.upper() == "scissors".upper() and comp_choice == "Rock":
    print("The computers input is {comp_choice}".format(comp_choice=comp_choice))
    print("The Computer Wins !") 
  elif userin.upper() == "SCISSORS".upper() and comp_choice.upper() == "PAPER":
    print("The computers input is {comp_choice}".format(comp_choice=comp_choice))
    print("You Won !")
  
  elif userin.upper() == "scissors".upper() and comp_choice.upper() == "SCISSORS":
    print("The computers input is also {comp_choice}".format(comp_choice=comp_choice))
    print("Its a Tie !")
    
rps()