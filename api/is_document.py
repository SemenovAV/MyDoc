def is_document(document):
    return (isinstance(document, dict) and
            document.get('number', False) and
            document.get('name', False) and
            document.get('type', False))
