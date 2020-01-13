from api.add_document import add_document
from api.create_document import create_document
from api.get_document_shelf import get_document_shelf
from api.is_document import is_document
from api.is_exit import is_exit
from api.messenger.inputs.dirs_number_input import dirs_number_input
from api.messenger.inputs.doc_number_input import doc_number_input
from api.messenger.inputs.doc_owner_input import doc_owner_input
from api.messenger.inputs.doc_type_input import doc_type_input
from api.view_document import view_document


def add_new_document(arg):
    docs = arg['documents']
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
        result = add_document(docs, dirs, document, shelf_number)
        if result:
            command['message'] = f'Документ добавлен:\n\n{view_document(dirs, result[0])}'
            return True
        else:
            command['message'] = 'Ошибка добавления документа'
            return False
    else:
        command['message'] = 'Ошибка создания документа'
        return False
