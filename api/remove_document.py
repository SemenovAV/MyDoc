from api.dir_delete_doc_number import dir_delete_doc_number
from api.view_document import view_document


def remove_document(documents, directories, document_index, shelf_document_index):
    result_doc = documents.pop(document_index)
    result_dir = dir_delete_doc_number(directories, shelf_document_index)
    result = result_doc and result_dir != -1
    if result:
        return view_document(directories, result_doc)