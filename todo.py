import os, re, subprocess

day_number = None
git_url = None

print(" <======Welcome to TODO-CLI application by Sharpsailor======> ")


def is_git_repository(directory):
    return (
        subprocess.run(
            ["git", "-C", directory, "rev-parse"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).returncode
        == 0
    )


def push_to_git(REMOTE_URL):
    global day_number

    file_name = f"{day_number}.md"
    commit_msg = f"Day {day_number} tasks added"

    # If the directory is not a Git repository, initialize a new one
    if not is_git_repository(current_directory):
        subprocess.run(["git", "init"], cwd=current_directory)
        subprocess.run(["git", "add", file_name], cwd=current_directory)
    else:
        subprocess.run(["git", "add", "."], cwd=current_directory)  # Add all files

    # Commit changes with the commit message
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=current_directory)

    # Create and checkout to the 'main' branch (if not existing)
    subprocess.run(["git", "checkout", "-B", "main"], cwd=current_directory)

    # Check if the remote URL is set
    remote_status = subprocess.run(
        ["git", "config", "--get", "remote.origin.url"],
        cwd=current_directory,
        capture_output=True,
        text=True,
    )

    # If the remote URL doesn't exist, add it
    if not remote_status.stdout.strip():
        subprocess.run(
            ["git", "remote", "add", "origin", REMOTE_URL], cwd=current_directory
        )

    # Push changes to the remote repository
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=current_directory)


class GitURLValidator:
    def __init__(self):
        self.valid_ssh_git_url = re.compile(r"^git@[\w.-]+(:|\/)[\w.-]+\/[\w.-]+\.git$")

    def is_valid_ssh_git_url(self, url):
        return bool(re.match(self.valid_ssh_git_url, url))

    def get_valid_ssh_git_url(self):
        while True:
            input_string = input(
                "Enter the SSH-only enabled URL for your Git repository: "
            )
            if self.is_valid_ssh_git_url(input_string):
                return input_string
            else:
                print("Not a valid SSH Git URL. Please enter a valid URL.")


# Usage example:
validator = GitURLValidator()
valid_url = validator.get_valid_ssh_git_url()
print(f"Link added : {valid_url}")

current_directory = None


# "C:\Users\Sharpsailor\Desktop\ToDo Cli\Desktop\Pushing_folder\2222.md"
def get_destination_folder():
    global current_directory
    default_path = os.path.join(os.path.expanduser("~"), "Desktop", "Todo App")

    user_input = input(
        "Enter Your Destination absolute path or press enter for default location for file creation: "
    )

    if user_input:
        current_directory = user_input
    else:
        current_directory = default_path

    # Check if the directory exists, if not, create it
    if not os.path.exists(current_directory):
        os.makedirs(current_directory)
        print(f"Directory '{current_directory}' created.")

    return current_directory


def get_task(file_name):
    task = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            task = f.read().splitlines()
    return task


# def save_task(file_name, task,current_directory):
#     file_path = os.path.join(current_directory, file_name)
#     with open(file_path, "w") as f:
#         for task_item in task:
#             f.write(f"{task_item}\n")


def save_task(file_name, task, current_directory):
    # global current_directory

    if current_directory:
        file_path = os.path.join(current_directory, file_name)

        try:
            with open(file_path, "w") as f:
                for task_item in task:
                    f.write(f"{task_item}\n")
            print(f"Task saved to: {file_path}")
        except FileNotFoundError:
            print("Error: Specified directory not found.")
    else:
        print("Error: Destination directory not set.")


def add_task(task, new_task):
    task.append(new_task)
    print("New task added ")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks, 1):  # Start enumeration from 1
            print(f"{i}. {task}")


def delete_task(tasks, task_index):
    actual_index = task_index - 1  # Adjust the entered index to match the 0-based index
    if actual_index >= len(tasks) or actual_index < 0:
        print("Task does not exist")
    else:
        del tasks[actual_index]
        print("Task deleted")


def add_task_github(file_name):
    cmd = input(" Is your Github configured ?")
    if cmd == "yes":
        pass
    else:
        pass


def main():
    global current_directory
    current_directory = get_destination_folder()
    print("Enter the task You want to perform ")
    print("1. Add Day")
    print("2. Add Task")
    print("3. Show Task")
    print("4. Delete Task")
    print("5. Save and exit")
    tasks = None  # Initialize tasks as None initially
    while True:
        cmd = int(input("Enter the task you want to perform: "))
        if cmd == 1:
            day_number = int(input("Enter the Day number: "))
            file_name = f"{day_number}.md"
            tasks = get_task(file_name)
            if not tasks:  # Check if tasks is empty, initialize as an empty list if so
                tasks = []
        elif cmd == 2:
            new_task = input("Enter the Task you want to add :")
            add_task(tasks, new_task)
        elif cmd == 3:
            view_tasks(tasks)
        elif cmd == 4:
            if tasks:
                task_index = int(input("Enter the task you want to delete: "))
                delete_task(tasks, task_index)
            else:
                print("No task available to delete")
        elif cmd == 5:
            if tasks and day_number:
                save_task(f"{day_number}.md", tasks, current_directory)
            break
        else:
            print("Enter valid command!!!")


if __name__ == "__main__":
    main()
    git_push = input("Do you want to Push this file to github? YES/NO ").lower()
    if git_push == "yes":
        push_to_git(valid_url)
    else:
        print(
            "Your files have been added to your local directory. Make sure to manually push your files; otherwise, they will remain untracked."
        )

    input("Press Enter to exit...")
