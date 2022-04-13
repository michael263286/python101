

tasks = {}

tasks = {
  "title": "",
  "priority": ""
}



user_input = int(input("Press 1 to add task \nPress 2 to delete task \nPress 3 to view all tasks \nPress q to quit"))

if user_input == 1:
  tasks["title"]=print(input("Add task: "))
  tasks["priority"]=print(input("What's the priority?: "))

print(tasks)





