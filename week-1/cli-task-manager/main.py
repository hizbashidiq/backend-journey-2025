from task_manager import TaskManager

# Minimum Feature:
# 1. Add a task
# 2. List all task
# 3. Mark a task as completed
# 4. (Optional) Delete a task
# 5 (Optional) Save/load tasks from json file



def main():
    u_input = 0

    account = TaskManager()
    account.load()


    print("Welcome to Minimalist Task Manager")
    print(f"Hi, {account.username}")
    
    while (u_input != 6):
        print("---LIST OF FEATURES---")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save current task manager")
        print("6. Exit")
        
        u_input = int(input("Please choose using a number: "))
        match u_input:
            case 1:
                print("You'll add a task")
                task_name = str(input("Input your task name: "))
                description = str(input("Input your task description: "))
                status = str(input("Input your task status (finished/unfinished): "))
                account.add_task(task_name, description, status)
                print("Your task have been added")
            case 2:
                account.print_task_manager()
            case 3:
                account.print_task_manager()
                task_id = int(input("Please choose task number:"))
                account.tasks[task_id-1].finished()
            case 4:
                account.print_task_manager()
                task_id = int(input("Please choose task number:"))
                account.delete_task(task_id-1)
                print("Task deleted succesfully.")
            case 5:
                account.save()


if __name__ == "__main__":
    main()