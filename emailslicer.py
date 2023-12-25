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
print("\n")
while True:

    default_input = input(" - $ : ")

# To learn how to use the program
    
    if default_input == "dyspo -h":
        print("\nGreetings Humans!")
        print("Use [dyspo -r] to use the program")
        print("Use [dyspo -h] to see this message")
        print("Use [dyspo -q] to exit the program\n")



    # To run the program

    if default_input == "dyspo -r":
        num = 0
        what_is = input("\nWhat is the Email ? : ")
        while num == 0 :
            
            what_is_slit = what_is.split("@")
            if "@" in what_is:
                num += 1
                print(f"\nThe Username is : {what_is_slit[0]}")
                print(f"The Domain is : {what_is_slit[1]}\n")            
            if "@" not in what_is:
                print("\nPlease Enter a Valid Email.\n")
                what_is = input("What is the Email ? : ")

# To exit the program
        
    if default_input == "dyspo -q":
        print("\nClosing ...")
        time.sleep(2)
        print("Program is closed\n")
        break

