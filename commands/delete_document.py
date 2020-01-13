from api.get_document_index import get_document_index
from api.get_document_shelf import get_document_shelf
from api.is_exit import is_exit
from api.messenger.inputs.doc_number_input import doc_number_input
from api.remove_document import remove_document


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
