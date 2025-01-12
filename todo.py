  def todo_list_manager():
      todo_list = []
  
      while True:
          print("\nTo-Do List Manager")
          print("1. Add Task")
          print("2. View Tasks")
          print("3. Remove Task")
          print("4. Exit")
  
          choice = input("Enter your choice: ")
  
          if choice == '1':
              task = input("Enter the task: ")
              todo_list.append(task)
              print("Task added successfully!")
          elif choice == '2':
              if not todo_list:
                  print("No tasks available.")
              else:
                  print("Your tasks:")
                  for i, task in enumerate(todo_list, 1):
                      print(f"{i}. {task}")
          elif choice == '3':
              if not todo_list:
                  print("No tasks to remove.")
              else:
                  task_num = int(input("Enter the task number to remove: "))
                  if 0 < task_num <= len(todo_list):
                      removed_task = todo_list.pop(task_num - 1)
                      print(f"Task '{removed_task}' removed successfully!")
                  else:
                      print("Invalid task number!")
          elif choice == '4':
              print("Exiting To-Do List Manager.")
              break
          else:
              print("Invalid choice!")
  
  todo_list_manager()
