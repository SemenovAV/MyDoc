from api.get_document_index import get_document_index
from api.is_exit import is_exit
from api.messenger.inputs.doc_number_input import doc_number_input


def get_people(arg):
    docs = arg['documents']
    command = arg['command']
    doc_number = doc_number_input(command)
    if is_exit(command, doc_number):
        return False
    index = get_document_index(docs, doc_number)
    if index != -1:
        result = docs[index].get('name')
        command['message'] = f'Документ с номером {doc_number} найден, владелец {result}'
        return True
    else:
        command['message'] = f'Документ с номером {doc_number} не найден.'
        return False
