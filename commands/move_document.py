from api.dir_add_doc_number import dir_add_doc_number
from api.dir_delete_doc_number import dir_delete_doc_number
from api.get_document_shelf import get_document_shelf
from api.is_exit import is_exit
from api.messenger.inputs.dirs_number_input import dirs_number_input
from api.messenger.inputs.doc_number_input import doc_number_input
from api.messenger.post_message import post_message


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
    result_del = dir_delete_doc_number(dirs, doc_shelf)
    if result_del != -1:
        result_add = dir_add_doc_number(dirs, doc_number, shelf)
        if result_add != -1:
            command['message'] = f'Документ номер {doc_number} перенесен с полки {doc_shelf[0]} на полку {shelf}'
            return True
        command['message'] = 'Ошибка добавления документа'
        return False
    command['message'] = 'Ошибка удаления документа'
    return False
