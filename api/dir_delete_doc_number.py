from api.get_shelf import get_shelf


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
