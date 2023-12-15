def foo(x):
    if x == 0:
        print("Вызов foo(0) возвращает 0")
        return 0
    else:
        print(f"Вызов foo({x - 1}) начинается и добавляется в стек")
        # new_result = foo(x - 1)
        # foo(x - 1)
        print(f"Вызов foo({x - 1}) завершился и удаляется из стека")
        result = x + foo(x - 1)
        return result
a = 3
b = foo(a)
print(b)