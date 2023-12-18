import random

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

print("\Guess a number from 1 to 10\n")


num_list = [] # Makes a empty list for the numbers to get appended to 


for num in range(1 , 11):
    num_list.append(num)
    rand_num = random.choice(num_list)


user_input = input("Guess a number: ")

try:
    

    while int(user_input) != rand_num:
        wrong_guess=input("\nTry again wrong guess: ")

        if int(user_input) == rand_num or int(wrong_guess) == rand_num:
            print("\nYou guessed the number !\n")
            break
except:
    print("\nPlease Enter A Number")












