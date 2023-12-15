import random, os

print('Задача 2. Возраст')

agent_file = open('agent.txt', 'w')
for i_line in range(10):
    agent_file.write(str(random.randint(1, 100)) + '\n')
agent_file.close()

try:
    agent_file = open('agent.txt', 'r')
    result_file = open('result.txt', 'x')
    # result_file = open(os.path.abspath(os.path.join('..', 'Module_11.2')), 'r')
    for i_line in agent_file:
        result_file.write((random.randint(ord('a'), ord('z')))
                          + chr(random.randint(ord('a'), ord('z')))
                          + ' ' + i_line.rstrip() + '\n')
    agent_file.close()
    result_file.close()
except (FileExistsError) as exc:
    print(f'{exc}Файл уже создан')
    os.remove('result.txt')
except PermissionError as exc:
    print(f'{type(exc)} путь к папке, а не файлу')
except (ValueError, TypeError) as exc:
    print(f'{exc} ошибка типа данных')
