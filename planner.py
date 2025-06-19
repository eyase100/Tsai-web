
class Planner:
    def __init__(self):
        self.tasks = []

    def add_task(self, goal):
        self.tasks.append(goal)
        return f"Task added: {goal}"

    def get_tasks(self):
        return self.tasks

    def clear_tasks(self):
        self.tasks = []
        return "All tasks cleared."
