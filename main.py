from data.documents import documents
from data.directories import directories
from api.run_command import run_command
from api.messenger.post_message import post_message
from commands.config import commands


def doc_program(doc, dirs):
    while True:
        command = input('\nВведите команду("h" - список команд): ')
        if command == 'exit':
            post_message({'component': 'exit', 'message': 'Выход из программы.'})
            break
        else:
            if command in commands:
                obj = commands[command]
                arg = {
                    'documents': doc,
                    'directories': dirs,
                    'command': obj,
                    'commands': commands
                }
                obj['message'] = obj['start']
                post_message(obj)
                run_command(obj, arg)
                post_message(obj)


doc_program(documents, directories)
