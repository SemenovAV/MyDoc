def add_document(documents, directories, document, shelf_number):
    documents.append(document)
    directories.setdefault(shelf_number, []).append(document['number'])
    return [document, shelf_number]