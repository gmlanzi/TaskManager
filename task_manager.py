print("Task Manager is running...")

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def list_tasks():
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number!")


# Teste básico
add_task("Buy groceries")
add_task("Finish the project")
list_tasks()

