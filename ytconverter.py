from pytube import YouTube
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
print("YouTube Converter by MrDyso47")
print("Use [dyspo -h] to learn how to use this program !")  
print("\n ")


while True:
    def_input = input(" -$ : ")

    if def_input == "dyspo -h" or def_input == "dyspo -help":
        print("Use [dyspo -h] to display this message")
        print("Use [dyspo -r] to run the download process")
        print("Use [dyspo -q] to exit the program")


    elif def_input == "dyspo -r" or def_input == "dyspo -run":
        url = input("\nEnter YouTube Video Link : ")
        yt = YouTube(url)
        views = yt.views
        title = yt.title
        publish_date = yt.publish_date
        author = yt.author

        print("\n")
        print(f"Channel Name : {author}")
        print(f"Title : {title}")
        print(f"Published : {publish_date}")
        print(f"Views : {views}")
        downyorn = input("Do You Want To Download ? (Y/N) : ")
        video_stream = yt.streams.get_highest_resolution()
        if downyorn.upper() == "Y" or "YES":
            try: 
                print("Downloading ...")
                video_stream.download("C:\ytdownloads")
            except:
                print("Video could not be downloaded!")

    if def_input == "dyspo -q" or def_input == "dyspo -quit":
        break

# convert()

