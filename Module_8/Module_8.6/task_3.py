print('Задача 3. Помощь другу')

def create_dict(data, template=None):
    template = template or dict()
    if isinstance(data, dict):
        return data
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template[data] = data
        return template



def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        rez = create_dict(i_element)
        if rez:
            new_list.append(rez)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)
data_1 = [{43}, [12, 42, 1]]
data_1 = data_preparation(data_1)
print(data_1)

