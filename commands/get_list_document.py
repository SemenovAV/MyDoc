from api.get_list import get_list


def get_list_document(arg):
    docs = arg['documents']
    dirs = arg['directories']
    command = arg['command']
    result = get_list(docs, dirs)
    if result != -1:
        command['message'] = f'\n{result}'
        return True
    else:
        command['message'] = 'Документы отсутствуют'
        return False
