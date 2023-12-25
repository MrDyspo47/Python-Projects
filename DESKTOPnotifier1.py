from plyer import notification
import time

       #################
       #   VARIABLES   #
       #################
            

while True:
    default_input = input(" \n-$ : ")


    if default_input == "-h":
        print("\n\nGreetings Humans ! \n\n-s : Is used to setup a notification \n\n-q : Is used to quit the program\n\n ")

        print("If you want to input hours into the \"How Much Time From Now ?\" convert the hours into minutes")
    
    if default_input == "-s":
        def show_notification():
            is_it_true = 0
            is_it_true1 = 0
        
            Task_name = input("\nWhats The Title ? : ")
            Task_message = input("Whats The Message ? : ")
            while is_it_true == 0:
                try:
                    Task_hour = int(input("\nHow Much Hours From Now ? :  "))
                    is_it_true += 1
                    break
                except:
                    print("\nPlease Enter A Number") 
                    
            while is_it_true1 == 0:
                try:
                    Task_min = int(input("How Much Minutes From Now ? :  "))
                    is_it_true1 += 1
                    break
                except:
                    print("\nPlease Enter A Number") 
                    
            Task_hour1 = Task_hour * 3600
            Task_min1 = Task_min * 60
            final_time = Task_hour1 + Task_min1


            try:
                print("Notification Sent !")
                time.sleep(int(final_time)) #Sets the reminder
                notification.notify(Task_name,Task_message)
            except:
                print("Notification was not set")
            

        show_notification()

        
    if default_input == "-q":
        print("\nClosing ...")
        time.sleep(2)
        print("\nClosed\n")
        break