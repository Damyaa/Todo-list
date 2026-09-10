tasks = []


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")


def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    print("------------------------")

    for number, task in enumerate(tasks, start=1):
        print(number, "-", task)


print("To-Do List")
print("------------------------")

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
