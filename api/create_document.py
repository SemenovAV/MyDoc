def create_document(document_number, document_type, owner):
    return {'type': document_type, 'number': document_number, 'name': owner}
