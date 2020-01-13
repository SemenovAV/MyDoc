from api.messenger.not_validate_msg import not_validate_msg


def dirs_number_input(command):
    result = None
    while not result:
        result = input(f'\n{command["component"]}@: Введите номер полки: ').strip()
        if result.isspace() or len(result) == 0:
            not_validate_msg(command)
            result = None
        elif result == 'exit':
            return -1
    return result
