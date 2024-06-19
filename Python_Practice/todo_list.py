class todo_list:
  def __init__(self):
    self.tasks = []

  def add_task(self,task):
    self.tasks.append(task)
    print("Task Added: ",task)

  def delete_task(self,task_index):
    if 0 <= task_index < len(self.tasks):
      deleted_task = self.tasks.pop(task_index)
      print("Deleted Task : ",deleted_task)

    else:
      print("Invalid task index")

  def mark_completed(self, task_index):
    if 0 <= task_index < len(self.tasks):
      self.tasks[task_index] += " (Completed)"
      print("Task marked as completed : ",self.tasks[task_index])

    else:
      print("Invalid")

  def display_task(self):
    if self.tasks:
      print("\n TODO LIST")
      for index, task in enumerate(self.tasks):
        print(f"{index + 1}.{task}")
    else:
      print("TODOLIST is empty...")


def main():
  todolist = todo_list()

  while True:
    print("*******************")
    print("ENTER OPTIONS")
    print("1. Add Task")
    print("2. delete Task")
    print("3. mark as complete")
    print("4. display")
    print("5 exit")

    choose = int(input("Enter Choice...."))

    if choose == 1:
      task = input("Enter task : ..")
      todolist.add_task(task)

    elif choose == 2:
      task_index = int(input("Enter task index to delete..."))
      todolist.delete_task(task_index)

    elif choose == 3:
      task_index = int(input("=mark as read ..."))
      todolist.mark_completed(task_index)

    elif choose == 4:
      todolist.display_task()

    elif choose == 5:
      print("Exiting....")
      break

    else:
      print("Invalid Choice. Please try again...")

if __name__ == '__main__':
  main()
