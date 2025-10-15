class Task:
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_uncompleted(self):
        self.completed = False

    def __str__(self):
        status = "OK" if self.completed else "NON"
        return f"[{self.id}] {status} {self.title} - {self.description}"
