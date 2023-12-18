import time


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


while True:
  def_in = input("\n -$ : ")
  # To add a contact

  if def_in.upper() == "-A":

    with open('contact.txt', 'a') as filename:
      contact_name = input("\nName: ")
      contact_number = input("Phone Number: ")
      print("\nContact Added")
      filename.writelines((contact_name + ' : ' + contact_number + "\n"))

# To find a contact

  elif def_in.upper() == "-F":


    with open("contact.txt", 'r') as filename:
      list = []
      find_name = input("\nFind Contact : ")
      print("\nFinding Contact...")
      time.sleep(2)
      for line in filename:
        if find_name in line:
            print("\n" + line)
            list.append(find_name)
            print(list)
        if find_name not in line:
              
          print("\nContact Not Found")
          break

      

# The help command for newbs XD
  elif def_in.upper() == "-H":
    print("\n -a : To add a contact to the contact book \n -h : prints this message \n -f : To find a contact in the contact book \n -q : To end the program ")
  
  if def_in.upper() == "-Q":
    print('\n -$ : Program Ending ...')
    time.sleep(1)
    print('\n -$ : Program Ended')
    break


#append to the back of thelist eith temp variable



