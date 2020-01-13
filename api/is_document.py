def is_document(document):
    return (type(document) == type(dict()) and
            document.get('number', False) and
            document.get('name', False) and
            document.get('type', False))
