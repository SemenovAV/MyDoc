def list_all_owner(arg):
    docs = arg['documents']
    command = arg['command']
    names = set()
    errors = 0
    counter = 0
    if len(docs) > 0:
        for doc in docs:

            try:
                name = doc['name']
            except KeyError as e:
                errors += 1
                break
            else:
                names.add(name)
        if len(names) > 0:
            for name in names:
                counter += 1
                command['message'] += f'{counter}. {name}\n'
        else:
            command['message'] = 'Имена не найдены'
        if errors > 0:
            command['message'] += f'---------\nДокументов с несуществующим ключем "name": {errors}'
    else:
        command['message'] = 'Документов нет'
        return False
    return True
