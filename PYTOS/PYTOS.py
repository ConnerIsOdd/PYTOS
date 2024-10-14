import os 
from time import sleep



def setup():
    print("\nWelcome to PYTOS!")
    sleep(0.7)
    print("\nBefore you can begin using the OS, we need some info first to finish setup. (You will only have to do this once)")
    print("\nPreparing...")
    sleep(2)
    prgmpath = ".\\programs"
    filepath = ".\\files"
    print("\nYou will need to create a user login. The username and password can be anything.")
    sleep(0.5)
    username = input("\nNew username: ")
    password = input("\nNew password: ")
    print("\nRegistering...")
    WTT = f"{prgmpath}^{filepath}^{username}^{password}"
    sleep(1)
    print("\nFinalizing setup...")
    config = open("config.txt", "w")
    config.write(WTT)
    config.close()
    sleep(2)
    print("\n\nYou have completed the setup and are ready to use PYTOS!")
    print("\nRebooting...")

def display_programs(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".py"):
                print(f"\n{filename}")

def display_files(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".txt"):
                print(f"\n{filename}")

def open_programs(path):
    display_programs(path)
    prgm = input("\nWhat program would like to open? (.py included): ")
    try:
        with open(path + f"\\{prgm}") as program:
            exec(program.read())
    except Exception as error:
        print("\n\nError: Program does not exist or cannot be indentified/opened")
        print("\nError:")
        print(f"\n{error}")

def open_files(path):
    display_files(path)
    file = input("\nWhat file would like to open? (.txt included): ")
    try:
        with open(path + f"\\{file}") as file:
            txt = file.read()
            print(f"\n{txt}")
            input("\nPress enter to continue: ")
            file.close()
    except:
        print("\n\nError: File does not exist or cannot be indentified/opened")

def cmd(path, username):
    exit = False
    while exit == False:
        cmd = input(f"\n{path.strip("programs")}|{username}> ")
        if cmd.lower() == "test":
            print("\ntest")
        elif cmd.lower() == "exit":
            exit = True
        elif cmd.lower() == "scriptrun":
            folder = input("\nFolder script is in: ")
            if folder == "programs":
                open_programs(path)

            elif folder == "files":
                display_files(path.strip("programs") + folder)
                script = input("What file would you like to run script from? (extension included):")
                try:
                    with open((path.strip("programs") + folder) + f"\\{script}") as script:
                        exec(script.read())
                except Exception as error:
                    print("\n\nError: script does not exist or cannot be indentified/opened/run")
                    print("\nError:")
                    print(f"\n{error}")
            else:
                print("\nInvalid location/directory")

        elif cmd.lower() == "crash":
            os.abort()
            
        else:
            print("\nInvalid Command") 

def main():
    try:
        config = open("config.txt", "r")
        info = config.read()
        info = info.split("^")
        prgmpath = info[0]
        filepath = info[1]
        username = info[2]
        password = info[3]
        config.close()
    except:
        setup()
        config = open("config.txt", "r")
        info = config.read()
        info = info.split("^")
        prgmpath = info[0]
        filepath = info[1]
        username = info[2]
        password = info[3]
        config.close()

    login = False
    while login == False:
        guessuser = input("\nUsername: ") 
        if guessuser == username:
            guesspass = input("\nPassword: ")
            if guesspass == password:
                login = True
            else:
                print("\nUsername or password is incorrect.")
        else:
            print("\nUsername or password is incorrect.")

    print("\nLogged in!")
    opened = True
    while opened == True:
        task = input("\nWhat would you like to do? (type help for valid commands): ")
        if task == "help":
            print("\n\nValid commands:")
            print("\n\n'help' - Displays all valid commands\n'open program' or 'open app' - Gives a list of all programs and opens program user chose\n'open file' - Gives a list of all non-program files and opens file user chose\n'cmd' - Opens cmd\n'power off' or 'off' - Powers off OS")
        elif task == "open program" or task == "open app":
            open_programs(prgmpath)
        elif task == "open file":
            open_files(filepath)
        elif task == "power off" or task == "off":
            print("\nPowering off...")
            sleep(1)
            opened = False
        elif task == "cmd":
            cmd(prgmpath, username)
        else:
            print("\nInvalid command")



    





    

    


if __name__ == "__main__":
    main()
