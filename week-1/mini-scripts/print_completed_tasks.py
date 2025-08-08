import json
from pathlib import Path

def print_completed_tasks(json_file):
    try:
        with open(json_file, "r") as f:
            tasks = json.load(f)
            for task in tasks:
                if task["completed"] is True:
                    print(task["title"])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":

    filename = Path(__file__).parent / "tasks.json"
    print_completed_tasks(filename)
