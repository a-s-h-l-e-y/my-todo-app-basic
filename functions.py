FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns
    the list of any existing to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do items to the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
