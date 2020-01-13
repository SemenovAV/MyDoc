from api.is_document import is_document


def get_document_index(documents, document_number):
    for index, document in enumerate(documents):
        if is_document(document) and document['number'] == document_number:
            return index
    return -1
