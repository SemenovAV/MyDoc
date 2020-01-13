def get_document_shelf(directories, document_number):
    for shelf_number, document_numbers in directories.items():
        for index, number in enumerate(document_numbers):
            if number == document_number:
                return [shelf_number, index]
    return -1
