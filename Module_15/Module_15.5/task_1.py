class File:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file= None

    def __enter__(self) -> object:
        self.file = open(self.path, self.mode, encoding='utf8')
        print(type(self.file))
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


print('Задача 1. Работа с файлом')

with File('example.txt', 'w') as file:
    file.write('Всем привет')
