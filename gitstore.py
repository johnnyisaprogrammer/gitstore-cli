import os
import time

print("Loading needed libs/packages and making functions! Please wait.")

def clearscreen():
    os.system("clear")

print("Done! Loading menu in 3 seconds.")
time.sleep(3)

while True:
    clearscreen()
    
    print("Welcome to gitstore! This is a CLI [soon it will be gui] github repo store. You can add your own repos by editing the code.\n")

    print("Options:")
    print("1. Neofetch")
    print("2. neovim")
    print("3. Fastfetch")
    print("4. tiny [a IRC chat client for your terminal]")
    print("Type 'exit' to quit.\n")

    userchoose = input("Enter a number to download that tool: ")

    if userchoose == "exit":
        print("Exiting gitstore. Goodbye!")
        break

    if userchoose == "1":
        print("Downloading Neofetch...")
        os.system("git clone https://github.com/dylanaraps/neofetch.git")

    elif userchoose == "2":
        print("Downloading neovim...")
        os.system("git clone https://github.com/neovim/neovim.git")

    elif userchoose == "3":
        print("Downloading Fastfetch...")
        os.system("git clone https://github.com/LinusDierheimer/fastfetch.git")

    elif userchoose == "4":
        print("Downloading tiny...")
        os.system("git clone https://github.com/jarun/tiny.git")

    else:
        print("Invalid choice! Try again.")
        time.sleep(2)
