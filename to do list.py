from task_manager import load_tasks, save_tasks, get_user_tasks, update_user_tasks
import datetime


# Define the Task class to represent individual tasks
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date


# Define the User class to manage user accounts and tasks
class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        if self.tasks:
            print(f"Tasks for {self.name}:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task.description} [{task.due_date}]")
        else:
            print("No tasks for this user.")


# Define the ToDoList class to manage user interactions
class ToDoList:
    motivational_quotes = [
        "You must set yourself tasks higher than your strengths: firstly, because you never know them anyway, "
        "and secondly, because strength appears as you complete an unattainable task.",
        "Any task can be completed if you break it down into manageable parts.",
        "The more complex the task, the more reason to start it now.",
        "The more impossible a task seems, the more interesting it is to solve it.",
        "The only way to survive is to constantly set yourself new challenges."
    ]

    @classmethod
    def display_motivation(cls):
        import random
        print("Motivation for you: " + random.choice(cls.motivational_quotes))


# Main program loop
def main():
    tasks_data = load_tasks('tasks.json')  # Load tasks from file

    # Sample user creation and tasks
    user_name = input("Welcome to \"TO DO LIST\"\nEnter your name: ")
    user_tasks = get_user_tasks(user_name, tasks_data)
    user = User(user_name)
    user.tasks = [Task(task['description'], task['due_date']) for task in user_tasks]

    # task1 = Task("Complete Python project", "Today")
    # task2 = Task("Study for exam", "This week")
    #
    # user.add_task(task1)
    # user.add_task(task2)

    while True:
        user.display_tasks()

        choice = input("Options: 'Exit', 'Next'\nChoose an option: ").lower()

        if choice == "exit":
            update_user_tasks(user.name, [task.__dict__ for task in user.tasks], tasks_data)  # Save tasks to file
            print(f"Goodbye, {user.name}!")
            break
        elif choice == "next":
            action = input("Options:\n"
                           "1. Write a new task\n"
                           "2. Edit a task\n"
                           "3. Finish a task \nChoose an action(number): ")

            if action == "1":
                description = input("Enter task description: ")
                due_date = input("Enter due date ('Today', 'This week', 'This month'): ")
                new_task = Task(description, due_date)
                user.add_task(new_task)
            elif action == "2":
                task_idx = int(input("Enter task number to edit: ")) - 1
                if 0 <= task_idx < len(user.tasks):
                    while True:
                        new_due_date = input("Enter new due date ('Today', 'This week', 'This month'): ")
                        if new_due_date == "Today" or new_due_date == "This week" or new_due_date == "This month":
                            user.tasks[task_idx].due_date = new_due_date
                else:
                    print("Invalid task number.")
            elif action == "3":
                task_idx = int(input("Enter task number to edit: ")) - 1
                del user.tasks[task_idx]
        else:
            print("Invalid choice.")

        ToDoList.display_motivation()


if __name__ == "__main__":
    main()
