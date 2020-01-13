documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type":"0"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def doc_program(doc, dirs):
    def get_document_index(documents, document_number):
        for index, document in enumerate(documents):
            if document['number'] == document_number:
                return index
        return -1

    def get_shelf(directories, shelf):
        return directories.get(shelf, -1)

    def get_document_shelf(directories, document_number):
        for shelf_number, document_numbers in directories.items():
            for index, number in enumerate(document_numbers):
                if number == document_number:
                    return [shelf_number, index]
        return -1

    def dir_delete_doc_number(directories, shelf_document_index):
        shelf_number, index = shelf_document_index
        shelf = get_shelf(directories, shelf_number)
        if shelf:
            new_value = list(shelf)
            result = new_value.pop(index)
            if (result or -1) != -1:
                directories[shelf_number] = tuple(new_value)
                return result
            else:
                return -1
        return -1

    def dir_add_doc_number(directories, document_number, shelf_number):
        shelf = directories.setdefault(shelf_number, [])
        new_value = list(directories.get(shelf_number))
        new_value.append(document_number)
        directories[shelf_number] = tuple(new_value)
        return document_number

    def get_list(documents, directories):
        result = ''
        for index, document in enumerate(documents):
            result += f'{index + 1}:\n{view_document(directories, document)}\n\n'
        result += f'Всего документов: {len(documents)}'
        return result or -1

    def create_document(document_number, docyment_type, owner):
        return {'type': docyment_type, 'number': document_number, 'name': owner}

    def add_document(documents, directories, document, shelf_number):
        documents.append(document)
        directories.setdefault(shelf_number, []).append(document['number'])
        return [document, shelf_number]

    def remove_document(documents, directories, document_index, shelf_document_index):
        result_doc = documents.pop(document_index)
        result_dir = dir_delete_doc_number(directories, shelf_document_index)
        result = result_doc and result_dir != -1
        if result:
            return view_document(directories, result_doc)

    def view_document(directories, document):
        doc_type = document['type']
        number = document['number']
        owner = document['name']
        shelf = get_document_shelf(directories, document['number'])
        if shelf == -1:
            shelf = '-'
        message = f'Тип: {doc_type}\nНомер: {number}\nВладелец: {owner}\nПолка: {shelf[0]}'
        return message

    def is_document(document):
        return (type(document) == type(dict()) and
                document.get('number', False) and
                document.get('name', False) and
                document.get('type', False))

    def is_exit(command, elem):
        if elem == -1:
            command['message'] = 'Отмена команды'
            return True

    def not_validate_msg(command):
        command['message'] = 'Введите валидное значение или введите exit для отмены команды'
        post_message(command)

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

    def doc_type_input(command):
        result = None
        while not result:
            result = input(f'\n{command["component"]}@: Введите тип документа: ').strip()
            if result.isspace() or len(result) == 0:
                not_validate_msg(command)
                result = None
            elif result == 'exit':
                return -1
        return result

    def doc_owner_input(command):
        result = None
        while not result:
            result = input(f'\n{command["component"]}@: Введите имя владельца: ').strip()
            if result.isspace() or len(result) == 0:
                not_validate_msg(command)
                result = None
            elif result == 'exit':
                return -1
        return result

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

    def post_message(command):
        print(f'\n{command["component"]}@: {command["message"]}')

    def run_command(command, arg=None):
        if arg is None:
            arg = {}
        return command['func'](arg)

    def get_command_list(arg):
        command = arg['command']
        commands = arg['commands']
        message = ''
        for key, value in commands.items():
            message += f'\n"{key}" - {value["start"]}'
        message += '"exit" - Выход'
        command['message'] = message
        return True

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
