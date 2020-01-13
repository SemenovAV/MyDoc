from api.get_document_shelf import get_document_shelf
from api.is_exit import is_exit
from api.messenger.inputs.doc_number_input import doc_number_input


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
