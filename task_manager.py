tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def list_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    while True:
        print("\nOptions: add, list, quit")
        choice = input("Choose: ").strip().lower()

        if choice == "add":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "list":
            list_tasks()
        elif choice == "quit":
            break
        else:
            print("Invalid option.")
