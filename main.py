class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {"title": title, "description": description, "completed": False}
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Complete" if task["completed"] else "Incomplete"
                print(f"{index + 1}. Title: {task['title']} - Description: {task['description']} - Status: {status}")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_task_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()