class Task():
    # def __init__(self, task_id, task_name, description="", status="unfinished"):
    def __init__(self, task_name, description="", status="unfinished"):
        # self.task_id = task_id
        self.task_name = task_name
        self.description = description
        self.status = status

    def print_task(self):
        print(f"Task Name   : {self.task_name}")
        print(f"Description : {self.description}")
        print(f"Status      : {self.status}")
        print()
    
    def finished(self):
        self.status = "finished"
    
    def to_dict(self):
        return {
            "task_name": self.task_name,
            "description": self.description,
            "status": self.status
        }