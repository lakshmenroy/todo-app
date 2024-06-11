import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    try:
        user_action = user_action.capitalize().strip()
        print(user_action)
        if user_action.startswith('Add'):
            todo = user_action[4:] + '\n'
            todos = functions.get_todos()
            todos.append(todo)
            functions.write_todos(todos)
        elif user_action.startswith('Show'):
            todos = functions.get_todos()
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")
        elif user_action.startswith('Edit'):
            todos = functions.get_todos()
            item_number = int(user_action[5:])
            if item_number <= len(todos):
                todos[item_number - 1] = input("Enter the new todo: ") + '\n'
                functions.write_todos(todos)
            else:
                print("No Item Found")
        elif user_action.startswith('Complete'):
            todos = functions.get_todos()
            item_number = int(user_action[9:])
            if item_number <= len(todos):
                todos.pop(item_number - 1)
                functions.write_todos(todos)
        elif user_action.startswith('Exit'):
            print("Bye!")
            break
        else:
            print("Error: Wrong Input!")
            print()
            if input("Do you want try again? Y/N: ").capitalize() == 'N':
                print("Bye!")
                break
    except Exception:
        print("Error")
        continue
