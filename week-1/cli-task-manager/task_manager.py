from task import Task
from pathlib import Path
import json

class TaskManager():
    def __init__(self, username="", tasks=None):
        self.username = username
        self.tasks = tasks if tasks is not None else []

    def __len__(self):
        return len(self.tasks)

    def print_task_manager(self):
        print(f"Username    : {self.username}")
        i = 0
        print()
        if len(self.tasks) == 0:
            print("There's no task yet")
        else:
            print(f"You have {len(self)} tasks")
            for task in self.tasks:
                i += 1
                print(i)
                task.print_task()

    def add_task(self, task_name, description="", status="unfinished"):
        self.tasks.append(Task(task_name=task_name, description=description, status=status))

    def delete_task(self, task_id):
        self.tasks.pop(task_id)

    def save(self):
        json_data = {}
        json_data["username"] = self.username
        tasks_data = [task.to_dict() for task in self.tasks]
        # for task in self.tasks:
        #     task_data = {}
        #     task_data["task_name"] = task.task_name
        #     task_data["description"] = task.description
        #     task_data["status"] = task.status
        #     tasks_data.append(task_data)
        json_data["tasks"] = tasks_data
        filename = Path(__file__).parent / "task_managersss.json"
        json_str = json.dumps(json_data, indent=4)
        with open(filename, "w") as f:
            f.write(json_str)
            # json.dump(json_data, f)
    
    def load(self):
        filename = Path(__file__).parent / "task_manager.json"
        with open(filename, "r") as f:
            data = json.load(f)
        self.username = data["username"]
        for task in data["tasks"]:
            self.add_task(task["task_name"], task["description"], task["status"])