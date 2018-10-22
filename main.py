# import win32api
# import win32console
# import win32gui
from ToDoList import tdlFile, tdlFolder

# TODO Finish at some point
# try:
#     pass
# except ModuleNotFoundError as e:
#     import sys
#     import subprocess
#     print("%s, I need to install some packages as they are not present." % name)
#     def install(package):
#         print("Installing package %s..." % package)
#         subprocess.call([sys.executable, "-m", "pip", "install", package])
#         print("Installation complete!")
#     install("pypiwin32")
#     install("diggity")

name = None


def main():

    print("Welcome to the Command Line To Do List!")
    name = input("What is your name? ")
    folder = tdlFolder()

    folder_capabilities = {
        '1': "Use the tool",
        '2': "Check existing users",
        '3': "Clear files",
        '4': "Exit"
    }

    def folder_options():
        choice = input("""Hi %s, what would you like to do today?
Type the number of an option to select it:
    1: %s
    2: %s
    3: %s
    4: %s
    """ % (name,
           folder_capabilities['1'],
           folder_capabilities['2'],
           folder_capabilities['3'],
           folder_capabilities['4']))
        print('You chose to "%s"' % folder_capabilities[choice])

        if choice == '1':
            user_options()

        elif choice == '2':
            folder.check_users()
            folder_options()

        elif choice == '3':
            folder.clear_files()
            folder_options()

        elif choice == '4':
            print("Thanks for using the CMD To Do List!")
            exit()

        else:
            print("Please only enter the number of your desired option")
            folder_options()

    user_capabilities = {
        '1': "Add a new item to your list",
        '2': "Read your list",
        '3': "Clear list",
        '4': "Check the location of your list",
        '5': "Exit"
    }

    def user_options():
        todo = tdlFile(name)
        todo.create_file()

        choice = input("""What do you want to do?
Type the number of an option to select it:
    1: %s
    2: %s
    3: %s
    4: %s
    5: %s
    """ % (user_capabilities['1'],
           user_capabilities['2'],
           user_capabilities['3'],
           user_capabilities['4'],
           user_capabilities['5']))
        print('You chose to "%s"' % user_capabilities[choice])

        if choice == '1':
            todo.add_new_task()
            user_options()

        elif choice == '2':
            todo.display_contents()
            user_options()

        elif choice == '3':
            todo.clear_list()
            user_options()

        elif choice == '4':
            todo.check_path()
            user_options()

        elif choice == '5':
            print("Thanks for using the CMD To Do List!")
            exit()

        else:
            print("Please only enter the number of your desired option")
            user_options()

    folder_options()


main()
