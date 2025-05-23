tasks = []
completed = []

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
    if completed:
        print("\n✅ Completed Tasks:")
        for c in completed:
            print(f"- {c}")
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
elif choice == "complete":
    index = int(input("Task number to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        completed_task = tasks.pop(index)
        completed.append(completed_task)
        print(f"Marked task as complete: {completed_task}")
    else:
        print("Invalid task number.")