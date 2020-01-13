def is_exit(command, elem):
    if elem == -1:
        command['message'] = 'Отмена команды'
        return True
