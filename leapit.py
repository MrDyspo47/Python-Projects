
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

print("Find out if the years is a leap year by answering below !")

def leap_year():


    what_year = input("\nEnter the Year : ")


    if int(what_year) % 4 == 0 :
        print("\nThis year is a leap year")

    elif int(what_year) % 4 > 0 :
        print("\nThis year is not a leap year.")

leap_year()
