tasks = []

def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    title = input("\nEnter task title: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print(f"Task '{title}' added.")

def view_tasks():
    if not tasks:
        print("\nNo tasks to display.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} - {task['status']}")

def mark_task_complete():
    try:
        view_tasks()
        task_num = int(input("\nEnter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Complete"
            print(f"Task '{tasks[task_num - 1]['title']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    try:
        view_tasks()
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def quit_app():
    print("\nThank you for using the To-Do List App!")
    exit()

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nSelect an option: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                quit_app()
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
