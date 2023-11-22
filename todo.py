import os


def get_task(file_name):
    task = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            task = f.read().splitlines
    return task


def save_task(file_name, task):
    with open(file_name, "w") as f:
        for task in task:
            f.write(f"{task}\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(task, new_task):
    task.append(new_task)
    print("New task added ")


def delete_task(tasks, task_index):
    if task_index >= len(tasks) or task_index == 0:
        print("Task does not exist")
    else:
        del tasks[task_index]
        print("Task deleted")


def add_task_github(file_name):
    cmd = input(" Is your Github configured ?")
    if cmd == "yes":
        pass
    else:
        pass


def main():
    print("<===TODO==CLI===>")
    print("Enter the task You want to perform ")
    print("1. Add Day")
    print("2. Add Task")
    print("3. Show Task")
    print("4. Delete Task")
    print("5. Save and exit")
    day_number = None
    tasks = None
    while True:
        cmd = int(input("Enter the task you want to perform"))
        if cmd == 1:
            day_number = int(input("Enter the Day number"))
            file_name = f"{day_number}.md"
            tasks = get_task(file_name)
        elif cmd == 2:
            new_task = input("Enter the Task you want to add :")
            add_task(tasks, new_task)
        elif cmd == 3:
            view_tasks(tasks)
        elif cmd == 4:
            if tasks:
                task_index = int(input("Enter the task you want to delete"))
                delete_task(tasks, task_index)
            else:
                print("No task available to delete")
        elif cmd == 5:
            if tasks and day_number:
                save_task(f"{day_number}.md", tasks)
            break
        else:
            print("Enter valid command")
    print("Do you want to Push this file to github")


if __name__ == "__main__":
    main()
