from data.documents import documents
from data.directories import directories

from api.get_document_index import get_document_index
from api.get_shelf import get_shelf
from api.get_document_shelf import get_document_shelf
from api.dir_delete_doc_number import dir_delete_doc_number
from api.dir_add_doc_number import dir_add_doc_number
from api.get_list import get_list
from api.view_document import view_document
from api.create_document import create_document
from api.remove_document import remove_document
from api.add_document import add_document
from api.is_document import is_document
from api.is_exit import is_exit
from api.run_command import run_command
from api.get_command_list import get_command_list

from api.messenger.post_message import post_message
from api.messenger.inputs.doc_number_input import doc_number_input
from api.messenger.inputs.doc_type_input import doc_type_input
from api.messenger.inputs.doc_owner_input import doc_owner_input
from api.messenger.inputs.dirs_number_input import dirs_number_input


def doc_program(doc, dirs):
    def get_people(arg):
        doc = arg['documents']
        command = arg['command']
        doc_number = doc_number_input(command)
        if is_exit(command, doc_number):
            return False
        index = get_document_index(doc, doc_number)
        if index != -1:
            result = documents[index].get('name')
            command['message'] = f'Документ с номером {doc_number} найден, владелец {result}'
            return True
        else:
            command['message'] = f'Документ с номером {doc_number} не найден.'
            return False

    def get_doc_shelf(arg):
        dirs = arg['directories']
        command = arg['command']
        doc_number = doc_number_input(command)
        if is_exit(command, doc_number):
            return False
        result = get_document_shelf(dirs, doc_number)
        if result != -1:
            command['message'] = f'Документ с номером {doc_number} расположен на полке {result[0]}'
            return True
        else:
            command['message'] = f'Документ с номером {doc_number} не найден'
            return False

    def get_list_document(arg):
        docs = arg['documents']
        dirs = arg['directories']
        command = arg['command']
        result = get_list(docs, dirs)
        if result != -1:
            command['message'] = f'\n{result}'
            return True
        else:
            command['message'] = 'Документы отсутствуют'
            return False

    def add_new_document(arg):
        dirs = arg['directories']
        command = arg['command']
        doc_number = doc_number_input(command)
        if is_exit(command, doc_number):
            return False
        if get_document_shelf(dirs, doc_number) != -1:
            command['message'] = f'Документ с номером {doc_number} уже существует'
            return
        doc_type = doc_type_input(command)
        if is_exit(command, doc_type):
            return False
        owner = doc_owner_input(command)
        if is_exit(command, owner):
            return False
        shelf_number = dirs_number_input(command)
        if is_exit(command, shelf_number):
            return False
        document = create_document(doc_number, doc_type, owner)
        if is_document(document):
            result = add_document(documents, directories, document, shelf_number)
            if result:
                command['message'] = f'Документ добавлен:\n\n{view_document(dirs, result[0])}'
                return True
            else:
                command['message'] = 'Ошибка добавления документа'
                return False
        else:
            command['message'] = 'Ошибка создания документа'
            return False

    def delete_document(arg):
        docs = arg['documents']
        dirs = arg['directories']
        command = arg['command']
        doc_number = doc_number_input(command)
        if is_exit(command, doc_number):
            return False
        shelf = get_document_shelf(dirs, doc_number)
        if shelf == -1:
            command['message'] = f'Документ с номером {doc_number} не существует'
            return False
        document = get_document_index(docs, doc_number)
        if document != -1:
            result = remove_document(docs, dirs, document, shelf)
            command['message'] = f'Документ с номером {doc_number} успешно удален.\n{result}'
            return True
        else:
            command['message'] = f'Документ с номером {doc_number} не существует'
            return False

    def move_document(arg):
        dirs = arg['directories']
        command = arg['command']
        doc_number = doc_number_input(command)
        if is_exit(command, doc_number):
            return False
        doc_shelf = get_document_shelf(dirs, doc_number)
        if doc_shelf == -1:
            command['message'] = f'Документ с номером {doc_number} не существует'
            return False
        command['message'] = f'Документ найден на полке {doc_shelf[0]}\n'
        post_message(command)
        shelf = dirs_number_input(command)
        if is_exit(command, doc_number):
            return False
        result_del = dir_delete_doc_number(directories, doc_shelf)
        if result_del != -1:
            result_add = dir_add_doc_number(directories, doc_number, shelf)
            if result_add != -1:
                command['message'] = f'Документ номер {doc_number} перенесен с полки {doc_shelf[0]} на полку {shelf}'
                return True
            command['message'] = 'Ошибка добавления документа'
            return False
        command['message'] = 'Ошибка удаления документа'
        return False

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

    def list_all_owner(arg):
        docs = arg['documents']
        command = arg['command']
        names = set()
        errors = 0
        counter = 0
        if len(docs) > 0:
            for doc in docs:

                try:
                    name = doc['name']
                except KeyError as e:
                    errors += 1
                    break
                else:
                    names.add(name)
            if len(names) > 0:
                for name in names:
                    counter += 1
                    command['message'] += f'{counter}. {name}\n'
            else:
                command['message'] = 'Имена не найдены'
            if errors > 0:
                command['message'] += f'---------\nДокументов с несуществующим ключем "name": {errors}'
        else:
            command['message'] = 'Документов нет'
            return False
        return True

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
