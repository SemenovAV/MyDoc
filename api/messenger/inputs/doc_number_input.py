from api.messenger.not_validate_msg import not_validate_msg


def doc_number_input(command):
    result = None
    while not result:
        result = input(f'\n{command["component"]}@: Введите номер документа: ').strip()
        if result.isspace() or len(result) == 0:
            not_validate_msg(command)
            result = None
        elif result == 'exit':
            return -1
    return result
