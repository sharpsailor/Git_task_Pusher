MainTask = []
tasks = {}
task_id = 0
MainTask.append(task_id)

cmd = input("Enter the task You want to Perform ")

if input == "Create Task":
    create_task()


def create_task():
    global task_id
    task_id += 1
    Day = input("Enter the day  in number:")
    daily_id = 0
    tasks[daily_id] = {"Day:": Day, "tasks": []}
    Add_task(daily_id)
    print("Day Created")
    daily_id += 1


def Add_task(task_id):
    Task = input("Enter the task you want to add")
    task[task_id]["Task"].append(Task)
    print("Task Added ")


def delete_Task():
    pass
