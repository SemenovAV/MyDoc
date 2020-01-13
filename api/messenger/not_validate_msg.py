from api.messenger.post_message import post_message


def not_validate_msg(command):
    command['message'] = 'Введите валидное значение или введите exit для отмены команды'
    post_message(command)
