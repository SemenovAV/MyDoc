def dir_add_doc_number(directories, document_number, shelf_number):
    shelf = directories.setdefault(shelf_number, [])
    new_value = list(directories.get(shelf_number))
    new_value.append(document_number)
    directories[shelf_number] = tuple(new_value)
    return document_number
