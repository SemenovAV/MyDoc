from api.get_document_shelf import get_document_shelf


def view_document(directories, document):
    doc_type = document['type']
    number = document['number']
    owner = document['name']
    shelf = get_document_shelf(directories, document['number'])
    if shelf == -1:
        shelf = '-'
    message = f'Тип: {doc_type}\nНомер: {number}\nВладелец: {owner}\nПолка: {shelf[0]}'
    return message