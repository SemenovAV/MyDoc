def run_command(command, arg=None):
    if arg is None:
        arg = {}
    return command['func'](arg)
