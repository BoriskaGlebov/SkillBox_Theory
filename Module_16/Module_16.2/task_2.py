import os
from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def in_dir(path: str) -> Iterator:
    try:
        os.chdir(path)
    except FileNotFoundError as exc:
        print(exc)
    yield


print('Задача 2. Директории')

with in_dir('C:\\'):
    print(os.listdir())
