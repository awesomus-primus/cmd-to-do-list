import os


class tdlFolder:

    path = None

    def __init__(self):
        self.path = os.path.join(os.getcwd(), "to-do-lists")

    def check_users(self):
        contents = os.listdir(self.path)
        users = []
        for f in contents:
            if '.txt' in f:
                users.append(f[:-4])

        if len(users) == 0:
            print("You are the first user to use this tool!")
        else:
            print("The following users use this tool: ")
            for f in users:
                print(str(users.index(f) + 1) + ". " + f)
            print()

    #TODO Implement
    def clear_files(self):
        print("Not implemented yet!")


class tdlFile:

    owner_name = None
    #This piece of code executes a shell command with the given arguments: os.system(args)
    #However, using the subprocess module allows for more powerful executions and retrieval making it preferable
    path = None

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.path = os.path.join(os.getcwd(), "to-do-lists", owner_name + ".txt")

    def check_path(self):
        print("Your list is located in %s" % self.path)

    def create_file(self):
        if not os.path.exists(os.path.join(os.getcwd(), "to-do-lists")):
            os.mkdir("to-do-lists")

        if os.path.exists(self.path):
            print("Welcome back, %s!" % self.owner_name)

        if not os.path.exists(self.path):
            print("Quickly creating your new To Do List...")
            open(self.path, 'a+')
            print("List created!\n")

    def add_new_task(self):
        file = open(self.path, 'a+')

        file.write(input("What is the priority of the task? (A to E according to the GTD system) ") + ", ")
        file.write(input("What task do you want to record? ") + ", ")

        def add_deadline():
            deadline_choice = input("Is there a deadline?(Y/N) ")
            if deadline_choice is 'Y':
                deadline = input("When is the deadline? ")
                file.write(deadline + ", ")
            elif deadline_choice is 'N':
                file.write("None, ")
            else:
                input("Please select either Y or N")
                add_deadline()
        add_deadline()

        def add_person_responsible():
            person_responsible = input("Is someone responsible for completing the task?(Y/N) ")
            if person_responsible is 'Y':
                file.write(input("Who is responsible for the task? "))
            elif person_responsible is 'N':
                file.write("None ")
            else:
                input("Please select either Y or N")
                add_person_responsible()
        add_person_responsible()

        #Adding a new line before closing the file to ensure every item goes on a new line
        file.write('\n')
        print("Task recorded!\n")
        file.close()

    def display_contents(self):
        file = open(self.path, 'r')
        print("Your list consists of the following items:")
        print(file.read())

    def clear_list(self):
        file = open(self.path, 'w')
        print("Your list has been cleared!\n")
