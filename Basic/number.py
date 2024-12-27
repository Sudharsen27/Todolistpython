# Simple To-Do List Application

# List to store tasks
tasks = []

def display_menu():
    """Display the menu options."""
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    print("5. Location")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """View all tasks."""
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    """Delete a task by its number."""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def add_location():
    """Add a location to the list."""
    location = input("Enter the location: ")
    print(f"Location '{location}' added successfully!")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    elif choice == "5":
        add_location()
    else:
        print("Invalid choice! Please select a valid option.")
