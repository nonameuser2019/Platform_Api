def count_categories(result):
    list_id = []
    for key in result:
        if key['id']:
            list_id.append(key['id'])
        if len(key['subcategories']):
            for sub_key in key['subcategories']:
                if sub_key ['id']:
                    list_id.append(sub_key['id'])
                if len(sub_key['subcategories']):
                    for key in sub_key['subcategories']:
                        if key['id']:
                            list_id.append(key['id'])
    return len(set(list_id))


