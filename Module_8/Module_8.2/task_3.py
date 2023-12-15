def f_value(structure, key):
    if key in structure:
        return structure[key]
    for sub_structure in structure.values():
        if isinstance(sub_structure, dict):
            rez = f_value(sub_structure, key)
            if rez:
                return rez
                break
    else:
        return None


print('Задача 3. Поиск элемента')

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

find_key = input('Искомый ключ: ')
find_value = f_value(site, find_key)
print('Значение:', find_value)
