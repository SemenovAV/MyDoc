from commands.get_command_list import get_command_list
from commands.get_people import get_people
from commands.get_doc_shelf import get_doc_shelf
from commands.get_list_document import get_list_document
from commands.add_new_document import add_new_document
from commands.delete_document import delete_document
from commands.move_document import move_document
from commands.add_new_shelf import add_new_shelf
from commands.list_all_owner import list_all_owner


commands = {
        'p': {
            'func': get_people,
            'component': 'people',
            'start': 'Поиск владельца документа по номеру.',
            'message': ''
        },
        'l': {
            'func': get_list_document,
            'component': 'list',
            'start': 'Список всех документов.',
            'message': ''
        },
        's': {
            'func': get_doc_shelf,
            'component': 'shelf',
            'start': 'Поиск полки документа.',
            'message': '',
        },
        'a': {
            'func': add_new_document,
            'component': 'add_doc',
            'start': 'Добавление нового документа.',
            'message': '',
        },
        'd': {
            'func': delete_document,
            'component': 'del',
            'start': 'Удаление документа.',
            'message': '',
        },
        'm': {
            'func': move_document,
            'component': 'move',
            'start': 'Перемещение документа.',
            'message': '',
        },
        'as': {
            'func': add_new_shelf,
            'component': 'add_shelf',
            'start': 'Добавление новой полки.',
            'message': '',
        },
        'ln': {
            'func': list_all_owner,
            'component': 'all_owner',
            'start': 'Список имен владельцев.\n',
            'message': '',
        },
        'h': {
            'func': get_command_list,
            'component': 'help',
            'start': 'Доступные команды\n',
            'message': '',
        }
    }
