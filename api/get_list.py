from api.view_document import view_document


def get_list(documents, directories):
    result = ''
    for index, document in enumerate(documents):
        result += f'{index + 1}:\n{view_document(directories, document)}\n\n'
    result += f'Всего документов: {len(documents)}'
    return result or -1
