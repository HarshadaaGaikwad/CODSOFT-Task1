#CODSOFT-TASK-1
#A To-Do List application is a useful project that helps users
# manage and organize their tasks efficiently.
# This project aims to create a command-line or GUI-based application
# using Python, allowing users to create, update, and track their to-do
# list . 
class ToDoListCLI:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {"id": len(self.tasks) + 1, "description": description, "status": "Pending"}
        self.tasks.append(task)
        print(f"Task added: {description}")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(f"{task['id']}. {task['description']} - {task['status']}")

    def update_task_status(self, task_id, new_status):
        task = next((t for t in self.tasks if t['id'] == task_id), None)
        if task:
            task['status'] = new_status
            print(f"Task {task_id} updated - New status: {new_status}")
        else:
            print(f"Task {task_id} not found")

def main():
    todo_cli = ToDoListCLI()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task Status")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_cli.add_task(description)
        elif choice == '2':
            todo_cli.display_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (e.g., Completed): ")
            todo_cli.update_task_status(task_id, new_status)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

