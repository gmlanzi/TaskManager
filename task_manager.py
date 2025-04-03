import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Carrega tarefas do arquivo JSON."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Salva tarefas no arquivo JSON."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Adiciona uma nova tarefa e salva no JSON."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def list_tasks():
    """Lista todas as tarefas salvas no JSON."""
    tasks = load_tasks()
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks found!")

def remove_task(task_number):
    """Remove uma tarefa pelo número e salva a lista atualizada no JSON."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid task number!")

# Testes básicos
if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Finish the project")
    list_tasks()
    remove_task(1)
    list_tasks()
