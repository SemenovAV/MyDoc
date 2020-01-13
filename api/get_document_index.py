def get_document_index(documents, document_number):
    for index, document in enumerate(documents):
        if document['number'] == document_number:
            return index
    return -1
