def count_categories(result):
    list_id = []
    for key in result:
        if key['guid']:
            list_id.append(key['guid'])
        if len(key['subcategories']):
            for sub_key in key['subcategories']:
                if sub_key ['guid']:
                    list_id.append(sub_key['guid'])
                if len(sub_key['subcategories']):
                    for key in sub_key['subcategories']:
                        if key['guid']:
                            list_id.append(key['guid'])
    return len(set(list_id))


