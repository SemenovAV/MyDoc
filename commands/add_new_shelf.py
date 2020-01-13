from api.get_shelf import get_shelf
from api.is_exit import is_exit
from api.messenger.inputs.dirs_number_input import dirs_number_input


def add_new_shelf(arg):
    dirs = arg['directories']
    command = arg['command']
    shelf = dirs_number_input(command)
    if is_exit(command, shelf):
        return False
    shelf_exist = get_shelf(dirs, shelf)
    if shelf_exist != -1:
        command['message'] = f'Полка с номером {shelf} уже существует.'
        return False
    else:
        dirs.setdefault(shelf, [])
        command['message'] = f'Успешно добавлена полка с номером {shelf}'
        return True
