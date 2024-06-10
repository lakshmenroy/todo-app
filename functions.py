def get_todos(filepath='todos.txt'):
    """ Reads the text file and Returns the list of todos. """
    with open(filepath, "r") as txt_file:
        todos_saved = txt_file.readlines()
    return todos_saved


def write_todos(new_todos, filepath='todos.txt'):
    """ Writes the latest changes to the todos list in the text file. """
    with open(filepath, "w") as txt_file:
        txt_file.writelines(new_todos)
