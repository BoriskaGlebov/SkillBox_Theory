class Example:
    def __init__(self):
        print("В функции __init__")

    def __enter__(self):
        print("В функции __enter__")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("В фукнции __exit__")
        return True
print('Задача 2. Пример')



my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')