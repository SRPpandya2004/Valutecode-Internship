#!/usr/bin/env python3
"""
todo.py

A CLI-based to-do list application supporting:
- Create, view, edit, delete tasks
- Task categorization (Work, Personal, Urgent, etc.)
- Mark tasks as completed
- JSON-based persistence between runs
"""

import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime

DATA_FILE = "tasks.json"


@dataclass
class Task:
    title: str
    description: str
    category: str
    created_at: str
    completed: bool = False

    def mark_completed(self):
        self.completed = True


def load_tasks():
    """Load tasks from DATA_FILE, return list of Task."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Task(**item) for item in raw]


def save_tasks(tasks):
    """Save list of Task to DATA_FILE as JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, indent=2)


def add_task(tasks):
    print("\n=== Add New Task ===")
    title = input("Title: ").strip()
    description = input("Description: ").strip()
    category = input("Category (Work/Personal/Urgent/...): ").strip() or "General"
    created_at = datetime.now().isoformat()
    task = Task(title, description, category, created_at)
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!\n")


def view_tasks(tasks):
    print("\n=== Your Tasks ===")
    if not tasks:
        print("No tasks found.\n")
        return
    for idx, t in enumerate(tasks, 1):
        status = "✔" if t.completed else "✖"
        print(f"{idx}. [{status}] {t.title} ({t.category})")
        print(f"    Created: {t.created_at}")
        print(f"    {t.description}\n")


def mark_task_completed(tasks):
    print("\n=== Mark Task Completed ===")
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Task number to mark done: "))
        tasks[idx - 1].mark_completed()
        save_tasks(tasks)
        print("Task marked completed!\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")


def delete_task(tasks):
    print("\n=== Delete Task ===")
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Task number to delete: "))
        removed = tasks.pop(idx - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed.title}\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")


def edit_task(tasks):
    print("\n=== Edit Task ===")
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Task number to edit: "))
        t = tasks[idx - 1]
        print("Leave blank to keep current value.")
        new_title = input(f"Title [{t.title}]: ").strip()
        new_desc = input(f"Description [{t.description}]: ").strip()
        new_cat = input(f"Category [{t.category}]: ").strip()

        if new_title:
            t.title = new_title
        if new_desc:
            t.description = new_desc
        if new_cat:
            t.category = new_cat

        save_tasks(tasks)
        print("Task updated!\n")
    except (ValueError, IndexError):
        print("Invalid selection.\n")


def main():
    tasks = load_tasks()

    MENU = """
=== To-Do List Menu ===
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Edit Task
5. Delete Task
6. Exit
> """
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Saving and exiting. Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
