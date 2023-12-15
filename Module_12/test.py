from binarytree import Node

# Создание бинарного дерева вручную
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(10)

# Вывод структуры дерева
print("Структура бинарного дерева:")
print(root)

# Обход дерева в прямом порядке (preorder)
def preorder(node):
    if node is not None:
        print(node.value)
        preorder(node.left)
        preorder(node.right)
print("Обход дерева в прямом порядке (preorder):")
preorder(root)

# Поиск элемента в дереве
def search(node, value):
    if node is None or node.value == value:
        return node
    if value < node.value:
        return search(node.left, value)
    return search(node.right, value)

print("Поиск элемента в дереве:")
result = search(root, 7)
if result is not None:
    print("Элемент найден!")
else:
    print("Элемент не найден!")