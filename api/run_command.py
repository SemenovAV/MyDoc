def run_command(command, arg=None):
    if arg is None:
        arg = {}
    try:
        result = command['func'](arg)
    except Exception as e:
        command['message'] = f'Компонент {command["component"]} вернул сообщение об ошибке: {e}'
        return False
    else:
        return result
