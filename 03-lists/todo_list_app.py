# To-Do List App
#
# A simple command-line app for managing a list of tasks.
#
# Features:
# 1. Shows the current tasks as a numbered list (or a message if it is empty).
# 2. Add a task: the user types the task and it is appended to the list.
# 3. Remove a task: the user enters the task number and it is removed.
# 4. Quit: ends the program.
#
# The menu repeats in a loop until the user chooses to quit.

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("TO-DO LIST APP".center(LINE_WIDTH))
print("=" * LINE_WIDTH)

todo_list = []

while True:
    print()
    print("-" * LINE_WIDTH)
    print("YOUR TASKS")
    print("-" * LINE_WIDTH)

    if len(todo_list) == 0:
        print("  (Your to-do list is empty)")
    else:
        index = 1
        for task in todo_list:
            print(f"{index}. {task}")
            index += 1

    print("-" * LINE_WIDTH)
    print("OPTIONS")
    print("  1) Add a task")
    print("  2) Remove a task")
    print("  3) Quit")
    print("-" * LINE_WIDTH)

    choice = input("Choose an option (1-3): ")
    print()

    if choice == "1":
        print("***** ADD A TASK *****")
        new_task = input("Enter the new task: ")
        todo_list.append(new_task)
        print(f"[+] Task added: {new_task}")
    elif choice == "2":
        print("***** REMOVE A TASK *****")
        if len(todo_list) == 0:
            print("[!] Nothing to remove, your list is empty.")
        else:
            task_number = int(input("Enter the task number: ")) - 1
            removed_task = todo_list.pop(task_number)
            print(f"[-] Task removed: {removed_task}")
    elif choice == "3":
        print("=" * LINE_WIDTH)
        print("Goodbye!".center(LINE_WIDTH))
        print("=" * LINE_WIDTH)
        break
    else:
        print("[!] Invalid input, please choose 1, 2, or 3.")
