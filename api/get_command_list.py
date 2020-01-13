def get_command_list(arg):
    command = arg['command']
    commands = arg['commands']
    message = ''
    for key, value in commands.items():
        message += f'\n"{key}" - {value["start"]}'
    message += '"exit" - Выход'
    command['message'] = message
    return True
