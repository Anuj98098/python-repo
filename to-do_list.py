# Create an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to view tasks in the list
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the list
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("Options:")
    print("Enter 'add' to add a task")
    print("Enter 'view' to view tasks")
    print("Enter 'remove' to remove a task")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter a task: ")
        add_task(task)
    elif user_input == "view":
        view_tasks()
    elif user_input == "remove":
        view_tasks()
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    else:
        print("Invalid input. Please try again.")
