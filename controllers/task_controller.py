import json
from models.task import Task

class TaskController:

    def __init__(self, save_file="data/tasks.json"):
        self.tasks = []
        self.next_id = 1
        self.save_file = save_file
        self.load_tasks()

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task

    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                self.save_tasks()
                return True
        return False

    def mark_completed(self, id):
        task = self.find_task(id)
        if task:
            task.mark_completed()
            self.save_tasks()
            return True
        return False

    def find_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def list_tasks(self):
        return self.tasks

    def save_tasks(self):
        data = {
            "next_id": self.next_id,
            "tasks": [
                {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "completed": task.completed
                }
                for task in self.tasks
            ]
        }
        with open(self.save_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_tasks(self):
        try:
            with open(self.save_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.next_id = data.get("next_id", 1)
                for task_data in data.get("tasks", []):
                    task = Task(
                        task_data["id"],
                        task_data["title"],
                        task_data["description"]
                    )
                    task.completed = task_data["completed"]
                    self.tasks.append(task)
        except FileNotFoundError:
            pass
