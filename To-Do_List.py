''' A To-Do List application is a useful project that helps users manage and organize their 
tasks efficiently. This project aims to create a command line or GUI based application 
using Python allowing users to create, update and track their to-do lists.'''

tasks= {}

def menu():
    print("To-Do List Menu")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View all Task")
    print("5. Exit")

def add_task():
    task_name= input("enter the task name:")
    task_description = input("enter description for the task:")
    tasks[task_name]= task_description
    print(f"Task '{task_name}' added successfully")

def update_task():
    task_name= input("enter the task name to update:")
    if task_name in tasks:
        new_description = input("enter new description for the task:")
        tasks[task_name]= new_description
        print(f"Task '{task_name}' updated successfully")
    else:
        print(f"Task '{task_name}' not found")

def delete_task():
    task_name= input("enter the task name to delete:")
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' deleted successfully")
    else:
        print(f"Task '{task_name}' not found")

def view_tasks():
    if tasks:
        print("All Tasks")
        for task_name, task_description in tasks.items():
            print(f"Task name: {task_name}")
            print(f"Description: {task_description}")
    else:
        print("No tasks found.")

def main():
    while True:
        menu()
        choice= int(input("Enter your choice:"))

        if choice == 1:
            add_task()
        elif choice == 2:
            update_task()
        elif choice == 3:
            delete_task()
        if choice == 4:
            view_tasks()
        elif choice == 5:
            print("Exiting.")
            break
        else:
            print("Invalid choice.")
main()