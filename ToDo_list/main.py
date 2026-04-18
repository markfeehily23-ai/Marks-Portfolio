tasks = []

def addTask():
    task = input("please enter a task:")
    tasks.append(task)
    print(f"Task {task} added to the list")

def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("current Tasks")
        for index, task in enumerate(tasks):
            print(f"Task #{index}, {task}")

def deletTask():
    listTask()
    try:
        taskToDelete = int(input("Enter the # number of task to delete"))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"task {taskToDelete} has been removed.")
        else: 
            print(f"Task # {taskToDelete} was not found.")
    except:
        print("invalid Input")


if __name__ == "__main__":
    ### create a loop to run the app
    print("welcome to the to do list app :)")
    while True: 
        ### Ask the user for a task
        print("\n")
        print("please select one of the following options")
        print("------------------------------------------")
        print("1 Add Task")
        print("2 Delete Task")
        print("3 list Tasks")
        print("4 Quit")

        choice = input("Enter your Choice:")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deletTask()
        elif(choice == "3"):
            listTask()
        elif(choice == "3"):
            break
        else:
            print("Invalid Input")  

    print("goodbye")