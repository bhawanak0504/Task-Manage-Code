import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority=None, due_date=None):
        self.tasks.append({"task": task, "priority": priority, "due_date": due_date})
        print("Task added successfully.")

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['task']} - Priority: {task['priority']}, Due Date: {task['due_date']}")
        else:
            print("No tasks available.")
    
    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task['task']},{task['priority']},{task['due_date']}\n")
        print("Tasks saved to file successfully.")

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    task_info = line.strip().split(',')
                    self.add_task(task_info[0], task_info[1], task_info[2])
            print("Tasks loaded from file successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            priority = input("Enter priority (optional): ")
            due_date = input("Enter due date (optional - YYYY-MM-DD): ")
            todo_list.add_task(task, priority, due_date)
        elif choice == '2':
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index - 1)  # Adjust index to 0-based
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks_to_file(filename)
        elif choice == '5':
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks_from_file(filename)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()