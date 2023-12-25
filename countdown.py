import time

logo = """


 /$$      /$$           /$$$$$$$                                         
| $$$    /$$$          | $$__  $$                                        
| $$$$  /$$$$  /$$$$$$ | $$  \ $$ /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$| $$  | $$| $$  | $$ /$$_____/ /$$__  $$ /$$__  $$
| $$  $$$| $$| $$  \__/| $$  | $$| $$  | $$|  $$$$$$ | $$  \ $$| $$  \ $$
| $$\  $ | $$| $$      | $$  | $$| $$  | $$ \____  $$| $$  | $$| $$  | $$
| $$ \/  | $$| $$      | $$$$$$$/|  $$$$$$$ /$$$$$$$/| $$$$$$$/|  $$$$$$/
|__/     |__/|__/      |_______/  \____  $$|_______/ | $$____/  \______/ 
                                  /$$  | $$          | $$                
                                 |  $$$$$$/          | $$                
                                  \______/           |__/                



"""

print(logo)  

print("Use [dsypo -h] to learn how to use this program !\n")

while True:
    default_input = input(" -$ : ")

    dog = 0

    # Help part of the progroam | For learning how to use the program

    if default_input == "dyspo -h":
        print("\nGreetings Humans\n")
        print("Use [dyspo -r] to to setup the countdown !")
        print("Use [dyspo -q] to quit the program")
        print("Use [dsypo -h] to display this message\n")


    # To start the countdown process
        
    if default_input == "dyspo -r":

        while dog == 0:
            try:
                countdown_var = int(input("\nWhat number do you want to countdown from ? : "))
                
                dog += 1
            except:
                countdown_var = int(input("What number do you want to countdown from ? : "))
                print("Please Enter A Number")

        # Just to make it look neat line 53 & 54
        time.sleep(1)
        print("\n")

        # Subtracts one from user input to create a countdown effect & it replaces 0 with a message.

        for i in range(countdown_var):
            if countdown_var != 0:
                print(countdown_var)
                countdown_var -= 1
                time.sleep(1)
            elif countdown_var == 0:
                continue
        print("Hooray , countdown is finished !\n")


# To to exit the program
        
    if default_input == "dyspo -q":
        print("Closing ...")
        time.sleep(2)
        print("Closed")
        break
