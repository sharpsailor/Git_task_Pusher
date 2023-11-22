tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added")


def remove_task(tasks):
    if task in tasks:
        tasks.remove(task)
        print("Task removed")
    else:
        print("Task not found")


def view_task():
    if tasks:
        print("Your Tasks")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No Tasks")


def completed_task(task):
    if task in tasks:
        pass
